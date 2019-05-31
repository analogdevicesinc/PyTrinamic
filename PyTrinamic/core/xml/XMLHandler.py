#!/usr/bin/env python3
'''
Created: 31.05.2019

@author: LK
'''

import PyTrinamic
import re
from xml.etree.ElementTree import ElementTree

class Format(object):
    def __init__(self, name):
        if(name == "c_header"):
            return FormatCHeader()
        elif(name == "python"):
            return FormatPython()
        elif(name == "latex"):
            return FormatLatex()

class FormatCHeader(Format):
    def __init__(self):
        pass

class FormatPython(Format):
    def __init__(self):
        pass

class FormatLatex(Format):
    def __init__(self):
        pass

class RenameMode(object):
    def __init__(self, name):
        if(name == "remove"):
            return RenameModeRemove()
        elif(name == "replace"):
            return RenameModeReplace()

class RenameModeRemove(RenameMode):
    def __init__(self):
        pass

class RenameModeReplace(RenameMode):
    def __init__(self):
        pass

class DuplicateMode(object):
    def __init__(self, name):
        if(name == "comment"):
            return DuplicateModeComment()
        elif(name == "keep"):
            return DuplicateModeKeep()
        elif(name == "ignore"):
            return DuplicateModeIgnore()
        elif(name == "remove"):
            return DuplicateModeRemove()
        elif(name == "error"):
            return DuplicateModeError()

class DuplicateModeComment(DuplicateMode):
    def __init__(self):
        pass

class DuplicateModeKeep(DuplicateMode):
    def __init__(self):
        pass

class DuplicateModeIgnore(DuplicateMode):
    def __init__(self):
        pass

class DuplicateModeRemove(DuplicateMode):
    def __init__(self):
        pass

class DuplicateModeError(DuplicateMode):
    def __init__(self):
        pass

class XMLHandler():

    def __init__(self, file, rename_mode, duplicate_mode):
        self._rename_mode = rename_mode
        self._duplicate_mode = duplicate_mode
        self._tree = ElementTree.parse(file)
        self._root = tree.getroot()

    def convert(self, to):
        if(isinstance(to, FormatCHeader)):
            return self.to_c_header()
        else:
            raise NotImplementedError()

    def to_c_header(self):
        out = "#ifndef %(ic)s\n#define %(ic)s\n\n%(fields)s\n#endif" % { "ic": self._format_c_header(self._root.attrib["name"], self._rename_mode) }
        fstr = ""
        list = []
        remove = []
        max = 0
        for field in self._root.findall('.//{http://www.trinamic.com}value_register_field'):
            field_name = self._format_c_header(field.attrib["name"], self._rename_mode)
            if(len(field_name) > max):
                max = len(field_name)
            if(field_name in [i[0] for i in list]):
                if(isinstance(self._duplicate_mode, DuplicateModeComment)):
                    list.append((field_name, "//#define %(field)s_MASK %(wspace)s%(mask)s\n//#define %(field)s_SHIFT %(wspace)s%(shift)s"
                        % { "field": field_name, "mask": field.attrib["mask"], "shift": field.attrib["shift"] }))
                elif(isinstance(self._duplicate_mode, DuplicateModeKeep)):
                    list.append((field_name, "#define %(field)s_MASK %(wspace)s%(mask)s\n#define %(field)s_SHIFT %(wspace)s%(shift)s"
                        % { "field": field_name, "mask": field.attrib["mask"], "shift": field.attrib["shift"] }))
                elif(isinstance(self._duplicate_mode, DuplicateModeIgnore)):
                    pass
                elif(isinstance(self._duplicate_mode, DuplicateModeRemove)):
                    if(field_name not in remove):
                        remove.append(field_name)
                elif(isinstance(self._duplicate_mode, DuplicateModeError)):
                    raise IOError("Duplicate: %s" % field_name)
            else:
                dupelist.append(field_name)
                list.append((field_name, "#define %(field)s_MASK %(wspace_mask)s%(mask)s\n#define %(field)s_SHIFT %(wspace_shift)s%(shift)s"
                    % { "field": field_name, "mask": field.attrib["mask"], "shift": field.attrib["shift"] }))
            for r in remove:
                list = [f for f in list if f[0] == r]
            for field in list:
                fstr += (field[1] % { "wspace_mask": " " * (1 + max - len(field[0])), "wspace_shift": " " * (max - len(field[0])) }) + "\n"
        return (out % { "fields": fstr })

    def to_python(self):
        pass

    def to_latex(self):
        pass

    @staticmethod
    def _format_c_header(input, rename_mode):
        out = re.sub(r"(\[)(\d+)(\])", r"_\1", input.upper())
        if(isinstance(rename_mode, RenameModeRemove)):
            out = re.sub(r"[^\w\d_]", "", out)
        elif(isinstance(rename_mode, RenameModeReplace)):
            out = re.sub(r"[^\w\d_]", "_", out)
        return out
