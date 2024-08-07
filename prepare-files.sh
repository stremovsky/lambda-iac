#!/bin/bash

mkdir -p .files
cd src
cp -r lambda_create_item.py lambda_function.py
zip lambda_create_item.zip lambda_function.py
cp -r lambda_get_item.py lambda_function.py
zip lambda_get_item.zip lambda_function.py
cp -r lambda_delete_item.py lambda_function.py
zip lambda_delete_item.zip lambda_function.py
mv *.zip ../.files/
