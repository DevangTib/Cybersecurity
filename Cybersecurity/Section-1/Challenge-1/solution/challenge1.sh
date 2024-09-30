#!/bin/bash

i=1
while true; do
    # Find the file with no extension
    no_extension=$(find . -maxdepth 1 -type f ! -name "*.*" | head -n 1)
    
    if [ -z "$no_extension" ]; then
        echo "No file without extension found!"
        exit 1
    fi
    
    pass=$(cat "$no_extension")
    
    if grep -q "flag" "$no_extension"; then
        echo "$pass"
        exit 0
    fi

    # Check for .zip files
    zip_file=$(ls -1 *.zip 2>/dev/null)
    zip_file_count=$(ls -1 *.zip 2>/dev/null | wc -l)

    if [ "$zip_file_count" -eq 1 ]; then
        output=$(python3 /mnt/c/Users/devan/Desktop/ls2024/self-cybersecurity/section1/base64_convert.py "$pass")
        base64_encoded=$(echo "$output" | sed -n '1p')
        base32_encoded=$(echo "$output" | sed -n '2p')
        hex_encoded=$(echo "$output" | sed -n '3p')
        text_itself=$(echo "$output" | sed -n '4p')

        passwords=("$base64_encoded" "$base32_encoded" "$hex_encoded" "$text_itself")

        mkdir -p "$i"
        for password in "${passwords[@]}"; do
            unzip -P "$password" "$zip_file" -d "$i" && break
        done
        cd "$i" || exit
        ((i=i+1))

    else
        # Check for .7z files
        zip_file=$(ls -1 *.7z 2>/dev/null)
        zip_file_count=$(ls -1 *.7z 2>/dev/null | wc -l)
        
        if [ "$zip_file_count" -eq 1 ]; then
            output=$(python3 /mnt/c/Users/devan/Desktop/ls2024/self-cybersecurity/section1/base64_convert.py "$pass")
            base64_encoded=$(echo "$output" | sed -n '1p')
            base32_encoded=$(echo "$output" | sed -n '2p')
            hex_encoded=$(echo "$output" | sed -n '3p')
            text_itself=$(echo "$output" | sed -n '4p')

            passwords=("$base64_encoded" "$base32_encoded" "$hex_encoded" "$text_itself")

            mkdir -p "$i"
            for password in "${passwords[@]}"; do
                7z x -p"$password" "$zip_file" -o"$i" && break
            done
            cd "$i" || exit
            ((i=i+1))
        else
            echo "No valid .zip or .7z file found"
            exit 1
        fi
    fi
done
