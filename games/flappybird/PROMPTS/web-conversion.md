# Flappy Bird Web Conversion - Progressive Prompts

Convert the Python Flappy Bird game to a web version. Start after completing the Python version.

## Prompt 1: Convert to HTML5/JavaScript

```
Convert the Python Flappy Bird game to HTML5/JavaScript:
- Create a single HTML file with embedded CSS and JavaScript
- Use HTML5 Canvas for rendering
- Implement the same game mechanics (gravity, jumping, pipes, collision)
- Use requestAnimationFrame for the game loop
- Keep the same controls (spacebar to jump)
- No external dependencies or frameworks
```

## Prompt 2: Add All Game Features

```
Add all the features from the Python version:
- Lives system (start with 3 lives)
- Invulnerability after hit
- Score display
- Pause with 'P' key
- God mode with 'G' key
- Extra lives with 'I' key
- High score tracking
- Same physics constants at top of script
```

## Prompt 3: Add Touch Support

```
Add mobile/touch support:
- Tap or click anywhere to jump
- Make the game responsive to different screen sizes
- Ensure buttons are large enough for touch
- Add viewport meta tag for mobile
- Test that it works on both desktop and mobile
```

## Prompt 4: Create Node.js Server

```
Create a simple Express server to host the game:
- Create server.js using Express
- Serve the HTML file on port 3000
- Create package.json with start script
- Add instructions for running with: npm start
- Include alternative Python server instructions
```

## Prompt 5: Add Visual Polish

```
Enhance the web version's visuals:
- Add CSS animations for smoother movement
- Use gradients for sky background
- Add shadow effects to pipes and bird
- Make clouds semi-transparent
- Add a subtle bounce animation when jumping
Keep it lightweight and CSS-based.
```

## Notes

- Each prompt builds on the previous one
- Maintain feature parity with the Python version
- Keep everything in minimal files (HTML + server.js)
- Focus on compatibility and performance