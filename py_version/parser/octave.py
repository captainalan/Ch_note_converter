# Authors: Alan Wong and Gabriella Quattrone
import re

class Octave:
    """Relative note values in a given octave"""
    # Something like: 5|--d---------------d-------|
    # will have num=5, notes="--d---------------d-------"

    # Constructor from string
    def __init__(self,line):
        self.num = int(line[0]) 
        # Read `|` as marking the beginning and end of the string (exclusive)
        notes = re.search(r"\|(.*)\|", line)
        self.notes = str(notes.group(1))

    def __len__(self):
        return len(self.notes)

    def __str__(self):
        return "{0}|{1}|".format(self.num,self.notes)