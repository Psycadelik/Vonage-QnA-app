import requests
import argparse


def create_conversation(jwt, name, display_name):
    r = requests.post(
        "https://api.nexmo.com/beta/conversations",
        params={
            "mame": "{}".format(name),
            "display_name": "{}".format(display_name)
        },
        headers={
            "authorization": "Bearer {}".format(jwt),
            "content-type": "application/json"
        }
    )
    response = r.json()
    print(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--jwt',
        required=True)
    parser.add_argument(
        '--name',
        required=True)
    parser.add_argument(
        '--display_name',
        required=True)

    args = parser.parse_args()

    create_conversation(
        args.jwt, args.name, args.display_name)
