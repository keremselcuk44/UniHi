require('dotenv').config();
const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');

const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Gemini API endpoint
app.post('/api/gemini', async (req, res) => {
    try {
        const { message } = req.body;
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${process.env.GEMINI_API_KEY}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                contents: [{
                    parts: [{
                        text: message
                    }]
                }]
            })
        });

        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error('Gemini API Error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// GNews API endpoint
app.get('/api/news', async (req, res) => {
    try {
        const response = await fetch(`https://gnews.io/api/v4/search?q=artificial+intelligence&lang=tr&country=tr&max=5&apikey=${process.env.GNEWS_API_KEY}`);
        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error('GNews API Error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
}); 