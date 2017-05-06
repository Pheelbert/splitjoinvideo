#!/usr/bin/python
import sys
from subprocess import call
import tempfile
import os

if not len(sys.argv) == 4:
  print('python pheelsplitjoin.py INPUT_VIDEO TIME_STAMPS OUTPUT_VIDEO')
  exit()

input_file = sys.argv[1]
timestamp_file = sys.argv[2]
output_file = sys.argv[3]

# Split output filename from extension
output_filename = output_file.split(".")[0]
output_extension = output_file.split(".")[-1]

# Read timestamps from the given file
timestamps = []
with open(timestamp_file) as file:
    for line in file:
      if (len(line) > 1): # ignore newlines-only
        timestamps.append(line.strip()[:8]) # 8 is length of timestamp in format 00:00:00


# Create clips and append to file list
split_filepath = output_filename + '_list.txt'
split_list = open(split_filepath, 'w')
index = 0
for i in range(0, len(timestamps) - 1, 2):
  t1 = timestamps[i]
  t2 = timestamps[i + 1]
  output_file_indexed = output_filename + '_' + str(index) + '.' +  output_extension
  index = index + 1

  split_list.write('file \'' + output_file_indexed + '\'')
  if not i == len(timestamps) - 2:
    split_list.write('\n')

  # print('ffmpeg', '-i', input_file, '-c', 'copy', '-ss', t1, '-to', t2, '-map', '0', output_file_indexed)
  if os.path.isfile(output_file_indexed):
    print('Clip ' + output_file_indexed + ' already exists, skipped.')
    continue
  else:
    print('Creating clip ' + output_file_indexed + '...')

  call(['ffmpeg', '-i', input_file, '-c', 'copy', '-ss', t1, '-to', t2, '-map', '0', output_file_indexed])

# Join clips
# print('ffmpeg', '-f', 'concat', '-i', split_filepath, output_file)
split_list.close()
call(['ffmpeg', '-f', 'concat', '-i', split_filepath, output_file])
# os.remove(split_filepath)