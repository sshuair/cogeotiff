## Cloud Optimized GeoTiff utility tools

## work in progress..

## Usage

### Python PAI
1. create cog file
```
from 
```
### Create cog file
- 可在python程序内部调用
- 可用命令行调用，参数如下
  - profile: 压缩方式
  - band
  - nodata：
  - overview-level
  - overview-resampling
  - co


- 可循环遍历所有文件夹下的文件
- 可转格式：
  - img
  - tiff
  - hdr

1. 

### Validate cog file
 

## Notice
- why not use `GDAL BuildOverviews` or `Rasterio` in script?
  Because for large file such as 100GB, it's take long time to generate overview and translate to tiled GeoTiff. There is no progress infomataion use `Rasterio` or `GDAL BuildOverviews` methods.
