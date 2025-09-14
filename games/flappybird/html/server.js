const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from current directory
app.use(express.static(__dirname));

// Main route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Start server
app.listen(PORT, () => {
    console.log(`\n🎮 Flappy Bird Game Server Running!`);
    console.log(`📍 Local: http://localhost:${PORT}`);
    console.log(`\nPress Ctrl+C to stop the server\n`);
});