const express = require("express");
const router = express.Router();
const orders = require("../controllers/Orders");
const auth = require("../controllers/Auth");

router.get("/", auth, orders.get);

router.get("/:id", auth, orders.get_id);

router.post("/", auth, orders.post);

router.delete("/", auth, orders.delete_many);

router.delete("/:id", auth, orders.delete_one);

module.exports = router;
