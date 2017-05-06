#!/usr/bin/python
import sys
from subprocess import call

if not len(sys.argv) == 3:
  print('python pheeljoin.py INPUT_FILE_LIST OUTPUT_VIDEO')
  exit()

input_file_list = sys.argv[1]
output_file = sys.argv[2]

# Join clips
# print('ffmpeg', '-f', 'concat', '-i', input_file_list, output_file)
call(['ffmpeg', '-f', 'concat', '-i', input_file_list, output_file])