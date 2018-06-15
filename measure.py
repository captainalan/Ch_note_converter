from octave import *

class Measure:
    """A measure of music in BLAH notation
   
    TODO: ensure that all octaves are of same length

    """
    def __init__(self):
        self.octaves = [] # A list of notes in a given octave

    def addOctave(self, line):
        try:
            self.octaves.append(Octave(line))
        except:
            print("Oops.")

    def getMeasureLength(self):
        if not(self.octaves == []):
            return len(self.octaves[0].notes)
        else:
            return 0

    def getOctaveSet(self):
        """Return the Octave.num values as a set"""
        return {octave.num for octave in self.octaves}

    def __str__(self):
        return '\n'.join([str(octave) for octave in self.octaves])


