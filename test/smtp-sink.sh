#!/bin/sh

# change to interface IP to bind to
INT='127.0.0.1'

# postfix smtp-sink test
smtp-sink -u root -d %d.%H.%M.%S ${INT}:25 10
