from osgeo import gdal

def get_max_overview(src_path, block_size=512):
    image = gdal.Open(src_path)
    width = image.RasterXSize
    height = image.RasterYSize

    nlevel = 0
    overview = 1

    while min(width // overview, height // overview) > block_size:
        overview *= 2
        nlevel += 1

    return nlevel


def check_overview(ds):
    '''check dataset overview exit or not.
     If overview exit (internel or extrial), return True, else False.
    
    Arguments:
        ds {gdal.Dataset} -- opened gdal raster dataset
    
    Returns:
        Boolen -- True for overview exit, False for overview not exit.
    '''

    main_band = ds.GetRasterBand(1)
    ovr_count = main_band.GetOverviewCount()
    if ovr_count == 0:
        return False
    else:
        return True