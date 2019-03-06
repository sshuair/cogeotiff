from cogeotiff.cog import create_cog

def test_create_cog():
    src_path = '/Users/sshuair/geohey-code/cog/tests/fixtures/multi-band.tif'
    dest_path = '/Users/sshuair/geohey-code/cog/tests/fixtures/multi-band.tif.cog'
    create_cog(src_path, dest_path)

test_create_cog()