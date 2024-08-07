#!/bin/bash

URL=`terraform output -raw api_url`
echo "API gateway url: $URL"
echo "Creating new item"
curl -X POST -H "Content-Type: application/json" -d '{"id":"key1","data":"Sample item data"}' $URL
echo
echo "Get item"
curl -X GET $URL?id=key1
echo
echo "Delete item"
curl -X DELETE $URL?id=key1
echo
