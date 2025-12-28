#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

curl -X POST "http://localhost:9200/products/_bulk" \
  -H "Content-Type: application/json" \
  --data-binary @"$SCRIPT_DIR/data/products.json"
