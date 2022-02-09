const mongoose = require('mongoose')

const ImgSchema = new mongoose.Schema({
    picture: String,
    result: String
})

mongoose.model("imgs2", ImgSchema);