#!/bin/bash
DIR="$(cd $(dirname ${BASH_SOURCE[0]})/.. && pwd)"
FILES="$(ls ${DIR} | grep '\.py') README.md LICENSE animations"

set -ex
tar -zcf dc26-fur-scripts.tar.gz -C ${DIR} ${FILES}
