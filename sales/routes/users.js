const express = require("express");
const router = express.Router();
const users = require("../controllers/Users");
const auth = require("../controllers/Auth");

router.get("/", auth, users.get);

router.post("/register", users.register);

router.delete("/", auth, users.delete_one);

router.post("/login", users.login);

module.exports = router;
