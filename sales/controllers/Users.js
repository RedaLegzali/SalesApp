const User = require("../models/User");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

const get = (req, res) => {
  User.findOne({ email: req.user.email })
    .then((data) => {
      res.json(data);
    })
    .catch((err) => {
      res.status(400).json(err);
    });
};

const register = (req, res) => {
  bcrypt.genSalt(10).then((salt) => {
    bcrypt.hash(req.body.password, salt).then((hash) => {
      const user = new User({
        name: req.body.name,
        email: req.body.email,
        password: hash,
        image: req.body.image,
      });
      user
        .save()
        .then((data) => {
          res.json(data);
        })
        .catch((err) => {
          res.status(400).json(err);
        });
    });
  });
};

const delete_one = (req, res) => {
  User.deleteOne({ email: req.user.email })
    .then((data) => {
      res.json(data);
    })
    .catch((err) => {
      res.status(400).json(err);
    });
};

const login = (req, res) => {
  User.findOne({ email: req.body.email })
    .then((user) => {
      bcrypt
        .compare(req.body.password, user.password)
        .then((result) => {
          if (result === true) {
            const user = { email: req.body.email };
            const accessToken = jwt.sign(user, process.env.ACCESS_TOKEN_SECRET);
            res.json({ accessToken: accessToken });
          } else res.status(400).json("Not Allowed");
        })
        .catch((err) => {
          res.status(400).json(err);
        });
    })
    .catch((err) => {
      res.status(400).json("User Not Found");
    });
};

module.exports = { get, register, login, delete_one };
