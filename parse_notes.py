# Length to note value correspondences
# Can do more maths and clean this up later
len_to_val = {
    1:16,
    2:8,
    4:4
}

# Classes representing musical information
# --------------------------------------------------------------------

class Octave:
    """Relative note values in a given octave"""
    def __init__(self,num,notes):
        self.num   = num   # pitch probably isn't the right term here
        self.notes = notes # string of those notes
    # Something like: 5|--d---------------d-------|
    # will have num=5, notes="--d---------------d-------"

class Measure:
    """A measure of music in BLAH notation"""
    def __init__(self):
        self.octaves = [] # A list of notes in a given octave

    def addOctave(self, line):
        pass # convert line into...


# Read in file and process stuff using above classes
# --------------------------------------------------------------------

filename = 'megalovania.txt'
measures = [] # A list of measure objects read in from file
with open(filename, 'r') as score:
    for line in score:
        if line != '\n': # While not new line
            pass # add line to current thing
        else:
            pass
            # print("fart.") # Fart between each 'measure'


