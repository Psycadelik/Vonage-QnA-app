#!/usr/bin/env bash

json_file=$1
trigger=$2

cd ~/personal/QnA/vonage/ || exit 1

phone=$(<phone_numbers.txt)

cd ~/personal/QnA/dialogflowapi/ || exit 1

export GOOGLE_APPLICATION_CREDENTIALS="$json_file"

chmod +x push_intent.py

./push_intent.py --trigger "$trigger" --number "$phone"
