#include <stdio.h>
#include "note_reader.h"

int main(int argc, char **argv){
//argv[0] will be myprogram.
//argv[1] will be myfile.txt.

  /* All parser functions declared in `note_reader.h` (and defined in
   * `note_reader.c`).
   *
   * In this file, do stuff like get command line arguments, store relevant
   * things in variables/memory to pass to parsing functions...
   */

  printf("Hello Robots\n");
  read_file(); // DO IT WORK?
  
  // megalovania = Track(filename); // this needs to have a declared type

  // Get rid of measures and print everything at once
  // megalovania.writeForRobots(); // figure out how this works in C
}
