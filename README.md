# acma-rrl-gpkg
Convert the acma data dumped daily from https://www.acma.gov.au/radiocomms-licence-data into a geopackage with some convenience views.

## Requirements
Local docker installation

## Usage
Files will be saved to `/var/lib/docker/volumes/data/_data` 

```bash
docker build . -t acma
docker run -v data:/data acma
```
