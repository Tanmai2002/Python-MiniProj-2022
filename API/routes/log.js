const Log = require("../models/Log");
const router = require("express").Router();

//CREATE
router.post("/", async (req, res) =>{
    const log = new Log({
      date: req.body.date,
      timeOfSleep: req.body.timeOfSleep,
      quality: req.body.quality
    });

    try{
        const newLog = await log.save();
        res.status(201).json(newLog);
    } catch (err){
        res.status(400).json({ message: err.message});
    }
});

module.exports = router;