#!/usr/bin/env python3
from subprocess import run
run("curl https://web.acma.gov.au/rrl-updates/spectra_rrl.zip -o spectra_rrl.zip", shell=True)
run("ogr2ogr -overwrite spectra_rrl.gpkg spectra_rrl.vrt", shell=True)
run("ogr2ogr -update -lco OVERWRITE=YES -unsetFid spectra_rrl.gpkg spectra_rrl_query.vrt", shell=True)