#!/usr/bin/env bash

# this is the phone number passed as argument when running the script
filename=$1

#read the contents of phone_numbers.txt
while read -r line;do
  number="$line"
  echo "PhoneNumber read from file - $number"
done < "$filename"

# direct bash to the root folder
cd ~/personal/QnA/two_way_sms_api/ || exit

chmod +x notify_customer.py

#run the python script to send the initial message to the customer
./notify_customer.py --phone_number "$number" || exit 1

cd ~/ || exit
