#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import subprocess
import argparse
source = 'smallify-all'


previous_dir = os.getcwd()
primary_folder = ""
current = "."
primary_foler_flag = False

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--depth', type=int)
args = parser.parse_args()

if args.depth is not None:
    MAX_DEPTH = args.depth
    print(f'Depth is {MAX_DEPTH}')
else:
    MAX_DEPTH = 100
    print('Infinite depth (100)')

print("Launching smallify-all in current folder")
subprocess.call(source)

if MAX_DEPTH > 0:
    for root, dirs, files in os.walk(current, topdown=True):
        for name in dirs:
            if name != "Smaller_comics":
                path = (os.path.join(root, name))
                if root.count(os.sep) - current.count(os.sep) == MAX_DEPTH - 1:
                    del dirs[:]
                try:
                    os.chdir(path)
                    print("Launching smallify-all in " + path)
                    subprocess.call(source)
                    os.chdir(previous_dir)
                except Exception as e:
                    print(e)
                    pass
