#!/bin/bash

echo "Checking zyre-gateway service......"
/bin/systemctl status zyre-gateway
echo; echo

echo "Checking csirtg-cef-zmq service......"
/bin/systemctl status csirtg-cef-zmq
echo; echo

echo "Checking csirtg-smrt service......"
/bin/systemctl status csirtg-smrt.service
echo; echo

echo "Checking bro processes......"
ps ax | grep bro
echo; echo

echo "Checking docker......"
/bin/docker ps
echo; echo

echo "Checking netstat ports......"
netstat -antp | egrep ":(22|1100|5670).*LISTEN"
echo; echo

echo "Checking gateway install......"
/bin/ls -laR /usr/local/gateway
echo; echo
