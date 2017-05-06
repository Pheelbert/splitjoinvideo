== Examples ==

= Split from timestamp file and join
python pheelsplitjoin.py INPUT_VIDEO TIME_STAMPS OUTPUT_VIDEO

= Join from list of files
python pheeljoin.py INPUT_FILE_LIST OUTPUT_VIDEO

== Arguments ==
INPUT_VIDEO: The full length video that you wish to split and join (ex: downloaded using Twitch Leecher)

TIME_STAMPS: The list of pairs of timestamps of sections to be kept from the original video. (ex: examples/timestamp_example.txt, newlines between pairs are not necessary)

OUTPUT_VIDEO: Name you wish to call the output joined video. This also influences how the segments will be called. (ex: <name>_0.mp4, <name>_1.mp4 will be joined to create <name>.mp4)

INPUT_FILE_LIST: List of files you wish to join together. (ex: examples/file_list_example.txt)

== Dependencies ==
python 3.6.0: https://www.python.org/downloads/release/python-360/
ffmpeg N-85750-ga75ef15: https://ffmpeg.org/download.html

PS: You must add those in your environment variable 'Path'. (ex: C:\ffmpeg\bin, C:\Users\alexa\AppData\Local\Programs\Python\Python36)

== Output ==
Segments according to timestamps, indexed from 0 to n.
Joined video.