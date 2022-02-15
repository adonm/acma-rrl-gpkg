# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFolderDestination)
from qgis import processing
from subprocess import run, check_output
import os
from zipfile import ZipFile
from pathlib import Path


class ImportACMAData(QgsProcessingAlgorithm):
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return ImportACMAData()

    def name(self):
        return 'importacmadata'

    def displayName(self):
        return self.tr('Import ACMA Data')

    def group(self):
        return self.tr('My Scripts')

    def groupId(self):
        return 'myscripts'

    def shortHelpString(self):
        return self.tr("Downloads ACMA data and sets up a queryable spatialite database")

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFolderDestination(
                self.OUTPUT,
                self.tr('Output folder')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        os.chdir(parameters["OUTPUT"])
        run("curl https://web.acma.gov.au/rrl-updates/spectra_rrl.zip -o spectra_rrl.zip", shell=True)
        ZipFile("spectra_rrl.zip").extractall()
        datadir = Path(".")
        for csv in datadir.glob("*.csv"):
            if str(csv).find("text_block") > -1:
                csv.unlink()
                continue
            run(["ogr2ogr", "-update", "-overwrite", "-a_srs", "EPSG:4326", "-oo", "AUTODETECT_TYPE=YES", "-oo", "AUTODETECT_WIDTH=YES", "-oo", "AUTODETECT_SIZE_LIMIT=0", "-oo", "X_POSSIBLE_NAMES=LON*", "-oo", "Y_POSSIBLE_NAMES=LAT*", "-oo", "Z_POSSIBLE_NAMES=ELEV*", "acma_rrl.gpkg", csv])
            csv.unlink()
        # Setup materialised view for fast querying of relevant data (constrained to specific entities by ABN)
        run(["ogr2ogr", "-update", "-overwrite", "acma_rrl.gpkg", "-sql", """
            select * from (select * from device_details inner join licence on device_details.LICENCE_NO = licence.LICENCE_NO) device_licence 
            inner join site on site.SITE_ID = device_licence.SITE_ID 
            inner join client on client.CLIENT_NO = device_licence.CLIENT_NO 
            where ABN in (91724684688,39563851304,38052249024,55028468715)
        """, "-nln", "licence_detail", "acma_rrl.gpkg"])
        return {self.OUTPUT: parameters["OUTPUT"]}