#!/bin/sh
find ./out -type f \( -name '*.html' -o -name '*.css' -o -name '*.js' -o -name '*.xml' \)  -exec sh -c "gzip -7 -f < {} > {}.gz" \;
