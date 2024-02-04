#!/usr/bin/env bash

for i in {1..30}; do
  if nc -z -w 1 "$1" "$2"; then
    echo
    exit 0
  fi

  echo -n .
  sleep 1
done

echo Timeout
exit 1
