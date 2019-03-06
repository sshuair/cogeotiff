import click
from cogeotiff.validate_cogeotiff import validate_cog

@click.command()
@click.argument('cog_path', type=str)
def validate_cog_command(cog_path):
    validate_cog(cog_path)