from track import Track

filename = 'megalovania.txt'
# Testing
megalovania=Track(filename)

# Get rid of measures and print everything at once
megalovania.writeForRobots()

# bloop = megalovania.deMeasureTrack()
# for beep in bloop:
#     print(beep)

