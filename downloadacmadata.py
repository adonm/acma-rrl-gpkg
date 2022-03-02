#!/usr/bin/env python3
import os
from subprocess import run
if not os.path.exists("spectra_rrl.zip"):
    run("curl -k https://web.acma.gov.au/rrl-updates/spectra_rrl.zip -o spectra_rrl.zip", shell=True)
if not os.path.exists("spectra_rrl.gpkg"):
    run("ogr2ogr spectra_rrl.gpkg spectra_rrl.vrt client licence device_details site", shell=True)
if not os.path.exists("spectra_rrl_query.gpkg"):
    # The order here is important as layers depend on previous calcs
    run("ogr2ogr -unsetFid spectra_rrl_query.gpkg spectra_rrl_query.vrt aggregated_sites", shell=True)
    run("ogr2ogr -update -unsetFid spectra_rrl_query.gpkg spectra_rrl_query.vrt network_sites", shell=True)
    run("ogr2ogr -update -unsetFid spectra_rrl_query.gpkg spectra_rrl_query.vrt network_coverage", shell=True)
run("ogr2ogr networks.csv spectra_rrl_query.gpkg network_coverage")
run("ogr2ogr sites.csv spectra_rrl_query.gpkg network_sites")