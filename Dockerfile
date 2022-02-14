FROM osgeo/gdal:ubuntu-full-latest
RUN mkdir /data
VOLUME /data
COPY acma.py /usr/local/bin/
CMD acma.py
