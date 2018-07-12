class Octave:
    """Relative note values in a given octave"""
    # Something like: 5|--d---------------d-------|
    # will have num=5, notes="--d---------------d-------"

    # Constructor from string
    def __init__(self,line):
        self.num = int(line[0]) # Make this an Int!
        # Have to do -2 as second index to chop newline
        self.notes = line[2:-2]

    def __len__(self):
        return len(self.notes)

    def __str__(self):
        # Had to do || as escape sequence?
        return "{0}|{1}|".format(self.num,self.notes)