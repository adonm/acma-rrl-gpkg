# acma-rrl-gpkg
Convert the acma data dumped daily from https://www.acma.gov.au/radiocomms-licence-data into a geopackage with some convenience views.

## Requirements
Python3 and local ogr2ogr binary (The [GDAL Docker Images](https://github.com/OSGeo/gdal/tree/master/docker) have both installed by default)

## Usage
Files will be saved to the current directory

```bash
git clone https://github.com/adonm/acma-rrl-gpkg.git
cd acma-rrl-gpkg
./downloadacmadata.py
```
