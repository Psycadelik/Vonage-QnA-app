from vonage.nexmo import nexmo_sms


def send_sms(message, number):
    text = message
    recipient = number
    return nexmo_sms(text, recipient)

#
# if __name__ == "__mian__":
#     send_sms(message=,)
