import click
from axcli import *

@click.group()
def cli():
    pass

cli.add_command(new)
cli.add_command(read)

if __name__ == "__main__":
    cli()