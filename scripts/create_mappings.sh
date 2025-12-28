#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

curl -X PUT "http://localhost:9200/products" \
  -H "Content-Type: application/json" \
  -d @"$SCRIPT_DIR/mappings/products.json"
