#!/bin/bash

# Breaking this up into two different steps makes it easier to resume the process.
# The server does not allow HEAD requests and doesn't send last modified headers, so
# we can't use wget's timestamping feature to resume the download.

# Get all the URLs to download
python3 -m pip install -r requirements.txt
python3 ./src/mirror.py

# Download the legislation.govt.nz website
# The web server doesn't allow using a more descriptive user agent
aria2c -x4 \
    --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" \
    --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" \
    --header="Accept-Language: en-US,en;q=0.9,es;q=0.8" \
    --continue true \
    -i urls.txt


