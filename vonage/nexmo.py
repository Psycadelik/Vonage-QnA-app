import nexmo
import os
import argparse
from flask import jsonify


def nexmo_sms(sms, recipient):
    NEXMO_API_KEY = os.getenv("NEXMO_API_KEY")
    NEXMO_API_SECRET = os.getenv("NEXMO_API_SECRET")

    client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

    responseData = client.send_message(
        {
            "from": "Quizzie",
            "to": recipient,
            "text": sms,
        }
    )

    if responseData["messages"][0]["status"] == "0":
        return jsonify("Message sent successfully.")
    else:
        return jsonify(f"Message failed with error: {responseData['messages'][0]['error-text']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--sms',
        required=True)
    parser.add_argument(
        '--recipient',
        required=True
    )

    args = parser.parse_args()
    nexmo_sms(args.sms, args.recipient)
