from track import Track

filename = 'megalovania.txt' 

# Testing
foo = Track(filename)
bar = foo.deMeasureTrack()
# print(foo) # Verfiying all measures are present got proc

for line in bar:
    print(line)

