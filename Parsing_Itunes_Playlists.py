import re, argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as n


def findDuplicates(fileName):
    print('Finding duplicates tracks %s..'% fileName)

    # read a playlist
    plist = plistlib.readPlist(fileName)

    # get the tracks from the Tracks dictionary
    tracks = plist['Tracks']

    # create a track name dictionary
    trackNames = {}

    # iterate through the tracks
    for trackId, track in tracks.item():
        try:
            name = track['Name']
            duration = track['Total Time']

            # look for ecisting entries
            if name in trackNames:
                # if a name and duration match, increment the count
                # round the track lenght to the nearest second

                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)

            else:
                 # add dictionary entry as a tuple (duration, count)
                trackNames[name] = (duration, 1)
        except:
            # ignore
            pass
        