# twitter_gif_blender
##Twitter GIF grabber written for Frances Bean Cobain
*(post - https://twitter.com/alka_seltzer666/status/674806345548214272)*

**Note!** - This is all based on Mac OS X, which has Python pre-installed so these commands will run ad hoc

> If you'd like to understand how the Python script works, just open it in TextEdit or something similar, there are comments in there that explain everything!

**Note!** - You only ever have to do step 2 once! Make sure to run each command separately!

1. Open Terminal *(cmd + space, search for 'Terminal' or go to Applications/Utilities)*

2. This module needs three external Python libraries installed one by one. To install them, copy and paste each of the following into Terminal and hit enter *(you'll have to enter your password to install these as an administrator)*

	`sudo pip install beautifulsoup`

	`sudo pip install moviepy`

	`sudo pip install requests`

BeautifulSoup gets the movie file URL, Requests downloads it, and MoviePy makes it a GIF (the movie file gets deleted after that)

3. To run the script, type into Terminal

	`python gif_smoothie.py --URL--`

Where *--URL--* is the specific Twitter post's link

Then you can name your GIF, and you're done!

**From then on all you ever have to do is steps 1 and 3 to get other GIFs! Just as shown in the quick_demo.mp4 movie!**