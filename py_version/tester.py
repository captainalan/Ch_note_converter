from track import Track

filename = 'megalovania.txt' 

# You will need to edit this every time you make a new file. This is your variable name.
# Make sure the filename is the same as this variable name when converting to chf files.
song = 'MegalovaniaStuff' 

# Testing
megalovania = Track(filename)
foo = megalovania.deMeasureTrack()
# print(megalovania) # Verfiying all measures are present got proc

for line in foo:
    print(line)

