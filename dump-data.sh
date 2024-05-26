#!/bin/sh

while getopts "d:" opt; do
    case ${opt} in
        d )
            FOLDER_NAME=$OPTARG
            ;;
        \? )
            echo "Usage: cmd [-f folder_name]"
            exit 1
            ;;
    esac
done

mkdir "./conf/data/$FOLDER_NAME"

cp --recursive "./src/media" "./conf/data/$FOLDER_NAME/media"

cd src/

uv run manage.py dumpdata clinic.staff --indent 4 > ../conf/data/$FOLDER_NAME/staff.json && \
    uv run manage.py dumpdata clinic.work --indent 4 > ../conf/data/$FOLDER_NAME/works.json && \
    uv run manage.py dumpdata clinic.review --indent 4 > ../conf/data/$FOLDER_NAME/reviews.json && \
    uv run manage.py dumpdata clinic.pricegroup --indent 4 > ../conf/data/$FOLDER_NAME/pricegroups.json && \
    uv run manage.py dumpdata clinic.price --indent 4 > ../conf/data/$FOLDER_NAME/prices.json && \
    uv run manage.py dumpdata clinic.contact --indent 4 > ../conf/data/$FOLDER_NAME/contacts.json && \
    uv run manage.py dumpdata clinic.servicegroup --indent 4 > ../conf/data/$FOLDER_NAME/servicegroups.json && \
    uv run manage.py dumpdata clinic.service --indent 4 > ../conf/data/$FOLDER_NAME/services.json && \
    uv run manage.py dumpdata clinic.about --indent 4 > ../conf/data/$FOLDER_NAME/about.json && \
    uv run manage.py dumpdata clinic.policy --indent 4 > ../conf/data/$FOLDER_NAME/policy.json && \
    uv run manage.py dumpdata clinic.photo --indent 4 > ../conf/data/$FOLDER_NAME/photos.json

cd ..
