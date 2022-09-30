#!/bin/bash

set -e

mock -r rocky+epel-9-$(arch) --spec SPECS/*.spec --sources SOURCES
cp /var/lib/mock/*/result/*.rpm /result/
