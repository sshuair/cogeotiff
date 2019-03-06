## Cloud Optimized GeoTiff utility tools


## Requirements
- click
- gdal

## Install
- pypi: `pip install cogeotiff`
- source code: `python setup.py install`

## Usage

### Python PAI
1. create cog file
example:
```python
from cogeotiff.cog import create_cog
src_path = '~/path_to_image/test.tif'
dest_path = '~/path_to_save/test.tiff.cog'
create_cog(src_path, dest_path, compress='jpeg')
```

2. validate cog file
```python
from cogeotiff.validate_cogeotiff import validate_cog
cog_path = '~/path_to_cog.tif.cog'
result = validate_cog(cog_path)
```

### Command tools
1. create cog file
```bash
Usage: cog create [OPTIONS] SRC_PATH DST_PATH

Options:
  --overview-resampling TEXT  resampling method for create pyramiddefault:
                              nearest
  --overview-level INTEGER    levels to build
  --nodata INTEGER            Assign a specified nodata value to output bands.
                              default: 0
  --block-size INTEGER        tiled size, default: 512
  --compress TEXT             compress method,default: raw
  --help                      Show this message and exit.
```

2. validate cog file
```bash
Usage: cog create [OPTIONS] COG_PATH 
```
 
## Q&A
- Q: why not use `GDAL BuildOverviews` or `Rasterio` in script?
- A: Because for large file such as 100GB, it's take long time to generate overview and translate to tiled GeoTiff. There is no progress infomataion use `Rasterio` or `GDAL BuildOverviews` methods.
- Q: why not use [rio-cogeo](https://github.com/cogeotiff/rio-cogeo)?
- A: Cause it use `rasterio MemoryFile()`, when the file is too large, it will cause insufficient memory.
