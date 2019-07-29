#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import subprocess
import argparse


source = 'smallify-all'
default_folder = "Smaller_comics"
custom_folder = "Smaller_comics"
command = []
command.append(source)


previous_dir = os.getcwd()
primary_folder = ""
current = "."
primary_foler_flag = False

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--depth', type=int,
                    help="depth of recursivity")
parser.add_argument('-f', '--folder', type=str,
                    help="Custom folder for smallified comics")
parser.add_argument('-r', '--replace', action='store_true',
                    help="REPLACE YOUR COMICS ! CAREFUL")
args = parser.parse_args()

if args.depth is not None:
    MAX_DEPTH = args.depth
    print(f'Depth is {MAX_DEPTH}')
else:
    MAX_DEPTH = 100
    print('Infinite depth (100)')

if args.replace is not None:
    if args.replace:
        print("REPLACE mode")
        command.append('-r')
    else:
        print("NOMRMAL mode")

if args.folder is not None:
    custom_folder = args.folder
    command.extend(['-f', custom_folder])

print("Launching smallify-all in current folder")
subprocess.call(command)

if MAX_DEPTH > 0:
    for root, dirs, files in os.walk(current, topdown=True):
        for name in dirs:
            if (name != default_folder and
                    name != custom_folder and
                    name != "Working"):
                path = (os.path.join(root, name))
                deg_of_sep = path.count(os.sep) - current.count(os.sep)
                if deg_of_sep > MAX_DEPTH:
                    pass
                else:
                    try:
                        os.chdir(path)
                        print("Launching smallify-all in " + path)
                        subprocess.call(command)
                        os.chdir(previous_dir)
                    except Exception as e:
                        print(e)
                        pass
