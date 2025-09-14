# Win32 Happy Birthday - Development Prompts

This folder contains the progressive prompts for building the Windows MIDI player.

## 📚 Prompt Files

- **[development.md](development.md)** - 8 progressive prompts to build the MIDI player

## 🎵 Development Approach

The prompts build a Windows-specific MIDI application:
1. Set up basic MIDI output
2. Implement the melody
3. Add controls and features
4. Create professional build system

## 🚀 How to Use

1. Start with Prompt 1 in `development.md`
2. Each prompt adds specific functionality
3. Test audio output after each step
4. Compile with: `gcc main.c -o midi.exe -lwinmm`
5. By Prompt 8, you have a complete MIDI player with CMake build

## 🔧 Technical Requirements

- Windows operating system
- C compiler (MinGW, MSVC)
- Windows Multimedia API (winmm)
- CMake (optional, added in Prompt 6)

## 💡 Key Concepts

- MIDI protocol and messages
- Windows Multimedia API
- Low-level audio programming
- Command-line argument parsing
- Professional build configuration

## Summary

These prompts demonstrate system-level audio programming on Windows, teaching how to interact directly with the OS multimedia capabilities. Perfect for learning low-level audio control and Windows API programming.