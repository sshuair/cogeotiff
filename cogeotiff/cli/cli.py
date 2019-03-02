import click
from .create import create_cog_command

@click.group()
@click.argument("arg", help="help message")
def entry_point():
    pass

# entry_point.add_command(create_cog_command)