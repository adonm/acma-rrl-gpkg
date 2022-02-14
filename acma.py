#!/usr/bin/env python3
from subprocess import run
from pathlib import Path
import os
os.chdir("/data")
run("curl https://web.acma.gov.au/rrl-updates/spectra_rrl.zip -o spectra_rrl.zip", shell=True)
run("unzip -o spectra_rrl.zip", shell=True)
datadir = Path(".")
for csv in datadir.glob("*.csv"):
    run(["ls", "-lh", csv])
    if str(csv).find("text_block") > -1:
        csv.unlink()
        continue
    run(["ogr2ogr", "-update", "-overwrite", "-a_srs", "EPSG:4326", "-oo", "X_POSSIBLE_NAMES=LON*", "-oo", "Y_POSSIBLE_NAMES=LAT*", "-oo", "Z_POSSIBLE_NAMES=ELEV*", "acma_rrl.gpkg", csv])
    csv.unlink()
