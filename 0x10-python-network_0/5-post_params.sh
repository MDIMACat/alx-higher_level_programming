#!/bin/bash
#POST request with data to add
curl -s -X POST -d email=test@gmail.com -d subject='I will always be here for PLD' $1
