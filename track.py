from measure import Measure

class Track:
    """Tracks ("Songs") are composed of measures"""

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

    def writeForRobots(self):
        """Print Track such that robots can make music"""
        # Length to note value correspondences
        # Can do more maths and clean this up later
        len_to_val = {
            1:16,
            2:8,
            4:4,
            8:2,
            16:1
        }
        # Get set of all octaves used 
        octaves = set()
        for measure in self.measures:
            octaves.update(measure.getOctaveSet())

        # Combine all measures
        # make sure each measure contains all octaves before combining
        # write a blank (e.g. "5|---------...--|" octave for unused octaves in
        # each measure.
        track = []
        for measure in self.measures:
            pass
            # Convert each measure...

    def __str__(self):
        return '\n\n'.join([str(measure) for measure in self.measures])


