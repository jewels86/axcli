import click
from colorama import Fore, Style
import axinite

@click.command("new")
def new():
    name = click.prompt("Enter the name of the system: ", type=str)
    author = click.prompt("Enter the author of the system: ", type=str)
    limit = click.prompt("Enter the time limit of the system in an interpretable form (none or -1 for infinite): ", type=str)
    delta = click.prompt("Enter the change in time of the system in an interpretable form: ", type=str)
    rate = click.prompt("Enter the framerate the system should be shown at: ", type=int)

    