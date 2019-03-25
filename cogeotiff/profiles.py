from collections import UserDict


class Profile(UserDict):
    defaults = {}

    def __init__(self, data={}, **kwargs):
        UserDict.__init__(self)
        initdata = self.defaults.copy()
        initdata.update(data)
        initdata.update(**kwargs)
        self.data.update(initdata)

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        #TODO: not good method, add kwargs
        if key == 'driver':
            self.data[key] = '-of {}'.format(value)
        elif key == 'tiled':
            self.data[key] = '-co TILED={}'.format('YES' if value else 'NO')
        elif key == 'block_size':
            self.data[key] = '-co BLOCKXSIZE={value} -co BLOCKYSIZE={value}'.format(value=value)
        elif key == 'copy_src_overviews':
            self.data[key] = '-co COPY_SRC_OVERVIEWS={}'.format('YES' if value else 'NO')
        elif key == 'nodata':
            self.data[key] = '-a_nodata {}'.format(value)
        elif key == 'compress':
            self.data[key] = '-co COMPRESS={}'.format(value)
        elif key == 'photometric':
            self.data[key] = '-co PHOTOMETRIC={}'.format(value)
        else:
            raise KeyError('not support key {key}'.format(key=key))


class RAWProfile(Profile):
    '''no compress GTiff'''
    
    defaults = {
        'driver': 'GTiff',
        'tiled': 'YES',
        'block_size': 256,
        'copy_src_overviews': True, 
        'nodata': 0,
    }


class JPEGProfile(Profile):
    defaults = {
        'driver': 'GTiff',
        'tiled': True,
        'block_size': 256,
        'copy_src_overviews': True, 
        'nodata': 0,
        'compress': 'JPEG',
        "photometric": "YCBCR",
    }


class WEBPProfile(Profile):
    """Tiled, pixel-interleaved, WEBP-compressed, 8-bit GTiff."""

    defaults = {
        "driver": "GTiff",
        "tiled": True,
        "block_size": 512,
        'copy_src_overviews': True, 
        'nodata': 0,
        "compress": "WEBP",
    }


class ZSTDProfile(Profile):
    """Tiled, pixel-interleaved, ZSTD-compressed GTiff.
    Note: ZSTD compression is available since gdal 2.3
    """

    defaults = {
        "driver": "GTiff",
        "tiled": True,
        "block_size": 512,
        'copy_src_overviews': True, 
        'nodata': 0,
        'dtype': 'Byte',
        "compress": "ZSTD",
    }


class LZWProfile(Profile):
    """Tiled, pixel-interleaved, LZW-compressed GTiff."""

    defaults = {
        "driver": "GTiff",
        "tiled": True,
        "block_size": 512,
        'copy_src_overviews': True, 
        'nodata': 0,
        "compress": "LZW",
    }


class DEFLATEProfile(Profile):
    """Tiled, pixel-interleaved, DEFLATE-compressed GTiff."""

    defaults = {
        "driver": "GTiff",
        "tiled": True,
        "block_size": 512,
        'copy_src_overviews': True, 
        'nodata': 0,
        "compress": "DEFLATE",
    }


class PACKBITSProfile(Profile):
    """Tiled, pixel-interleaved, PACKBITS-compressed GTiff."""

    defaults = {
        "driver": "GTiff",
        "tiled": True,
        "block_size": 512,
        'copy_src_overviews': True, 
        'nodata': 0,
        "compress": "PACKBITS",
    }


class COGProfiles(dict):
    def __init__(self):
        self.update({
            'JPEG': JPEGProfile(),
            'RAW': RAWProfile(),
            'DEFLATE': DEFLATEProfile(),
            'LZW': LZWProfile(),
            'WEBP': WEBPProfile(),
            'ZSTD': ZSTDProfile(),
            'PACKBITS': PACKBITSProfile()

        })

    def get(self, key):
        if key not in self.keys():
            raise KeyError('{} is not in COG profile'.format(key))
        
        return self[key].copy()

cog_profile = COGProfiles()
