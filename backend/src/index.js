const path = require('path');
require('dotenv').config({ path: path.resolve(__dirname, '../.env') });
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const bcrypt = require('bcrypt');
const app = express();
const port = 3001;

// Routes
const aiRoutes = require('./routes/ai'); // AI route'ları (varsa)

// Güvenlik ve CORS
app.use(cors());
app.use(helmet({
  crossOriginResourcePolicy: { policy: "cross-origin" },
  crossOriginOpenerPolicy: { policy: "unsafe-none" },
  contentSecurityPolicy: false,
}));
app.use(express.json());

// MongoDB bağlantısı
mongoose.connect('mongodb://localhost:27017/unihi_db', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('MongoDB ye bağlantı başarılı!'))
.catch(err => console.error('MongoDB bağlantı hatası:', err));

// User modeli
const User = require('./models/User');

app.post('/api/login', async (req, res) => {
  try {
    const { username, password } = req.body;

    const user = await User.findOne({ username });
    if (!user) {
      return res.status(404).json({ message: 'Kullanıcı bulunamadı' });
    }

    const passwordMatch = await bcrypt.compare(password, user.password); // hash karşılaştırması

    if (!passwordMatch) {
      return res.status(401).json({ message: 'Şifre yanlış' });
    }

    res.status(200).json({ message: 'Giriş başarılı', user });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Sunucu hatası' });
  }
});


app.post('/api/register', async (req, res) => {
  try {
    const { fullName, faculty, department, studentNumber, username, password } = req.body;

    const existingUser = await User.findOne({ username });
    if (existingUser) {
      return res.status(400).json({ message: 'Bu kullanıcı adı zaten var' });
    }

    const hashedPassword = await bcrypt.hash(password, 10); // şifreyi hashle

    const newUser = new User({
      fullName,
      faculty,
      department,
      studentNumber,
      username,
      password: hashedPassword, // hashlenmiş şifreyi kaydet
    });

    await newUser.save();
    res.status(201).json({ message: 'Kayıt başarılı' });
  } catch (e) {
    console.error(e);
    res.status(500).json({ message: 'Sunucu hatası' });
  }
});

// AI route'ları
app.use('/api/ai', aiRoutes);

// Frontend dosyaları
app.use(express.static(path.join(__dirname, '..', '..')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '..', '..', 'home.html'));
});

// Sağlık kontrol endpoint'i
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', message: 'Server is running' });
});

// GitHub webhook
app.post('/webhook', (req, res) => {
  console.log('Webhook geldi:', req.body);
  res.status(200).end();
});

// Global hata yakalayıcı middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Server başlat
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
