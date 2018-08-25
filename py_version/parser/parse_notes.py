# Authors: Alan Wong and Gabriella Quattrone
# Note: this program only works with the format provided on this site: https://pianoletternotes.blogspot.com/
import argparse
from track import Track

parser = argparse.ArgumentParser()

parser.add_argument("filename", help="Path of the file you wish to parse.")
parser.add_argument("songname", help="Song name must match Ch filename.")

args = parser.parse_args()

filename = args.filename
song = args.songname

# Main
music = Track(filename)
print("""
/* File: """ + song + """.chf
   The function file """ + song + """.chf for melody """ + song + """ */
#include <linkbot.h>
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
}""")

# For testing purposes. We're still fixing deMeasureTrack().
# foo = music.deMeasureTrack()
# for line in foo:
#     print(line)
