#!/bin/bash
# Display the size of the status code of the response of a curl request
curl -so /dev/null --write-out "%{http_code}" "$1"
