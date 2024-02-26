#!/usr/bin/env bash
set -e
docker compose up --build --abort-on-container-exit --force-recreate -V --no-attach mongo
docker container cp test:/app/report.pdf ./report/report.pdf

#!/usr/bin/env bash
set -e
docker compose up --build --abort-on-container-exit --force-recreate -V --no-attach mongo
docker container cp test:/app/report.pdf ./report/report.pdf
