#!/bin/bash
# A Bash script that sends a POST req to the passed URL and displays the res body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
