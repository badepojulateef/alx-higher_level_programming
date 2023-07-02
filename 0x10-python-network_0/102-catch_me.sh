#!/bin/bash
# A script that makes a req to 0.0.0.0:5000/catch_me and displays the res
curl -sL -X PUT  -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
