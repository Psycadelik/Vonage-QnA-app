#! /usr/bin/env python3
import argparse
import sys
import os

from dotenv import load_dotenv

sys.path.append('../')
from vonage.nexmo import nexmo_sms

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')  # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


def notify_customer(number):
    text = "Hello. You can start your quiz with quizzie-bot by sending the following keywords: hi," \
           " hello or vonage."
    print(nexmo_sms(text, number))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--phone_number",
        required=True)

    args = parser.parse_args()

    notify_customer(args.phone_number)
