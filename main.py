import os
import json
import typer
import asyncio

from tester import test


def load_config(file):

    if os.path.exists(file) is False:
        raise ValueError("Invalid file path! It does not exist")
        exit(1)

    with open(file, "r") as f:
        data = json.load(f)
    # data = json.loads(file)

    return data


def main(file: str = None):
    if file is None:
        print("Default config file will be used")
        file = "config.json"
        print("Using default config.json file")

    config = load_config(file)

    asyncio.get_event_loop().run_until_complete(test(config))


if __name__ == "__main__":
    typer.run(main)
