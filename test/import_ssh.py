#!/usr/bin/env python
import os
import anydbm
from cjson import encode as dumps, decode as loads
import requests
import glob
import subprocess
import sys

def chunk(it, slice=50):
    """Generate sublists from an iterator
    >>> list(chunk(iter(range(10)),11))
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    >>> list(chunk(iter(range(10)),9))
    [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9]]
    >>> list(chunk(iter(range(10)),5))
    [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    >>> list(chunk(iter(range(10)),3))
    [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    >>> list(chunk(iter(range(10)),1))
    [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    """

    assert(slice > 0)
    a=[]

    for x in it:
        if len(a) >= slice :
            yield a
            a=[]
        a.append(x)

    if a:
        yield a

class Seen:
    def __init__(self, filename):
        self.filename = filename

    def has_seen(self, key):
        d = anydbm.open(self.filename, 'c')
        res = str(key) in d
        d.close()
        return res

    def mark_seen(self, key):
        d = anydbm.open(self.filename, 'c')
        d[str(key)] = '1'
        d.close()

    def remove(self, key):
        d = anydbm.open(self.filename, 'c')
        del d[str(key)]
        d.close()

def fix_line(line):
    try :
        rec = loads(line)
        rec['time'] = rec['time'][:len("2017-02-07T19:11:04")]
        rec['day'] = rec['time'][:rec['time'].index("T")]
        return dumps(rec)
    except:
        return


TABLE='sshauth'
ENDPOINT = 'http://localhost:8123'

#done = Seen("ssh_imported.clickhouse")
def do_import(f):
    query="INSERT INTO {} FORMAT JSONEachRow".format(TABLE)
    #data = os.popen("zcat {}".format(f))
    data = os.popen("cat {}".format(f))
    print f,
    for i, block in enumerate(chunk(data, 50000)):
        #if len(block) != 50000:
        #    return
        block_id = '{}_{}'.format(f, i)
        #if done.has_seen(block_id):
        #    sys.stdout.write("#")
        #    sys.stdout.flush()
        #    continue
        fixed = [fix_line(line) for line in block]
        fixed = [d for d in fixed if d]
        blob = "\n".join(fixed) + "\n"
        r = requests.post(ENDPOINT, params=dict(query=query,input_format_skip_unknown_fields="1"), data=blob)
        r.raise_for_status()
        #done.mark_seen(block_id)
        sys.stdout.write("#")
        sys.stdout.flush()
    print

do_import("ssh.log.gz")

