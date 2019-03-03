import click
from cogeotiff.validate_cogeotiff import main_validate

@click.command()
@click.argument('cog_path', type=str)
def validate_cog_command(cog_path):
    main_validate(cog_path)