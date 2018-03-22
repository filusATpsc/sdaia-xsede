#!/bin/bash

set -e

echo 'running ansible...'



ansible-playbook -vv -i "localhost," -c local ./site.yml
