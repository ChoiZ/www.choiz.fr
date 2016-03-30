#!/bin/bash

# Convert all .rst files to .md

for file in `ls content/ |grep rst|cut -d '.' -f 1`;
    do `pandoc content/$file".rst" --from rst --to markdown_strict -o content/$file".md"`;
done;
