#!/usr/bin/env python3
'''
Created: 29.05.2019

@author: LK
'''

import PyTrinamic
import argparse
from PyTrinamic.core.xml.XMLHandler import *

parser = argparse.ArgumentParser(description='Convert XML module descriptors to various output formats.')
parser.add_argument('inputs', metavar='input', type=argparse.FileType('r'), nargs='+',
                    help='XML module descriptor')
parser.add_argument('--format, -f', dest='format', action='store', nargs=1, choices=['c_header', 'python', 'latex'], default='c_header',
                    help='Conversion format')
parser.add_argument('--output, -o', dest='output', action='append', type=argparse.FileType('w'), nargs='*',
                    help='Output file for n-th descriptor')
parser.add_argument('--outdir, -O', dest='outdir', action='store', type=argparse.FileType('w'), nargs=1,
                    help='Output directory for all descriptors')
parser.add_argument('--mode, -m', dest='mode', action='store', nargs=1, choices=['remove', 'replace'],
                    help='Replacement mode')
parser.add_argument('--duplicates, -d', dest='dmode', action='store', nargs=1, choices=['comment', 'keep', 'ignore', 'remove', 'error'],
                    help='Duplicate handling mode')

args = parser.parse_args()
