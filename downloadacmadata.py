#!/usr/bin/env python3
from subprocess import run
run("curl -k https://web.acma.gov.au/rrl-updates/spectra_rrl.zip -o spectra_rrl.zip", shell=True)
run("ogr2ogr -overwrite spectra_rrl.gpkg spectra_rrl.vrt client licence device_details site", shell=True)
run("ogr2ogr -overwrite -unsetFid spectra_rrl_query.gpkg spectra_rrl_query.vrt", shell=True)