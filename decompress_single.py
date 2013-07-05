#!/usr/bin/python
#
import mmh3
import sys
import os
import ast
import time

exitFlag = 0
match = 0
    



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

while (match == 0):
  rands = str(bytearray(os.urandom(size)))
  h1 = mmh3.hash64(rands)
  if (h1 == ohash):
    solution = rands
    match = 1


if 'solution' in locals():
  answer = str(solution)
  print 'the answer is'
  print answer



#write out comp file
#except:
#  sys.stderr.write("no file specified, or error")
#  sys.stderr.write("\n")
