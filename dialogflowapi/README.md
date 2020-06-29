# the steps to setup your application on Google Cloud
- visit https://console.cloud.google.com 
- create a new project : 
   take note of the project ID
- Enable the DialogFlow API from the list of APIs
- To be able to test the DialogFlow API, we need to download the GCP credentials
- Navigate to credentials under DialogFlow project and select create credentials
- create a service account
- Download the credentials file provided as json
- locally, assuming you're using Linux/Mac: `export GOOGLE_APPLICATION_CREDENTIALS=my-key.json`
- you can now make requests

# creating a DialogFlow agent
- create an agent on the DialogFlow console
- while selecting a Google Project, select the project created on GCP for purposes of linking the service account
- to make the requests to the Console, run the following:
    
    - `export GOOGLE_APPLICATION_CREDENTIALS=my-key.json`
    - `python detect_intent_texts.py --project-id PROJECT-ID --session-id 12345678 "your-message-here"` 
