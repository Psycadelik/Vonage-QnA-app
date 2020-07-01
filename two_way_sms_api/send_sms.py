from vonage.nexmo import nexmo_sms


def send_sms(message, number):
    text = message
    recipient = number
    print(nexmo_sms(text, recipient))
