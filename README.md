# Vonage-QnA-app
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
 
 