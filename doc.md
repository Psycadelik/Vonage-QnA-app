### CREATING A QUESTION AND ANSWER GAME USING DIALOGFLOW API,  THE VONAGE MESSAGES API AND PYTHON FLASK

We will be using DialogFlow API to build a quiz bot that interacts with the end user via sms, which is made possible by the vonage SMS API. 

### PREREQUISITES

This article requires that you have setup an account with nexmo and created a messages api application. We will begin by using the nexmo interactive CLI mode to create an app.

Install the nexmo CLI on your machine as follows:

`npm install nexmo-cli@beta -g`

Create a directory for you application locally: `mkdir your-application`

 Inside the directory, run the following command:
nexmo app:create

In the interactive CLI mode:

```
Application Name: your-app-name
Select capabilities: press the space bar to select voice, messages and rtc
Use default HTTP methods?: yes
Voice answer url: press enter to leave it as default (https://example.com)
Voice Fallback Answer URL: Optional
Voice Event URL: press enter to leave it as default (https://example.com)
Messages Inbound URL: use ngrok to create a URL
Messages Status URL: press enter to leave it as default (https://example.com)
RTC Event URL: press enter
Public key path: press enter
Private Key path: your private key (downloadable from the nexmo dashboard)

```      

The application should now be created. Visit https://dashboard.nexmo.com and navigate to applications. Your shiny new app should be listed there.

Up Next we need to setup the DialogFlow agent:


SETTING UP THE DIALOGFLOW AGENT

To setup the DialogFlow agent, we first need to visit : https://console.cloud.google.com. 

Create a new project: 

![Screenshot from 2020-07-01 17-36-37](https://user-images.githubusercontent.com/8037388/86770437-59d56100-c059-11ea-997e-1e8fa0b976bf.png)


Take note of the PROJECT ID
Enable the DialogFlow API from the list of APIs:

![Screenshot from 2020-07-07 12-02-28](https://user-images.githubusercontent.com/8037388/86770507-77a2c600-c059-11ea-8243-f68838aae4c4.png)

Visit https://dialogflow.cloud.google.com to create a new agent:

![create-agent](https://user-images.githubusercontent.com/8037388/86769973-a79d9980-c058-11ea-91f5-14d569739657.png)


At the end of this article, there’s a link to the github repository. Navigate to the dialogflow directory and under the resources download the quizzie.zip file

On the dialogflow dashboard, click settings and navigate to export/import. Import the zip file we just downloaded:

![dialogflow-create-agent](https://user-images.githubusercontent.com/8037388/86770186-f814f700-c058-11ea-8a5c-e70f652813ca.png)


Our dialogflow quiz agent is all setup and ready to go


##### PAUSE:  So far we have created our nexmo application and went ahead and created our dialogflow agent that we intend to use in creating our quiz game.

For the next steps we need to create the logic that will handle the back and forth messaging between the end user and our DialogFlow agent.

### Our Functionality code in Python

We want to begin by initiating an sms to the end user, but first:

 - Rent a nexmo number from the dashboard
 - Install the nexmo library via pip: pip install nexmo
 - Set up the nexmo function that enables the sending of messages:

![nexmo-code](https://user-images.githubusercontent.com/8037388/86770219-05ca7c80-c059-11ea-908c-add0ecd08428.png)

Next add the code that will notify our customer:

![notify](https://user-images.githubusercontent.com/8037388/86770240-0ebb4e00-c059-11ea-98bf-e7d882b9d5ba.png)


Once the end user receives the messages, we want them to reply to them. Nexmo requires a webhook setup. Remember we setup an inbound sms URL while creating an app at the top. It is now time to add logic to our webhook.

![route](https://user-images.githubusercontent.com/8037388/86770266-17138900-c059-11ea-9520-ae0ff28ddb84.png)

In addition, We need to chain the responses we receive from the end user as input to our dialogflow agent. For this we need to use the DialogFlow REST Agent.

Specifically we need to detect the user intent and pass it as input to the agent.

![detect-intent](https://user-images.githubusercontent.com/8037388/86770166-edf2f880-c058-11ea-9752-a7642b0c935c.png)

### CONCLUSION

Our setup is now complete. The user is now able to send and receive sms messages which has been made possible by using our DialogFlow agent and the Vonage Messages API.

Note:
  - The intents aren’t cast in stone and can be edited at will. 
  - You need to rent/buy a nexmo number to be able to test this out on your phone.


The full code sample is available on this repo:  https://github.com/Psycadelik/Vonage-QnA-app . For any further questions, feel free to contact me via mail (adriannduva@gmail.com). 
 

