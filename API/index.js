const express = require('express');
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const userRoute = require("./routes/user");
const authRoute = require("./routes/auth");
const productRoute = require("./routes/product");
const cartRoute = require("./routes/cart");
const orderRoute = require("./routes/order");
const logRoute = require("./routes/log");
const cors=require("cors");
dotenv.config();

mongoose.connect(process.env.MONGO_URL).then(()=>console.log("DB Connection Successfull!")).catch((err)=>{console.log(err)})

app.use(express.json());
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "http://localhost:3000"); // update to match the domain you will make the request from
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });
  app.use(cors())
  ;
app.use("/api/auth", authRoute);
app.use("/api/users", userRoute);
app.use("/api/products", productRoute);
app.use("/api/carts",cartRoute);
app.use("/api/orders", orderRoute);
app.use("/api/logs", logRoute);

app.listen(process.env.PORT || 5001, () => {
    console.log("Backend server is running");
});

