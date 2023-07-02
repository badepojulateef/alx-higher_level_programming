#!/bin/bash
# sends a JSON POST req, and displays the body of the res
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
