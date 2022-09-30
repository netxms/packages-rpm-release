#!/bin/bash

set -e

mock -r rocky+epel-8-$(arch) --spec SPECS/*.spec --sources SOURCES
cp /var/lib/mock/*/result/*.rpm /result/
