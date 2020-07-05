# Vonage-QnA-app
[![Actions Status](https://github.com/Psycadelik/Vonage-QnA-app/workflows/Quizzie/badge.svg)](https://github.com/Psycadelik{user}/Vonage-Qna-app/actions)


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
│   ├── conversation-rolldown.sh
│   ├── README.md
│   └── vonage.txt
├── dialogflowapi
│   ├── google.txt
│   ├── __init__.py
│   ├── intent_texts.py
│   ├── README.md
│   └── test_credentials.py
├── entry-point.sh
├── .env
├── instance
├── nexmo.txt
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── settings.py
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
## setup instructions:
- clone the repository to your local folder:
```
git clone git@github.com:Psycadelik/Vonage-QnA-app.git QnA
```
- edit this file and add a valid phonenumber
```
nano QnA/vonage/phone_numbers.txt
```
- rent a valid number from vonage and edit the file:
```
- nano vonage/nexmo.py

response_data = client.send_message(
        {
            "from": "valid-number",
            "to": recipient,
            "text": sms,
        }
    )
```
- initiate an SMS to the end user to start playing the game
```
./entry-point.sh vonage/phone_numbers.txt
```

The user receives the following message:
```
Hello. You can start your quiz with quizzie-bot by sending the following keywords:
hi, hello or vonage.
```

- The DialogFlow agent takes over from here :-)

