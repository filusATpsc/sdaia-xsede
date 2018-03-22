#!/usr/bin/env python3
from __future__ import print_function
import sys
import zmq
import time
import json
import signal
from datetime import datetime


host='localhost'

file = open("/tmp/ssh.txt","a+",0)

def handle_intr(signal, frame):
    print('Ctrl+C caught, exiting...')
    sys.exit(0)

signal.signal(signal.SIGINT, handle_intr)
context = zmq.Context()

def connect(topics):
    # Socket to talk to server
    socket = context.socket(zmq.SUB)
    socket.connect ("tcp://%s:%s" % (host, 14000))
    for topic in topics:
        socket.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))
    return socket


def sub(topics):
    control = context.socket(zmq.DEALER)
    control.connect("tcp://%s:%s" % (host, 14001))
    for topic in topics:
        control.send_multipart([b"SUB", topic.encode('utf-8')]) #needs to be done periodically

    #TODO: have gateway send a response to SUB, if no response, recreate sockets.

def show_ssh(topic, who, messagedata):
    prefix = "{}:".format(who)
    rec = json.loads(messagedata)
    out = "{description} {indicator} -> {dest}:{dest_portlist}".format(**rec)
    if 'additional_data' in rec and 'duser' in rec['additional_data']:
        if 'fingerprint' in rec['additional_data']:
            rec['additional_data']['password'] = rec['additional_data']['fingerprint']
        if 'password' in rec['additional_data']:
            out += " {duser}:{password} using {client_version}".format(**rec['additional_data'])
    logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(logtime, prefix, out)
    # this is confusing: time that event was logged, not when it occured
    file.write(logtime+" "+prefix+" "+out+"\n")

def main():
    topics = sys.argv[1:]

    socket = connect(topics)

    last_sub = 0
    while True:
        if time.time() - last_sub > 10:
            sub(topics)
            last_sub = time.time()

        if socket.poll(1000):
            topic, who, messagedata = socket.recv_multipart()
            show_ssh(topic, who, messagedata)

if __name__ == "__main__":
    main()
