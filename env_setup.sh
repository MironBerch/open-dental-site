#!/bin/sh

ENV_FILE=".env"

if [ -f "$ENV_FILE" ]; then
    echo "Загрузка переменных среды из $(realpath "$ENV_FILE")"
    while IFS= read -r line; do
        if [[ ! "$line" =~ ^[[:space:]]*# && ! -z "$line" ]]; then
        key=$(echo "$line" | awk -F '=' '{print $1}')
        value=$(echo "$line" | awk -F '=' '{print $2}')
        export "$key"="$value"
        echo "Set $key"
        fi
    done < "$ENV_FILE"
    echo "Переменные среды, заданны из $(realpath "$ENV_FILE")."
else
    echo "Файл .env не найден в директории - open-dental-site/"
fi
