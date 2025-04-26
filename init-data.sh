#!/bin/sh

cp --update=none "./conf/data/"* "./src/"
cp --recursive "./conf/data/media" "./src/"

uv run manage.py loaddata staff.json && \
uv run manage.py loaddata works.json && \
uv run manage.py loaddata reviews.json && \
uv run manage.py loaddata prices.json && \
uv run manage.py loaddata pricegroups.json && \
uv run manage.py loaddata contacts.json
