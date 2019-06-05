#!/usr/bin/env python3
'''
Created: 29.05.2019

@author: LK
'''

import PyTrinamic
import argparse
import re
import os
from PyTrinamic.helpers import v_func
from PyTrinamic.Strings import Strings
from PyTrinamic.core.xml.XMLHandler import *

parser = argparse.ArgumentParser(description='Convert XML module descriptors to various output formats.')
parser.add_argument('inputs', metavar="input", type=str, nargs='+',
                    help='XML module descriptor file or directory')
parser.add_argument('--format', dest='format', action='store', nargs=1, type=str, choices=['c_header', 'python', 'latex'], default=['c_header'],
                    help='Conversion format (default: %(default)s)')
parser.add_argument('--output', dest='output', action='append', type=argparse.FileType('w'), nargs='*',
                    help='Output file for n-th descriptor')
parser.add_argument('--outdir', dest='outdir', action='store', type=str, nargs=1, default=".",
                    help='Output directory for all descriptors (default: %(default)s)')
parser.add_argument('--mode', dest='mode', action='store', nargs=1, type=str, choices=['remove', 'replace'], default=["replace"],
                    help='Rename mode (default: %(default)s)')
parser.add_argument('--duplicates', dest='dmode', action='store', nargs=1, type=str, choices=['comment', 'keep', 'ignore', 'remove', 'error'], default=["comment"],
                    help='Duplicate handling mode (default: %(default)s)')
parser.add_argument('--verbosity', dest='verbosity', action='store', nargs=1, type=int, choices=[0, 1, 2], default=1,
                    help='Verbosity level (default: %(default)s, 0: no output, 2: highest detail)')

args = parser.parse_args()

verbosity = args.verbosity[0]

v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "Raw arguments:"))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "args.inputs:", args.inputs))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "args.format:", args.format))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "args.output:", args.output))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "args.outdir:", args.outdir))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "args.mode:", args.mode))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "args.dmode:", args.dmode))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "args.verbosity:", args.verbosity))

format = Format.from_string(args.format[0])
mode = RenameMode.from_string(args.mode[0])
dmode = DuplicateMode.from_string(args.dmode[0])

v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "Interpreted arguments:"))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "format:", format))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "mode:", mode))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "dmode:", dmode))
v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "verbosity:", verbosity))

files = []
for input in args.inputs:
    if(os.path.isfile(input)):
        v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "File detected:", input))
        files.append(input)
    elif(os.path.isdir(input)):
        v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "Directory detected:", input))
        for root, dirs, fils in os.walk(input, topdown=True):
            for f in fils:
                v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "File in subdirectory:", os.path.join(root, f)))
                files.append(os.path.join(root, f))
for file in files:
    v_func(verbosity, 1, lambda: print(Strings.CLI_INFO, "Converting file", file, "..."))
    if(os.path.splitext(file)[1] == ".xml"):
        v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "XML descriptor detected:", file))
        xml = XMLHandler(file, mode, dmode, verbosity=verbosity)
        if(args.output):
            ofile = args.output.pop(0)
            v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "Using specified output:", ofile.name))
        else:
            v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "Using output directory:", args.outdir))
            ofile = open(os.path.join(args.outdir, "%s.%s" % (os.path.splitext(os.path.basename(file))[0], format.get_extension())), "w")
        v_func(verbosity, 2, lambda: print(Strings.CLI_INFO, "Output file:", ofile.name))
        ofile.write(xml.convert(format))
        ofile.close()
    else:
        v_func(verbosity, 1, lambda: print(Strings.CLI_WARNING, "Not a XML descriptor:", file, ", skipping..."))
