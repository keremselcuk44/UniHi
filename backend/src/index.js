const path = require('path');
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const aiRoutes = require('./routes/ai');
const app = express();
const port = 3001;


// CORS configuration
app.use(cors());

// Helmet configuration with relaxed settings
app.use(helmet({
  crossOriginResourcePolicy: { policy: "cross-origin" },
  crossOriginOpenerPolicy: { policy: "unsafe-none" },
  contentSecurityPolicy: false,
}));

app.use(express.json()); // Parse JSON bodies

// Routes
app.use('/api/ai', aiRoutes);

app.use(express.static(path.join(__dirname, '..', '..')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '..', '..', 'home.html'));
});

// Basic route
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', message: 'Server is running' });
});

// GitHub webhook
app.post('/webhook', (req, res) => {
  // GitHub’dan gelen push olayını burada işlersin
  console.log('Webhook geldi:', req.body);
  res.status(200).end();
});


// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
}); 
