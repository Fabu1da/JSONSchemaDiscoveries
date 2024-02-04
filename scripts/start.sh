#!/usr/bin/env bash
set -m

npm run start &

./scripts/waitport.sh localhost 3000
./scripts/waitport.sh mongo 27017
sleep 1

python3 scripts/automation.py

wait
