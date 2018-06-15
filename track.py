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

    def deMeasureTrack(self):
        """Get rid of measures and return a simpler representation"""
        """Print Track such that robots can make music"""

        # Get set of all octaves used 
        octaves = []
        octaveCounts = {}
        for measure in self.measures:
            tempOctaveCounts = {}
            for m in measure.getOctaveList():
                if m in tempOctaveCounts:
                    tempOctaveCounts[m] = tempOctaveCounts[m] + 1
                else:
                    tempOctaveCounts[m] = 1
            for k in tempOctaveCounts:
                if k in octaveCounts:
                    if tempOctaveCounts[k] > octaveCounts[k]:
                        octaveCounts[k] = tempOctaveCounts[k]
                    else:
                        pass
                else:
                    octaveCounts[k] = tempOctaveCounts[k]

        # Get string representing all the octaves we need
        octaves = [str(key)*octaveCounts[key] for key in octaveCounts ]
        octaves = ''.join(octaves)
        octaves = [int(octaves[i]) for i in range(0,len(octaves))]
        octaves.sort()
        # print(octaves) gives something like [2, 3, 3, 4, 4, 5, 5, 6]
        # We have 1 measure of pitch 2, 2 measures of pitch 3, 2 measures
        # of pitch 4, etc.

        """
        Combine all measures
        Make sure each measure contains all octaves before combining
        Write a blank (e.g. "5|---------...--|" octave for unused octaves 
        in each measure.
        """

        track = []
        measureToWrite = Measure() # Empty measure to write stuff to
        for measure in self.measures:
            measureCopy = measure # can use mutable methods on this copy
            for o in octaves:
                if o in measure.getOctaveList():
                    # print("yipee what we got")
                    measureToWrite.addOctave(str(measureCopy.popOctaveN(o)))                    
                else:
                    # print("Gotta add empties")
                    # hardcoding 27 as measure length while I debug
                    measureToWrite.addOctave("{0}|{1}|".format(o,"-"*26))
            track.append(measureToWrite)
            measureToWrite = Measure() # Clear this

        """
        When all measures contain all octaves, we can combine those
        measures by simply concatenating strings.
        """

        combined = [ ["{0}|".format(i)] for i in octaves ]

        for i in range(0,len(track)):
            measure = track[i]
            for j in range(0,len(measure.octaves)):
                octave = measure.octaves[j]
                combined[j].append(octave.notes)
   
        for i in range(0,len(combined)):
            combined[i].append("|") # ending char
            combined[i] = ''.join(combined[i])

        # Printing to confirm output, remove later
        for line in combined:
            print(line) # okay looks fine

        # Now, we can go through `combined` and generate note representations,
        # counting the lengths of each note
    
    def writeForRobots(self):
        # Length to note value correspondences
        # Can do more maths and clean this up later
        len_to_val = {
            1:16,
            2:8,
            4:4,
            8:2,
            16:1
        }

        # Work from a "deMeasured" track; this way note lengths that go through
        # multiple measures are still captured! :)

    def __str__(self):
        return '\n\n'.join([str(measure) for measure in self.measures])


