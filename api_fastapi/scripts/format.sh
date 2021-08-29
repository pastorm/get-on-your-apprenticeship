#!/bin/bash

APP_DIR=$(readlink -f "$0" | sed "s/scripts\/format.sh/api/")

black "$APP_DIR"
