#!/bin/bash
#Script returns status code
curl -s -I -w "%{http_code}" -o /dev/null  $1
