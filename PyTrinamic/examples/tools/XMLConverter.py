#!/usr/bin/env python3
'''
Created: 29.05.2019

@author: LK
'''

import PyTrinamic
import argparse
import re
import os
from PyTrinamic.core.xml.XMLHandler import *

parser = argparse.ArgumentParser(description='Convert XML module descriptors to various output formats.')
parser.add_argument('inputs', metavar="input", type=str, nargs='+',
                    help='XML module descriptor file or directory')
parser.add_argument('--format, -f', dest='format', action='store', nargs=1, type=str, choices=['c_header', 'python', 'latex'], default='c_header',
                    help='Conversion format')
parser.add_argument('--output, -o', dest='output', action='append', type=argparse.FileType('w'), nargs='*',
                    help='Output file for n-th descriptor')
parser.add_argument('--outdir, -O', dest='outdir', action='store', type=str, nargs=1, default=".",
                    help='Output directory for all descriptors')
parser.add_argument('--mode, -m', dest='mode', action='store', nargs=1, type=str, choices=['remove', 'replace'], default="replace",
                    help='Rename mode')
parser.add_argument('--duplicates, -d', dest='dmode', action='store', nargs=1, type=str, choices=['comment', 'keep', 'ignore', 'remove', 'error'], default="comment",
                    help='Duplicate handling mode')
parser.add_argument('--verbosity, -v', dest='verbosity', action='store', nargs=1, type=int, choices=[0, 1], default=0,
                    help='Verbosity level')

args = parser.parse_args()

format = Format.from_string(args.format)

for file in args.inputs:
    xml = XMLHandler(file, RenameMode.from_string(args.mode), DuplicateMode.from_string(args.dmode), verbosity=args.verbosity)
    if(args.output):
        of = args.pop(0)
    else:
        of = open(os.path.join(args.outdir, "%s.%s" % (os.path.splitext(os.path.basename(file.name))[0], format.get_extension())), "w")
    of.write(xml.convert(format))
    of.close()
