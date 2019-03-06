import click
from cogeotiff.cog import create_cog

@click.command()
@click.argument('src_path')
@click.argument('dst_path')
@click.option('--overview-resampling', 
             default='nearest',
             help='resampling method for create pyramiddefault: nearest'
             )
@click.option('--overview-level', 
             type=int, 
             default=None,
             help='levels to build'
             )
@click.option('--nodata', 
             type=int, 
             default=None,
             help='Assign a specified nodata value to output bands. default: 0'
             )
@click.option('--block-size', 
             type=int, 
             default=512,
             help='tiled size, default: 512'
             )
@click.option('--compress', 
             type=str, 
             default='raw',
             help='compress method,default: raw')
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