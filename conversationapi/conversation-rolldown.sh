#!/usr/bin/env bash

#Ensure you have nexmo CLI installed: npm install nexmo-cli@beta -g

api_key=$1
api_secret=$2
app_id=$3

#setup your nexmo account:
nexmo setup "$api_key" "$api_secret" || exit 1

#the above command writes your credentials to /home/<user>/.nexmorc

#navigate to the directory that contains the private key
cd ~/<your-app-directory>/ || exit 1

#set up your app
nexmo app:setup  "$app_id" ./private.key

#create a user
nexmo user:create name="example-user"

#generate a JWT token
token=$(nexmo jwt:generate ./private.key sub=example-user exp=$(($(date +%s)+86400)) acl='{"paths":{"/*/users/**":{},"/*/conversations/**":{},"/*/sessions/**":{},"/*/devices/**":{},"/*/image/**":{},"/*/media/**":{},"/*/applications/**":{},"/*/push/**":{},"/*/knocking/**":{}}}' application_id="$app_id")

#navigate to create_conversation script
cd ~/<your-app-directory>/conversationapi/python_scripts/ || exit 1

#make the script executable
chmod +x create_conversation.py

#create a conversation
./create_conversation.py --jwt $token --name="example-name" --display_name="better-name"

#exit
cd ~/ || exit 1
