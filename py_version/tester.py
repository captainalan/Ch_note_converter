from track import Track

filename = 'megalovania.txt' 

# You will need to edit this every time you make a new file. This is your variable name.
# Make sure the filename is the same as this variable name when converting to chf files.
song = 'MegalovaniaStuff' 

# Testing
megalovania = Track(filename)
foo = megalovania.deMeasureTrack()
for line in foo:
    print(line)

"""
foo = megalovania.deMeasureTrack()
for line in foo:
    print(line)
"""
