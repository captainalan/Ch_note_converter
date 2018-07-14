# Let LinkBots Make Music

## Problem Description

We want to easily translate music sheets into Ch code! First we start with Python, then we port to C/Ch.
Our choice of music sheets is based on https://pianoletternotes.blogspot.com/.

### Input Representation

Each group of letter notes is played from left to right, and
vertical letters on the same column are played together. The numbers
in front of each line are the octave. Lowercase (a c g f) letters are natural
notes (white keys). Uppercase (A C G F) letters are the sharp notes
(black keys a.k.a. A# C# G# F#). The lines between letters indicates
timing to play the notes.

### Output Representation
    #include <linkbot.h>
    CLinkbotI robot;

    note_t SongName(int i)
    {
    int len;
    note_t note;
    note_t song[ ] =
    {
        {NOTE_D4, 32}, {NOTE_D4, 32}, {NOTE_D5, 8}, {NOTE_A4, 4},
        {NOTE_GS4, 8}, {NOTE_G4, 8}, {NOTE_F4, 8}, {NOTE_D4, 32},
        {NOTE_F4, 32}, {NOTE_G4, 32}
    };

    len = sizeof(song) / sizeof(note_t);
    if (i < len)
    {
        note.frequency = song[i].frequency;
        note.duration = song[i].duration;
        }
    else {
        note.frequency = -1;
        note.duration = -1;
        }

    return note;
    }

    note_t SongName(int i);
    robot.playMelody(SongName, 1);
