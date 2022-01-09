#!/bin/bash
# take in a URL sends a request to it, and displays the size of the body of the response
curl -w '%{size_download}\n' -so /dev/null $1