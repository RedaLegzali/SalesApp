const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
require("dotenv/config");

const app = express();
const DB_URI = `mongodb://${process.env.DB_HOST}:${process.env.DB_PORT}/${process.env.DB_NAME}`;

app.use(cors());
app.use(express.json());

const ordersRoute = require("./routes/orders");
const usersRoute = require("./routes/users");
app.use("/orders", ordersRoute);
app.use("/users", usersRoute);

mongoose.connect(DB_URI, { useNewUrlParser: true }, () => {
  console.log("Mongoose Connected");
});

app.listen(process.env.PORT, () => {
  console.log(`Listening on port ${process.env.PORT}`);
});
