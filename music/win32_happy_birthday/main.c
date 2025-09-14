// Plays "Happy Birthday" slowly via WinMM MIDI APIs.
// Build with CMake (links against winmm).

#include <windows.h>
#include <mmsystem.h>
#include <stdio.h>

#pragma comment(lib, "winmm.lib")

static DWORD pack_short_msg(BYTE status, BYTE data1, BYTE data2) {
    return (DWORD)((DWORD)status | ((DWORD)data1 << 8) | ((DWORD)data2 << 16));
}

static MMRESULT send_short(HMIDIOUT hmo, BYTE status, BYTE data1, BYTE data2) {
    return midiOutShortMsg(hmo, pack_short_msg(status, data1, data2));
}

static void program_change(HMIDIOUT hmo, int channel, int program) {
    send_short(hmo, (BYTE)(0xC0 | (channel & 0x0F)), (BYTE)(program & 0x7F), 0);
}

static void control_change(HMIDIOUT hmo, int channel, int controller, int value) {
    send_short(hmo, (BYTE)(0xB0 | (channel & 0x0F)), (BYTE)(controller & 0x7F), (BYTE)(value & 0x7F));
}

static void note_on(HMIDIOUT hmo, int channel, int note, int velocity) {
    send_short(hmo, (BYTE)(0x90 | (channel & 0x0F)), (BYTE)(note & 0x7F), (BYTE)(velocity & 0x7F));
}

static void note_off(HMIDIOUT hmo, int channel, int note) {
    send_short(hmo, (BYTE)(0x80 | (channel & 0x0F)), (BYTE)(note & 0x7F), 0);
}

static void all_notes_off(HMIDIOUT hmo, int channel) {
    control_change(hmo, channel, 123 /* All Notes Off */, 0);
}

// MIDI note numbers (C4 = 60)
enum {
    C4 = 60, Cs4, D4, Ds4, E4, F4, Fs4, G4, Gs4, A4, As4, B4,
    C5, Cs5, D5, Ds5, E5, F5, Fs5, G5, Gs5, A5, As5, B5
};

typedef struct {
    int midi;    // MIDI note number 0-127
    int beats;   // duration in beats
} NoteEvent;

// Global configurable tempo (milliseconds per beat)
// Default: 350ms for faster playback (was 700ms)
int G_BEAT_MS = 350;

int main(void) {
    HMIDIOUT hmo = NULL;
    MMRESULT mmr = midiOutOpen(&hmo, MIDI_MAPPER, 0, 0, 0);
    if (mmr != MMSYSERR_NOERROR) {
        char err[256] = {0};
        midiOutGetErrorTextA(mmr, err, sizeof(err));
        fprintf(stderr, "midiOutOpen failed: %s\n", err);
        return 1;
    }

    const int channel = 0;         // MIDI channel 1
    const int program = 0;         // Acoustic Grand Piano
    const int volume = 100;        // 0-127
    const int velocity = 100;      // 0-127

    program_change(hmo, channel, program);
    control_change(hmo, channel, 7 /* Main Volume */, volume);

    // "Happy Birthday" in key of C
    // Durations are approximate; held longer for a slow feel.
    const NoteEvent melody[] = {
        // Line 1: G G A G C B
        {G4,1}, {G4,1}, {A4,2}, {G4,2}, {C5,2}, {B4,4},
        // Line 2: G G A G D C
        {G4,1}, {G4,1}, {A4,2}, {G4,2}, {D5,2}, {C5,4},
        // Line 3: G G G(high) E C B A
        {G4,1}, {G4,1}, {G5,2}, {E5,2}, {C5,2}, {B4,2}, {A4,4},
        // Line 4: F F E C D C
        {F5,1}, {F5,1}, {E5,2}, {C5,2}, {D5,2}, {C5,4},
    };

    const size_t n = sizeof(melody)/sizeof(melody[0]);

    for (size_t i = 0; i < n; ++i) {
        int dur_ms = melody[i].beats * G_BEAT_MS;
        int on_ms = (int)(dur_ms * 0.88);   // leave a small gap between notes
        int off_ms = dur_ms - on_ms;
        if (on_ms < 10) on_ms = 10;
        if (off_ms < 10) off_ms = 10;

        note_on(hmo, channel, melody[i].midi, velocity);
        Sleep(on_ms);
        note_off(hmo, channel, melody[i].midi);
        Sleep(off_ms);
    }

    all_notes_off(hmo, channel);
    midiOutClose(hmo);
    return 0;
}

