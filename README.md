#A Personal Greek Reader

This is a little Greek reader I made for myself. It is nothing fancy but I figured I would share it anyway. A few things to note.

*   I'm not good at Python, so don't assume the simple Python script for making this (create.py) is good Python.
*   I'm not good at LaTeX, so don't assume the LaTeX is worthy to be emulated.
*   I'm not sharing this so you can use *my* reader. The notes aren't meant to be comprehensive. They are just notes that I make as I go along for me. I'm sharing this just in case you also might find having a personal reader useful. You can use the scripts to make your own.

I built this to solve two of my problems. First, I wanted a reader that could be used with two separate typeface sizes. I generally do my Greek reading in one of two modes, in a chair (small text is okay) or on a treadmill (big text is necessary). Second, I wanted to build this reader so that later on, if I want to mine these files for data, I can get to the data easily (so it can't be in an annoying to parse format, like Microsoft Word). My solution was to use LaTeX and generate a version for normal reading and one for the treadmill off the same source.

The output isn't perfect (for the treadmill version you'll notice the page number is cut off at the bottom) but it has been working great for me for a number of weeks now.

##Dependencies

*   This script uses Python 3, so if you don't have this on your system, you will need to install it. Once installed, "python3 create.py" in a shell should generate everything for you.
*   I am using Gentium Plus for the Greek font because it is the best ever. You will either need to change the font or get that installed on your system.

I have annotated the Python source to make it relatively easy for modification for those who don't know Python.

So that's why this exists. If you find it useful, please let me know.
