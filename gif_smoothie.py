import urllib, sys, os
import requests
from bs4 import BeautifulSoup, SoupStrainer
from moviepy.editor import *

'''

The following is a Python script to download a GIF posted on Twitter.

It does so by grabbing a Twitter page with urllib, isolating an MP4 
movie URL with BeautifulSoup, downloading the MP4 with Requests,
converting it to a GIF with MoviePy, and removing the movie file with os.

'''

# Ask for a file name, use 'input' function prompt only if user has Python 3
if sys.version_info[0] < 3:
    gif_name = raw_input("What do you want to name your gif?: ")
else:
    gif_name = input("What do you want to name your gif? : ")

# Open and grab the HTML of the twitter URL
twitterURL = sys.argv[1]
f = urllib.urlopen(twitterURL)
s = f.read()
f.close()

# Use BeautifulSoup to get the video source URL and the video's filename
soup = BeautifulSoup(s, 'html.parser')
video_url = soup.find('source').get('video-src')
video_name = video_url.split('/')[-1]

# Use Requests to download the video and temporarily save it by its filename
r=requests.get(video_url)
print "****Connected****"
f=open(video_name,'wb');
print ''
print "WHHHIRRRRR..... blending your gif!!!"
for chunk in r.iter_content(chunk_size=255): 
    if chunk: # filter out keep-alive new chunks
        f.write(chunk)
f.close()

# Open the video and use MoviePy to convert it to a GIF
clip = VideoFileClip(video_name)
clip.write_gif(gif_name+'.gif')

# Erase the video from memory
os.remove(video_name)

# Prompt the user that the GIF is ready and retained the filename they put in
print ''
print "Your GIF smoothie is now ready as " + gif_name + ".gif!!"