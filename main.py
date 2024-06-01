import click
import json

@click.command()
@click.option("--payload", default="{}", help="coordinates in json format")

def getData(payload):
    """Simple program that greets NAME for a total of COUNT times."""
    parsedData = json.loads(payload)
    print(parsedData)


if __name__ == '__main__':
    getData()