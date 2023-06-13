#!/bin/bash

clear

modules=("cryptography" "pickle" "ply.lex" "ply.yacc" "hashlib" "json")
install_marker=".installed"

if [ ! -f "$install_marker" ]; then
    for module_name in "${modules[@]}"; do
        if python3 -c "import $module_name" &> /dev/null; then
            echo "$module_name is already installed."
        else
            echo "$module_name is not installed. Installing..."
            pip install $module_name
            echo "$module_name has been successfully installed."
        fi
    done

    touch "$install_marker"
fi

python3 mooYacc.py
python3 VirtualMachine.py

