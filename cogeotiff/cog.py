import os
from osgeo import gdal
import subprocess
from .profiles import cog_profile
from .utils import check_overview, get_max_overview


def create_cog(
    src_path,
    dst_path, 
    overview_resampling='nearest',
    overview_level=None,
    nodata=0,
    block_size=256,
    compress='raw',
    **kwargs):
    '''create cog file from a specific file(tiff img hdr...)
    
    Arguments:
        src_path {string} -- source file path
        dst_path {string} -- target file path
    
    Keyword Arguments:
        overview_resampling {str} -- resampling method for create pyramid (default: 'nearest')
        overview_level {int} -- levels to build (default: {None})
        nodata {float} -- Assign a specified nodata value to output bands (default: 0)
        block_size {int} -- tiled size (default: 256)
        compress {str} -- compress method: JPEG,RAW,DEFLATE,LZW,WEBP,ZSTD,PACKBITS (default: 'raw')
    '''
    dataset = gdal.Open(src_path)

    # overview level:
    if not overview_level:
        nlevel = get_max_overview(src_path)
    overview_list = [2 ** j for j in range(1, nlevel + 1)]
    overview_list = ' '.join([str(x) for x in overview_list])
    
    # check overview extis or not, if overview exits, then skip create overview
    if not check_overview(dataset):
        print('++++creating overview++++')
        overview_command = ' '.join(['gdaladdo', '-ro', '-r', overview_resampling, src_path, overview_list ])
        addo_result = subprocess.run(overview_command, shell=True, check=True)
    else:
        print('++++overview already exits, skip create overview++++')

    # translate the file to tiled tif
    print('\n++++generate cloud optimized geotiff++++')
    out_profile = cog_profile.get(compress)
    out_profile.update({'nodata':nodata, 'block_size':block_size})
    out_profile = dict(out_profile).values()
    translate_command = ' '.join(['gdal_translate', ' '.join(out_profile), src_path, dst_path])
    subprocess.run(translate_command, shell=True)

    # remove the external ovr file
    # os.remove(src_path+'.ovr')

if __name__ == "__main__":
    src_path = '/Volumes/sshuair/imagery-path/cog-test/test_7.tif'
    dest_path = '/Volumes/sshuair/imagery-path/cog-test/cache/test_7.tiff.cog'
    create_cog(src_path, dest_path, compress='jpeg')