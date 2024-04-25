#!/bin/bash
# This script retrieves the size of the response body from a URL (bytes)

curl -s "${1}" | wc -c
