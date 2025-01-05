import click
from axcli import *

@click.group()
def cli():
    pass

cli.add_command(new)

if __name__ == "__main__":
    cli()