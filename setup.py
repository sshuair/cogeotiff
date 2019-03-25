#coding: --utf-8--
from setuptools import setup

# install requirements
inst_reqs = [
    'click', 'gdal'
]

# readme
with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='cogeotiff',
    version = '0.1.3',
    description = u'Cloud Optimized GeoTiff utility tools.',
    long_description = readme,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Scientific/Engineering :: GIS'],
    keywords='GeoTiff COG GDAL',
    author='sshuair',
    author_email='sshuair@gmail.com',
    url='https://github.com/sshuair/cogeotiff',
    packages = ['cogeotiff', 'cogeotiff.cli'],
    install_requires=inst_reqs,
    entry_points='''
        [console_scripts]
        cog=cogeotiff.cli.cli:entry_point
    '''
)
