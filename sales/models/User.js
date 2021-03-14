const mongoose = require("mongoose");

const UserSchema = mongoose.Schema({
  name: {
    first: String,
    last: String,
  },
  email: { type: String, unique: true },
  password: String,
  image: { type: String, default: "default.jpg" },
  created_at: { type: Date, default: Date.now },
});

module.exports = mongoose.model("users", UserSchema);
