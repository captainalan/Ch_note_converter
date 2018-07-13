TARGET = parse_notes
CC = gcc
CFLAGS = -g -Wall

.PHONY : default all clean

default: $(TARGET)
all: default

HEADERS = note_reader.h
OBJECTS = note_reader.o parse_notes.o

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) -c $< -o $@

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -Wall -o $@

clean:
	rm -f *.o
	rm -f $(TARGET)
