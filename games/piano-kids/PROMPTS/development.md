# Piano Kids Development - Progressive Prompts

Build an educational piano for children in a single HTML file.

## Prompt 1: Basic Piano Interface

```
Create a single HTML file for a kids' piano:
- Title "Piano Kids" at the top
- 6 large buttons numbered 1-6 arranged horizontally
- Colorful, kid-friendly design with bright colors
- Each button should be large enough for small fingers
- All CSS embedded in <style> tags
- Responsive layout that works on tablets
```

## Prompt 2: Add Sound with Web Audio API

```
Make the piano keys produce sound:
- Use Web Audio API to generate tones (no external audio files)
- Keys 1-6 play notes C4, D4, E4, F4, G4, A4
- Each note plays for 200ms when clicked
- Add visual feedback - keys change color when pressed
- Include touch event support for tablets
```

## Prompt 3: Add Keyboard Support

```
Enable computer keyboard input:
- Number keys 1-6 trigger the corresponding piano keys
- Same visual and audio feedback as clicking
- Prevent sound repetition when key is held down
- Add instruction text: "Click keys or press number keys 1-6"
```

## Prompt 4: Create Song Library

```
Add pre-programmed children's songs:
- Create a songs array with at least 3 songs
- Each song has: name and notes (as string of numbers)
- Include "Twinkle Twinkle" (1 1 5 5 6 6 5, 4 4 3 3 2 2 1)
- Add "Mary Had a Little Lamb" 
- Add "Happy Birthday"
- Use commas for phrase breaks in notation
```

## Prompt 5: Add Song Playback

```
Implement automatic song playback:
- Dropdown to select a song
- Play button to start playing selected song
- Stop button to halt playback
- Keys light up as notes play
- Disable manual playing during playback
- 400ms between notes by default
```

## Prompt 6: Add Playback Controls

```
Add speed and volume controls:
- Speed selector: Slow (1x), Medium (1.5x), Fast (2x)
- Volume slider from 0-100% (default 50%)
- Controls should be kid-friendly with clear labels
- Speed affects note duration proportionally
```

## Prompt 7: Display Song Notation

```
Show the song being played:
- Display song notes below the piano
- Highlight the current note during playback
- Use large, colorful numbers
- Numbers should match key colors
- Auto-scroll if song is long
```

## Prompt 8: Add More Songs

```
Expand the song library to 10+ songs:
- "Old MacDonald Had a Farm"
- "Row Row Row Your Boat"
- "The Wheels on the Bus"
- "London Bridge"
- "Baa Baa Black Sheep"
- "Hickory Dickory Dock"
- "Jack and Jill"
- Organize alphabetically in dropdown
```

## Prompt 9: Add Print Mode

```
Create a print-friendly view:
- Button to show print mode
- Display selected song title and number notation
- Hide all controls and piano keys
- Large, clear numbers for easy reading
- Button to return to normal view
- Clean layout for printing on paper
```

## Prompt 10: Final Polish

```
Add finishing touches:
- Help section with simple instructions for kids
- Emoji icons for visual appeal (🎹 🎵 🎶)
- Loading animation when switching songs
- Better mobile responsiveness
- Smooth animations for all interactions
- About section explaining the educational benefits
```

## Notes

- Keep everything in a single HTML file for easy sharing
- No external dependencies or files
- Focus on simplicity and kid-friendly design
- Test on various devices, especially tablets
- Ensure all features work together smoothly