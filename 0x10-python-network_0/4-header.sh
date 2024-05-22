#!/bin/bash
# This script takes a URL as input, sends a GET request using curl with a specific header, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
