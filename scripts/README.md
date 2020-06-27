- ensure you have nexmo CLI installed using: `npm install nexmo-cli@beta -g
`
- set up account: `nexmo setup <api-key> <api-secret>`
   - credentials are written to : `/home/<User>/.nexmorc`
- For more details visit the repo: https://github.com/Nexmo/nexmo-cli/tree/beta
 app setup
- nexmo app:setup APP_ID ./private_key 

Generating JWT tokens:

- `nexmo jwt:generate ./private.key sub=jamie exp=$(($(date +%s)+86400)) acl='{"paths":{"/*/users/**":{},"/*/conversations/**":{},"/*/sessions/**":{},"/*/devices/**":{},"/*/image/**":{},"/*/media/**":{},"/*/applications/**":{},"/*/push/**":{},"/*/knocking/**":{}}}' application_id=YOUR_APP_ID`
- copy the JWT string generated (default expiration is 15 minutes)
- Run the following to generate a conversation

- ` -$ JWT=the-jwt-token-string-copied-above`
- ` -$ CONV_NAME=the-conversation-name-you-intend-to-use`
- ` -$ CONV_DISPLAY_NAME=your-preferred-display-name`

creating a conversation:

bash:
- run `./create_conversation.sh`

JS:
- run `node create_conversation.js`

Python:
- run `python3 create_conversation.py --jwt JWT --name Name --display_name DisplayName`
