# Authors: Alan Wong and Gabriella Quattrone
from octave import Octave

class Measure:
    def __init__(self):
        self.octaves = []
        self.length = 0

    def addOctave(self, line):
        """If the octave being added is the first one, then use this to set the measure length.
           Otherwise, ensure that the new octave being added is the same length as the measure
           length."""
        if self.octaves == []:
            self.length = (len(line))
        try:
            assert len(line) == self.length
            self.octaves.append(Octave(line))
        except AssertionError:
            print("Something is wrong with the line length:\n{}".format(str(line)))
            print("This measure:\n", str(self) )
        except:
            print("Oops. Can't append octave: {}".format(str(line)))

    def getMeasureLength(self):
        if not(self.octaves == []):
            return len(self.octaves[0].notes)
        else:
            print("Problem getting measure length")
            return 0

    def getOctaveList(self):
        """Return the Octave.num values as a list"""
        return sorted([octave.num for octave in self.octaves], \
            reverse=True)

    def popOctaveN(self,n):
        """Return first octave of pitch n"""
        for o in reversed(self.octaves):
            if o.num == n:
                temp = o
                self.octaves.remove(o)
                return temp

    def __str__(self):
        return '\n'.join([str(octave) for octave in self.octaves]) \
        + '\n'
