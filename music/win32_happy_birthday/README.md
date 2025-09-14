# Win32 Happy Birthday MIDI Player

A Windows-specific MIDI player written in C that plays "Happy Birthday" using the Windows Multimedia API. This project demonstrates low-level audio programming and system API usage.

## 📚 Development Prompts

**[View the progressive prompts used to build this application →](PROMPTS/)**

## Features

- **MIDI playback** - Uses Windows MIDI synthesizer
- **No external files** - Melody encoded in the program
- **Configurable tempo** - Adjustable playback speed
- **Instrument selection** - Choose from MIDI instruments
- **Volume control** - Set playback volume
- **Loop mode** - Continuous playback option
- **Professional build** - CMake configuration included

## Quick Start

### Building with CMake
```bash
cd music/win32_happy_birthday
mkdir build
cd build
cmake ..
cmake --build .
./wi32_midi_happy_birthday.exe
```

### Direct Compilation
```bash
gcc main.c -o midi_happy_birthday.exe -lwinmm
./midi_happy_birthday.exe
```

## Usage

```bash
# Basic usage (plays once with default settings)
wi32_midi_happy_birthday.exe

# With options
wi32_midi_happy_birthday.exe [instrument] [tempo] [volume] [--loop]

# Examples
wi32_midi_happy_birthday.exe 0 120 64        # Piano, 120 BPM, medium volume
wi32_midi_happy_birthday.exe 24 140 100      # Guitar, 140 BPM, loud
wi32_midi_happy_birthday.exe 73 100 50 --loop # Flute, 100 BPM, soft, looping
```

## Instrument Numbers

Common MIDI instruments:
- 0: Acoustic Grand Piano
- 19: Church Organ
- 24: Acoustic Guitar (nylon)
- 40: Violin
- 56: Trumpet
- 73: Flute
- (0-127 available)

## Technical Details

### Windows Multimedia API
- `midiOutOpen()` - Opens MIDI output device
- `midiOutShortMsg()` - Sends MIDI messages
- `midiOutReset()` - Resets device state
- `midiOutClose()` - Closes MIDI device

### MIDI Messages
- **Note On**: 0x90 | channel, note, velocity
- **Note Off**: 0x80 | channel, note, velocity
- **Program Change**: 0xC0 | channel, instrument

### Note Encoding
- Middle C (C4) = MIDI note 60
- Each semitone up = +1
- Each octave up = +12

## Project Structure

```
win32_happy_birthday/
├── PROMPTS/          # AI development prompts
│   ├── README.md     # Prompts guide
│   └── development.md # Progressive prompts
├── main.c            # Main program source
├── CMakeLists.txt    # CMake build configuration
├── build/            # Build output directory
└── README.md         # This file
```

## Requirements

- **Windows OS** - Uses Windows-specific APIs
- **C Compiler** - MinGW, MSVC, or compatible
- **Windows SDK** - For multimedia headers
- **CMake** (optional) - For build management

## How It Works

1. Opens the default Windows MIDI output device
2. Sends MIDI messages to play notes
3. Each note has:
   - Pitch (MIDI note number)
   - Duration (milliseconds)
   - Velocity (volume/intensity)
4. Plays the Happy Birthday melody
5. Properly closes MIDI device when done

## Limitations

- **Windows only** - Uses Windows Multimedia API
- **Requires MIDI support** - Windows must have MIDI synthesizer
- **No external MIDI** - Only uses built-in Windows MIDI
- **Single melody** - Only plays Happy Birthday (but easy to modify)

## Learning Objectives

This project teaches:
- Windows API programming
- MIDI protocol basics
- Low-level audio control
- System resource management
- C programming practices
- CMake build systems

## Extending the Project

Ideas for enhancement:
- Add more songs
- Read MIDI files
- Create a simple sequencer
- Add a GUI with Windows API
- Support for external MIDI devices
- Real-time keyboard input
- Multi-track playback

## Development

See the [PROMPTS folder](PROMPTS/) for step-by-step instructions on building this application from scratch using AI assistance.

## Troubleshooting

- **No sound**: Check Windows sound settings and MIDI configuration
- **Compilation errors**: Ensure winmm library is linked (`-lwinmm`)
- **CMake issues**: Verify CMake version >= 3.10
- **Stuck notes**: Program includes proper cleanup, but Ctrl+C may leave notes on

## License

Open source for educational purposes. Demonstrates Windows system programming concepts.