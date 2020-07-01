#!/usr/bin/env python3

import argparse
import os
import sys

sys.path.append('../')
from vonage.nexmo import nexmo_sms
from two_way_sms_api.send_sms import send_sms
from .intent_texts import detect_intent_texts


def push_intent_to_gcp(trigger, number):
    project_id = os.getenv("PROJECT_ID")
    session_id = os.getenv("SESSION_ID")
    language_code = os.getenv("LANG_CODE")

    response = detect_intent_texts(project_id, session_id, trigger, language_code)

    print(nexmo_sms(response, number))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--trigger',
        required=True)
    parser.add_argument(
        '--number',
        required=True)

    args = parser.parse_args()

    push_intent_to_gcp(args.trigger, args.number)
