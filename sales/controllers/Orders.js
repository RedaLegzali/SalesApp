const Order = require("../models/Order");

const get = (req, res) => {
  Order.find({ user: req.user.email })
    .then((data) => {
      res.json(data);
    })
    .catch((err) => {
      res.status(400).json(err);
    });
};

const get_id = (req, res) => {
  Order.findOne({ user: req.user.email, _id: req.params.id })
    .then((data) => {
      res.json(data);
    })
    .catch((err) => {
      res.status(400).json(err);
    });
};

const post = (req, res) => {
  const order = new Order({
    user: req.user.email,
    skus: req.body.skus,
    price: req.body.price,
  });
  order
    .save()
    .then((data) => {
      res.json(data);
    })
    .catch((err) => {
      res.status(400).json(err);
    });
};

const delete_many = (req, res) => {
  Order.deleteMany({ user: req.user.email })
    .then((data) => {
      res.json(data);
    })
    .catch((err) => {
      res.status(400).json(err);
    });
};

const delete_one = (req, res) => {
  Order.deleteOne({ user: req.user.email }, { _id: req.params.id })
    .then((data) => {
      res.json(data);
    })
    .catch((err) => {
      res.status(400).json(err);
    });
};

module.exports = { get, get_id, post, delete_many, delete_one };
