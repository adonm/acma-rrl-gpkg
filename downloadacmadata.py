#!/usr/bin/env python3
import os
from subprocess import run
if not os.path.exists("spectra_rrl.zip"):
    run("curl -k https://web.acma.gov.au/rrl-updates/spectra_rrl.zip -o spectra_rrl.zip", shell=True)
if not os.path.exists("spectra_rrl.gpkg"):
    run("ogr2ogr -overwrite spectra_rrl.gpkg spectra_rrl.vrt client licence device_details site", shell=True)
if not os.path.exists("spectra_rrl_query.gpkg"):
    run("ogr2ogr -overwrite -unsetFid spectra_rrl_query.gpkg spectra_rrl_query.vrt", shell=True)