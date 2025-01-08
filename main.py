import click
from axcli import *

@click.group()
def cli():
    pass

cli.add_command(new)
cli.add_command(read)
cli.add_command(load)
cli.add_command(catalog)
cli.add_command(run)

if __name__ == "__main__":
    cli()