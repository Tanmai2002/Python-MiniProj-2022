const mongoose = require("mongoose");

const LogSchema = new mongoose.Schema(
  {
    date: { type: String, required: true},
    timeOfSleep: { type: Number, required: true},
    quality: { type: Number, required: true },
  }
);

module.exports = mongoose.model("Log", LogSchema);