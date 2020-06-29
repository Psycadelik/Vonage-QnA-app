import nexmo
import os
import json


def nexmo_sms(sms, recipient):
    NEXMO_API_KEY = os.getenv("NEXMO_API_KEY")
    NEXMO_API_SECRET = os.getenv("NEXMO_API_SECRET")

    client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

    response_data = client.send_message(
        {
            "from": "Quizzie",
            "to": recipient,
            "text": sms,
        }
    )

    if response_data["messages"][0]["status"] == "0":
        return json.dumps("Message sent successfully.")
    else:
        return json.dumps(f"Message failed with error: {response_data['messages'][0]['error-text']}")
