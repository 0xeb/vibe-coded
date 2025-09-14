# Win32 Happy Birthday MIDI Player - Progressive Prompts

Build a Windows MIDI player in C that plays "Happy Birthday".

## Prompt 1: Basic MIDI Setup

```
Create a C program for Windows that plays Happy Birthday using MIDI:
- Include windows.h and mmsystem.h
- Open the default MIDI output device using midiOutOpen
- Define MIDI note numbers for the song (C4=60, D4=62, E4=64, F4=65, G4=67, A4=69, B4=71)
- Create a simple playNote function that sends MIDI messages
- Play a test note (middle C) for 1 second
- Close MIDI device properly
- Link with winmm library
```

## Prompt 2: Implement Happy Birthday Melody

```
Add the complete Happy Birthday melody:
- Create arrays for notes and durations
- Happy Birthday notes: G G A G C B, G G A G D C, G G G* E C B A, F F E C D C
- Use 0 for rests/pauses
- Quarter note = 500ms, half note = 1000ms
- Loop through arrays playing each note
- Add 50ms gap between notes for clarity
```

## Prompt 3: Add Tempo Control

```
Make the tempo adjustable:
- Add BPM (beats per minute) variable, default 120
- Calculate note durations based on BPM
- Quarter note = 60000/BPM milliseconds
- Adjust all durations proportionally
- Print current BPM when starting
```

## Prompt 4: Add Instrument Selection

```
Allow different instrument sounds:
- Use MIDI Program Change message to select instruments
- Add common instruments: Piano=0, Organ=19, Guitar=24, Flute=73, Trumpet=56
- Default to Piano
- Print selected instrument name
```

## Prompt 5: Command Line Arguments

```
Add command line argument parsing:
- First argument: instrument number (0-127)
- Second argument: tempo BPM (60-240)
- Third argument: volume (0-127)
- Show usage if arguments are invalid
- Example: program.exe 24 140 100 (guitar, 140 BPM, volume 100)
```

## Prompt 6: Add CMake Build System

```
Create CMakeLists.txt for the project:
- Project name: MidiHappyBirthday
- Minimum CMake version 3.10
- Add executable from main.c
- Link winmm library
- Add compiler warnings for MSVC and GCC
- Set output name to wi32_midi_happy_birthday
```

## Prompt 7: Add Loop Mode

```
Add option to loop the song:
- Add --loop command line flag
- Play song continuously when loop mode is on
- Print "Press Ctrl+C to stop" message
- Add 2 second pause between repetitions
- Ensure clean exit on Ctrl+C
```

## Prompt 8: Polish and Error Handling

```
Add final improvements:
- Check if MIDI device is available
- Print friendly error messages
- Add help text with --help flag
- Show progress while playing (note 1/25, note 2/25...)
- Reset MIDI device before closing to stop any stuck notes
- Add version information
```

## Notes

- Each prompt builds on the previous code
- Test audio output after each step
- Windows-specific - requires Windows Multimedia API
- Compile with: gcc main.c -o midi.exe -lwinmm
- Or use CMake for more professional build setup