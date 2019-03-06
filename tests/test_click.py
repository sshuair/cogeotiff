import click

@click.command()
@click.argument('src_path')
@click.argument('dst_path')
@click.option('--overview-resample', default='nearest')
@click.option('--overview-level', type=int, default=None)
@click.option('--nodata', type=int, default=None)
@click.option('--block-size', type=int, default=512)
@click.option('--compress', type=str, default=None)
def create_cog_command(
    src_path,
    dst_path, 
    overview_resampling, 
    overview_level, 
    nodata,
    block_size,
    compress
):
    print(123)