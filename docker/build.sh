#!/bin/bash

set -e

mkdir -p /result/epel /result/fedora

rm -rf /var/lib/mock
mock -r rocky+epel-8-$(arch) --spec SPECS/*.spec --sources SOURCES
cp /var/lib/mock/*/result/*.rpm /result/epel/

rm -rf /var/lib/mock
mock -r fedora-37-$(arch) --spec SPECS/*.spec --sources SOURCES
cp /var/lib/mock/*/result/*.rpm /result/fedora/
