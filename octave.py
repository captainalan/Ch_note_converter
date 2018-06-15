class Octave:
    """Relative note values in a given octave"""
    # Something like: 5|--d---------------d-------|
    # will have num=5, notes="--d---------------d-------"

    # Constructor from string
    def __init__(self,line):
        self.num = line[0]
        self.notes = line[2:-1]

    def __str__(self):
        return "{0}|{1}".format(self.num,self.notes)


