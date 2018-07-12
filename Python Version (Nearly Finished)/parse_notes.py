from track import Track

filename = 'megalovania.txt' # Put music text file you wish to convert to Ch format here

# Note: this program only works with the format provided on this site: https://pianoletternotes.blogspot.com/

# Testing
megalovania = Track(filename)

# Get rid of measures and print everything at once
megalovania.writeForRobots()
