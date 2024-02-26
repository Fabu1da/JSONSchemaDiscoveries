#!/usr/bin/env bash
set -e
docker compose build
docker compose up --abort-on-container-exit --force-recreate -V --no-attach mongo
docker cp node:/app/report.csv "$(pwd)"/report/report.csv
docker build -t latex report
docker run --mount type=bind,source="$(pwd)"/report,target=/report latex
