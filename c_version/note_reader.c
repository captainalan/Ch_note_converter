#include <stdio.h>
#define OCTAVES       6     // Number of octaves to read note values for 
#define SONG_LEN    100     // Max length of a song 

/* Read in numeric sheet music representation into arrays. Array is two
 * dimensional; the first dimension represents the different octaves, the second
 * dimension represents the different notes (e.g. C, D, E...) in that octave.
 * For instance, we  might have:
 *
 * Octave 1 ['C', 'C', 'C', 'C'] 
 * Octave 2 ['G', '-', 'G', '-']
 * Octave 3 ['-', '-', '-', '-']
 *
 * ...where a dash represents an empty value (no sound from that octave). Each
 * octave array should be of the same length.
 * */

/* Array to contain musical info */
/* By default, we'll support 6 octaves */
char song[SONG_LEN][SONG_LEN][SONG_LEN][SONG_LEN][SONG_LEN][SONG_LEN];

void read_file(){
    printf("Reading in file... la la la!\n");
}

void write_file(){
    // Write stored song to another file (or standard output?)
}
