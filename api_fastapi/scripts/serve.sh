#!/bin/bash

APP_DIR=$(readlink -f "$0" | sed "s/scripts\/format.sh/api/")

uvicorn --reload --app-dir "$APP_DIR" --port 3000 main:app
