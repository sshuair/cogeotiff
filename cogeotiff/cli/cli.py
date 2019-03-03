import click
from .create import create_cog_command
from .validate import validate_cog_command

@click.group()
def entry_point():
    '''Cloud Optimized GeoTiff tools for create COG file and validate COG file.

\b 
    command:
        [cog create] : create Cloud Optimized GeoTiff.
        [cog validate]: validate the cog file is valid.
\b
    for detial help, check [cog create --help] or [cog validate --help]
    '''
    pass

entry_point.add_command(create_cog_command, name='create')
entry_point.add_command(validate_cog_command, name='validate')