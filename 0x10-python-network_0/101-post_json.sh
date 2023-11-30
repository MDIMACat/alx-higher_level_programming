#!/bin/bash
#Script that Makes a POST request for a JSON file
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
