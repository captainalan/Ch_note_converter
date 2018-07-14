from octave import Octave

class Measure:
    """A measure of music in specific notation
   
    TODO: ensure that all octaves are of same length

    """
    def __init__(self):
        self.octaves = []

    def addOctave(self, line):
        try:
            self.octaves.append(Octave(line))
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
        for o in self.octaves:
            if o.num == n:
                temp = o
                self.octaves.remove(o)
                return temp

    def __str__(self):
        return '\n'.join([str(octave) for octave in self.octaves]) \
        + '\n'


