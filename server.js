const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');
const config = require('./config');

const app = express();
const port = process.env.PORT || 8080;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Test endpoint
app.get('/api/test', (req, res) => {
    res.json({ message: 'Server is working!' });
});

// Gemini API endpoint
app.post('/api/gemini', async (req, res) => {
    try {
        const { message } = req.body;
        console.log('Received message:', message);
        
        const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${config.GEMINI_API_KEY}`;
        console.log('Calling Gemini API...');
        
        const response = await fetch(apiUrl, {
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
        console.log('Gemini API Response:', data);
        
        if (!data.candidates || !data.candidates[0]) {
            console.error('Invalid response from Gemini API:', data);
            return res.status(500).json({ error: 'Invalid response from Gemini API' });
        }
        
        res.json(data);
    } catch (error) {
        console.error('Gemini API Error:', error);
        res.status(500).json({ error: 'Internal server error', details: error.message });
    }
});

// GNews API endpoint
app.get('/api/news', async (req, res) => {
    try {
        const response = await fetch(`https://gnews.io/api/v4/search?q=artificial+intelligence&lang=tr&country=tr&max=5&apikey=${config.GNEWS_API_KEY}`);
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