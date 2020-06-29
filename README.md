# Vonage-QnA-app
The project structure looks like this:
```
.
├── conversationapi
│   ├── bash_scripts
│   │   └── create_conversation.sh
│   ├── js_scripts
│   │   └── vonage_sdk_node
│   │       ├── create_conversation.js
│   │       ├── package.json
│   │       ├── package-lock.json
│   │       └── README.md
│   ├── python_scripts
│   │   └── create_conversation.py
│   ├── README.md
│   └── vonage.txt
├── dialogflowapi
│   ├── google.txt
│   ├── __init__.py
│   ├── intent_texts.py
│   ├── README.md
│   └── test_credentials.py
├── entry-point.sh
├── instance
├── nexmo.txt
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── settings.py
├── tests
│   ├── __init__.py
│   ├── test_answer_web_hook.py
│   ├── test_create_users.py
│   ├── test_event_web_hook.py
│   ├── test_jwt_token_generation.py
│   ├── test_notify_web_hook.py
│   └── test_update_web_hook.py
├── two_way_sms_api
│   ├── __init__.py
│   ├── notify_customer.py
│   └── send_sms.py
├── vonage
│   ├── config.py
│   ├── db.py
│   ├── __init__.py
│   ├── models.py
│   ├── nexmo.py
│   ├── phone_numbers.txt
└── wsgi.py
```

### what are we trying to do?
  - Create a conversation :
    - open your terminal
    - type: `JWT=your-jwt-token`
    - type: `CONV_NAME=your-conversation-name`
    - type: `CONV_DISPLAY_NAME=your-conversation-display-name`
    
   background actions:
    - chmod +x create_conversation.sh
   
   Run on your terminal: `./create_conversation.sh`
 
  -  Integrate to the Vonage 2-way SMS API:
     - configure a virtual nexmo number
     - create a basic web app
     - send an sms notification
     - process the reply sms
  
  - The game logic
    - A user has to be under either Geographical, Historical or Entertainment chatroom
    - A user starts the game by texting play
    - They receive a reply with the first question
    - They correct answer has to be a choice of either A, B, C or D
    - For each correct answer, a user gets 2 points and for each wrong answer a user gets 0 points
    - at the end of the ten questions, a user gets a summary of their questions and answers and their final score
    
  That's it :-)
 
## How it works(web):
 - the `/webhooks/notify` url expects a number in the post request payload
```
e.g:
{
    "number": +187678490
}
```
 - after receiving the number, the webhook responds with the following question to the 
 end user: `Hello. You can start your quiz with quizzie-bot by sending the following keywords: hi, hello or vonage.`

- the user responds to this using the provided key words which are now handled by the
`/webhooks/update` url

- dialogflow takes over from here
 
 ## How it works, bash:
- entry point takes an argument of txt file
```
./entry-point.sh vonage/phone_numbers.txt
``` 
