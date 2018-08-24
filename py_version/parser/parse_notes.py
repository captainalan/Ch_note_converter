# Authors: Alan Wong and Gabriella Quattrone
from track import Track

filename = 'reflection.txt' # Put music text file you wish to convert to Ch format here
# Note: this program only works with the format provided on this site: https://pianoletternotes.blogspot.com/


# You will need to edit this every time you make a new file. This is your variable name.
# Make sure the filename is the same as this variable name when converting to chf files.
song = 'Reflection' 

# Testing
music = Track(filename)
print("""
#include <linkbot.h>
CLinkbotI robot;

note_t """ + song + """(int i) {
    int len;
    note_t note;
    note_t song[] = {""")

# Get rid of measures and print everything at once
music.writeForRobots()

print("""
 };

    len = sizeof(song) / sizeof(note_t);
    if (i < len) {
        note.frequency = song[i].frequency;
        note.duration = song[i].duration;
    } else {
        note.frequency = -1;
        note.duration = -1;
    }

    return note;
}

note_t """ +  song + """(int i);

robot.playMelody(""" + song + ", 1);")

# For testing purposes. We're still fixing deMeasureTrack().
# foo = music.deMeasureTrack()
# for line in foo:
#     print(line)
