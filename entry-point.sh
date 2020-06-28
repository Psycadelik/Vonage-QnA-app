#!/usr/bin/env bash
set e

# direct this script to initiate by notifying the customer to begin the quiz
cd ~/personal/QnA/two_way_sms_api/ || exit

# this is the phone number passed as argument when running the script
filename=$1

#read the contents of phone_numbers.txt
while read -r line;do
  name="$line"
  echo "Name read from file - $name"
done < "$filename"

#run the python script to send the initial message to the customer
> python3 notify_customer.py --phone_number name || exit 1

cd ~/ || exit
