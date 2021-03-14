const mongoose = require("mongoose");

const OrderSchema = mongoose.Schema({
  user: String,
  skus: [
    {
      name: String,
      quantity: Number,
      price: Number,
    },
  ],
  price: Number,
  created_at: { type: Date, default: Date.now },
});

module.exports = mongoose.model("orders", OrderSchema);
