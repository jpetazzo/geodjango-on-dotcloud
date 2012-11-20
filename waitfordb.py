#!/usr/bin/env python
import json
import socket
import time

with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

host = env['DOTCLOUD_DB_SQL_HOST']
port = int(env['DOTCLOUD_DB_SQL_PORT'])

deadline = time.time() + 90

while time.time() < deadline:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.connect((host, port))
    break
  except:
    print 'Could not connect to the database; retrying.'
    time.sleep(1)
else:
  print 'Giving up.'
  print 'Either the platform is really slow today, or something is wrong.'
  exit(1)

