#!/bin/sh

cp -u "./conf/data/"* "./src/"
cp --recursive "./conf/data/media" "./src/"

cd src/

uv run manage.py loaddata staff.json && \
    uv run manage.py loaddata works.json && \
    uv run manage.py loaddata reviews.json && \
    uv run manage.py loaddata pricegroups.json && \
    uv run manage.py loaddata prices.json && \
    uv run manage.py loaddata contacts.json && \
    uv run manage.py loaddata servicegroups.json && \
    uv run manage.py loaddata services.json && \
    uv run manage.py loaddata about.json && \
    uv run manage.py loaddata policy.json

rm staff.json && \
    rm works.json && \
    rm reviews.json && \
    rm pricegroups.json && \
    rm prices.json && \
    rm contacts.json && \
    rm servicegroups.json && \
    rm services.json && \
    rm about.json && \
    rm policy.json

cd ..
