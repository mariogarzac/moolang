#!/bin/bash

clear
# rm parser.out
# rm parsetab.py

if [ -z "$1" ] || [ -z "$2" ]; then
    python3 mooYacc.py 
else
    python3 mooYacc.py | sed -n "/Tests\/$1\.moo/,/$2\.moo/p"
fi
