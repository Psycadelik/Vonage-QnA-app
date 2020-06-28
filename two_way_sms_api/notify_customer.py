import argparse
from vonage.nexmo import nexmo_sms


def notify_customer(number):
    text = "Hello. You can start your quiz with quizzie-bot by sending the following keywords: hi," \
           " hello or vonage."
    return nexmo_sms(text, number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--phone_number",
        required=True)

    args = parser.parse_args()

    notify_customer(args.number)
