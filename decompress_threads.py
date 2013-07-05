#!/usr/bin/python
#
import mmh3
import sys
import os
import ast
import threading
import multiprocessing
import time

exitFlag = 0
match = 0
printed = 0
found_by = ''

class myThread (threading.Thread):
  def __init__(self, threadID, name, counter, size, ohash):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.counter = counter
    self.size = size
    self.ohash = ohash
  def run(self):
    print "Starting " + self.name
    find_match(self.name, self.size, self.ohash)
    print "Exiting " + self.name

def find_match(threadName, size, ohash):
  global match
  global solution
  global found_by
  while (match == 0):
    rands = str(bytearray(os.urandom(size)))
    h1 = mmh3.hash64(rands)
    if (h1 == ohash):
      solution = rands
      match = 1
      found_by = threadName
    



#try:
# open file
filename = sys.argv[1]
sys.stderr.write("the input file name: ")
sys.stderr.write(filename)
sys.stderr.write("\n")
filenameParts = filename.split('.')
outfilename = filenameParts[0]+'.'+filenameParts[1]
f = open(filename, "r")
contents = f.read()
f.close()
cstr = str(contents)
parts = cstr.split(';')
hashstr = parts[0]
sizestr = parts[1]
size = int(sizestr)
ohash = ast.literal_eval(hashstr)

threads = []

cores = multiprocessing.cpu_count()

for i in range(1,cores):
  istr = str(i)
  thread = myThread(i, "Thread-"+istr, i, size, ohash)
  thread.start()
  threads.append(thread)

for t in threads:
  t.join()
  if (printed == 0):
    if 'solution' in globals():
      answer = str(solution)
      print 'the answer is'
      print answer
      print 'found by: '+found_by
      printed = 1





#write out comp file
#except:
#  sys.stderr.write("no file specified, or error")
#  sys.stderr.write("\n")
