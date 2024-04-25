#!/bin/bash
# This script takes a URL as input, sends a request using curl,
# and displays the size of the response body in bytes

curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r\n'
