const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  fullName: { type: String, required: true },
  faculty: { type: String },
  department: { type: String },
  studentNumber: { type: String },
  username: { type: String, required: true, unique: true },
  email: { type: String }, // eğer email kullanıyorsan burada kalabilir
  password: { type: String, required: true },
});

module.exports = mongoose.model('User', userSchema);
