#!/bin/bash

# Path to the .txt file containing the package names
FILE="installed.txt"

# Check if file exists and is not empty
if [ ! -s "$FILE" ]; then
    echo "The file $FILE does not exist or is empty."
    exit 1
fi

# Loop to process package names in batches of 5
while [ -s "$FILE" ]; do
    # Read the first 5 names and store them in an array
    mapfile -t batch < <(head -n 5 "$FILE")

    # Check if batch is empty (in case of unexpected file changes)
    if [ "${#batch[@]}" -eq 0 ]; then
        break
    fi

    # Echo the 5 names to stdout for review
    echo "The following packages will be removed:"
    printf "%s\n" "${batch[@]}"

    # Run apt remove, capturing output and errors
    apt_output=$(printf "%s\n" "${batch[@]}" | xargs -I {} apt remove -y {} 2>&1)

    # Print the output from apt remove for review
    # echo "$apt_output"

    # Check if apt remove succeeded
    if [[ "$apt_output" == *"Use 'apt autoremove' to remove them"* ]]; then
        echo "Running 'apt autoremove' as suggested..."
        apt autoremove -y
        sleep 1  # Delay for 1 second before proceeding
    fi

    # Remove the processed names from the file
    sed -i '1,5d' "$FILE"

    # Sleep for 3 seconds before processing the next batch
    sleep 3
done

echo "All packages processed."

