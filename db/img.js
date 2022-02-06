const mongoose = require('mongoose')

const ImgSchema = new mongoose.Schema({
    change: String,
    notchange: String
    //url is a String type
})

mongoose.model("imgs2", ImgSchema);