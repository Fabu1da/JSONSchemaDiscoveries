#!/usr/bin/env python3
import argparse
from datetime import datetime
import json
import random

import pymongo
import requests

datetime_format: str = r'%Y-%m-%dT%H:%M:%S.%fZ'


def mongoimport(client: pymongo.MongoClient, databaseName: str, collectionName: str) -> None:
    db = client[databaseName]
    collection = db[collectionName]

    with open(f"data/{collectionName}.json") as f:
        for line in f.readlines():
            try:
                collection.insert_one(json.loads(line))
            except pymongo.errors.DuplicateKeyError:
                pass


def register(email: str, username: str, password: str) -> None:
    json_data = {
        'email': email,
        'username': username,
        'password': password,
    }

    response = requests.post('http://localhost:3000/api/register', json=json_data)
    response.raise_for_status()


def login(email: str, password: str) -> str:
    json_data = {
        'email': email,
        'password': password,
    }

    response = requests.post('http://localhost:3000/api/login', json=json_data)
    response.raise_for_status()

    result: dict = response.json()
    return result['token']


def create_rawschema(token: str, databaseName: str, collectionName: str) -> str:
    headers = {
        'Authorization': 'Bearer ' + token, 
    }

    json_data = {
        'authentication': {
            'authMechanism': 'SCRAM-SHA-1',
            'authDatabase': 'admin',
            'userName': 'mongoadmin',
            'password': 'secret',
        },
        'port': '27017',
        'address': 'mongo',
        'databaseName': databaseName,
        'collectionName': collectionName,
    }

    response = requests.post(
        'http://localhost:3000/api/batch/rawschema/steps/all',
        headers=headers,
        json=json_data,
    )
    response.raise_for_status()

    result: dict = response.json()
    return result['batchId']


def get_batch(token: str, batchId: str) -> dict:
    headers = {
        'Authorization': 'Bearer ' + token,
    }

    response = requests.get(f'http://localhost:3000/api/batch/{batchId}', headers=headers)
    response.raise_for_status()

    result: dict = response.json()
    return result


def view_schema(token: str, schema_id: str) -> dict:
    headers = {
        'Authorization': 'Bearer ' + token,
    }

    response = requests.get(
        f'http://localhost:3000/api/batch/jsonschema/generate/{schema_id}',
        headers=headers,
    )

    response.raise_for_status()
    return response.json()


def main(args: argparse.Namespace) -> None:
    databaseName: str = 'jsonschemadiscovery'

    client = pymongo.MongoClient(
        host='mongo',
        port=27017,
        username='mongoadmin',
        password='secret',
    )

    for collectionName in args.collections:
        mongoimport(client, databaseName, collectionName)

    client.close()

    randomId: str = str(random.randint(0, 2**32))
    email: str = f"info{randomId}@example.com"
    username: str = f"johndoe{randomId}"
    password: str = "Secret123"

    register(email, username, password)
    token: str = login(email, password)
    print()

    for collectionName in args.collections:
        print("collectionName:", collectionName)
        batchId: str = create_rawschema(token, databaseName, collectionName)
        print("batchId:", batchId)
        batch: dict

        while (batch := get_batch(token, batchId))['status'] != "DONE":
            print("status:", batch['status'])

        #print(json.dumps(batch, indent=2))

        print("collectionCount:", batch['collectionCount'])
        print("uniqueUnorderedCount:", batch['uniqueUnorderedCount'])
        print("uniqueOrderedCount:", batch['uniqueOrderedCount'])
        print()

        startDate = datetime.strptime(batch['startDate'], datetime_format)
        extractionDate = datetime.strptime(batch['extractionDate'], datetime_format)
        unorderedAggregationDate = datetime.strptime(batch['unorderedAggregationDate'], datetime_format)
        orderedAggregationDate = datetime.strptime(batch['orderedAggregationDate'], datetime_format)
        unionDate = datetime.strptime(batch['unionDate'], datetime_format)
        endDate = datetime.strptime(batch['endDate'], datetime_format)

        print("step 1:", extractionDate - startDate)
        print("step 2.1:", unorderedAggregationDate - extractionDate)
        print("step 2.2:", orderedAggregationDate - unorderedAggregationDate)
        print("step 3:", unionDate - orderedAggregationDate)
        print("step 4:", endDate - unionDate)
        print("total:", endDate - startDate)
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("collections", type=str, nargs="*", default=["firenze_checkins", "firenze_venues"])
    args = parser.parse_args()
    main(args)
