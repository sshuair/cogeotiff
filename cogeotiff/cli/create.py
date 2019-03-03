import click
from cogeotiff.cog import create_cog

@click.command()
@click.argument('src_path')
@click.argument('dst_path')
@click.option('--overview-resampling', default='nearest')
@click.option('--overview-level', type=int, default=None)
@click.option('--nodata', type=int, default=None)
@click.option('--block-size', type=int, default=512)
@click.option('--compress', type=str, default='raw')
def create_cog_command(
    src_path,
    dst_path, 
    overview_resampling, 
    overview_level, 
    nodata,
    block_size,
    compress
):
    create_cog(
    src_path,
    dst_path, 
    overview_resampling=overview_resampling, 
    overview_level=overview_level, 
    nodata=nodata,
    block_size=block_size,
    compress=compress)