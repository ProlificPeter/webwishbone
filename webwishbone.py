# webwishbone.py - PRL Granlund - (c) RL Dimensions
#
# Simple script for pulling local webfiles from a directory tree.

import os

class WebWishbone(object):
    
    @staticmethod
    def hunt(directory):
        listOfDirectoryAndFiles = []
        for dirPath, __, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".htm") or filename.endswith(".html"):
                    listOfDirectoryAndFiles.append((dirPath, filename))
        return listOfDirectoryAndFiles