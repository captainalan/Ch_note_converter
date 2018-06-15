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

        return combined
    
    def writeForRobots(self):
        roboNoteString = [] # Will be what we return

        """Some helper functions"""
        # Length of string in chars to note value conversion
        len_to_val = (lambda x: 16/x) # e.g. c (len = 1) is a 16/1 -> 16th note
        # Note to Note Conversions from stringy piano music to robots
        n2n = {
                'c':'C',
                'C':'CS',
                'd':'D',
                'D':'DS',
                'e':'E',
                'E':'ES',
                'f':'F',
                'F':'FS',
                'g':'G',
                'G':'GS',
                'a':'A',
                'A':'AS',
                'b':'B',
                'B':'BS' # b-b-b-buuuuulllllhit
        }

        # WRITE FUNCTION TO APPROPRIATELY MAP NOTE NAMES BETWEEN TWO CONVENTIONS

        """
        As we iterate through octaves, keep track of the current note's length.
        Reset to 0 and begin counting from one whenever a new note is being
        added.  
        """

        currentNote    = 'start' # Just initializing this
        currentOctave  = 'start'
        currentNoteLen = 0  

        # Work from a "deMeasured" track; this way note lengths that go through
        # multiple measures are still captured! :)
        combined = self.deMeasureTrack()

        octaves = [int(octave[0]) for octave in combined]

        for i in range(2,len(combined[0])): # Skip first two characters
            """combined[0] is an octave; index 0 arbitrarily chosen"""
            # Imagine a vertical bar, simultaneously covering all octaves 
            currentBeat = [octave[i] for octave in combined]

            # Two paths:
            if all([i=='-' for i in currentBeat]):
                # (1) all octaves have '-' so just increase duration of previous
                currentNoteLen = currentNoteLen + 1
                continue
            elif (currentNote != 'start'):
                # (2) we're done with current note; output/save it
                # print("{0}, duration: {1}".format(currentNote,currentNoteLen))
                print("{{NOTE_{0}{1},{2:.3}}}".format(n2n[currentNote],
                    currentOctave,len_to_val(currentNoteLen)), end=', ')

            # Choose current note
            # Current heuristic; just choose highest octave one
            for i in range(-1,-1 * (len(currentBeat) + 1), -1): # Count backwards
                if (currentBeat[i] != '-'):
                    currentNote = currentBeat[i]
                    currentNoteLen = 1
                    currentOctave = len(currentBeat) + i
                    break
                else:
                    pass # Do nothing if we're just sustaining a note

    def __str__(self):
        return '\n\n'.join([str(measure) for measure in self.measures])


