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

    # Constructor from string
    def __init__(self,line):
        self.num = line[0]
        self.notes = line[2:-1]

    def __str__(self):
        return "{0}|{1}".format(self.num,self.notes)

class Measure:
    """A measure of music in BLAH notation"""
    def __init__(self):
        self.octaves = [] # A list of notes in a given octave

    def addOctave(self, line):
        try:
            self.octaves.append(Octave(line))
        except:
            print("Oops.")
    def __str__(self):
        return '\n'.join([str(octave) for octave in self.octaves])

class Track:
    """Tracks ("Songs") are composed of measures"""
    def __init__(self):
        self.measures = [] # A list of measure objects that make up a track 

    def __init__(self, filename):
        self.measures = [] # Read measures from a file
        with open(filename, 'r') as score:
            currentMeasure = Measure() # Make a new measure
            for line in score:
                if line != '\n': # While not new line
                    currentMeasure.addOctave(line) # add line to current thing
                else:
                    # At new line, add current measure to list of measures
                    saveMeasure = currentMeasure
                    self.measures.append(saveMeasure)
                    currentMeasure = Measure() # Reset measure, continue

    def addMeasure(self,measure):
        try:
            self.measures.append(measure) # check to make sure its a measure
        except:
            print("Oops")

    def __str__(self):
        return '\n\n'.join([str(measure) for measure in self.measures])


# Read in file and process stuff using above classes
# --------------------------------------------------------------------

filename = 'megalovania.txt'
# Testing
megalovania=Track(filename)
print(megalovania)


