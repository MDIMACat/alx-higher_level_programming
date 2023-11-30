#!/bin/bash
#Script that Makes a POST request for a JSON file
curl -s -x POST -H "Content-Type: application/json" -d @$2 $1
