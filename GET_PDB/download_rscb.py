import os
import urllib
import time
import socket

socket.setdefaulttimeout(300)

file = open("../list/pdb_entry_type.txt", "r")
data_table = file.readlines()
file.close()
index = 0
for line in data_table:
  data = line.split()
  print data[0], index
  url = "https://files.rcsb.org/download/" + data[0] + ".pdb"
    if os.path.exists(data[1]):
    paths = "./" + data[1] + "/" + data[2]
    if os.path.exists(paths):
      pass
    else:
      os.mkdir(paths)
  else:
    paths = "./" + data[1]
    os.mkdir(paths)
    paths = "./" + data[1] + "/" + data[2]
    os.mkdir(paths)
  paths = paths + "/" + data[0] + ".pdb"
  if os.path.exists(paths):
    continue
  check_try = 1
  while check_try == 1:
    try:
      data = urllib.urlopen(url).read()
      check_try = 0
    except:
      time.sleep(60)
      print data[0]
      check_try = 1
  file_pdb = open(paths,"wb")
  file_pdb.write(data)
  file_pdb.close()
  index = index + 1
