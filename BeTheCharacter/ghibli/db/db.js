const express = require('express')
const db = express()
const bodyParser = require('body-parser')
const mongoose = require('mongoose')
require('./img')

db.use(bodyParser.json())

const img = mongoose.model("imgs2")

mongoose.connect("mongodb+srv://timmy:tjdskacjdsus@cluster0.pszbu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
.then(()=>console.log('MongoDB Connected...'))
.catch(err=>console.log(err))

db.get('/', (req, res) => {
    img.find({}).then(data=>{
        res.send(data)
    }).catch(err=>{
        console.log(err)
    })
    //res.send("welcome to ghibli world!")
})

db.post('/send-data', (req, res) => {
    //console.log(req.body)
    const imgDB = new img({
        picture: req.body.picture,
        result: req.body.result
    })
    imgDB.save().then(data => {
        console.log(data)
        res.send(data)
    }).catch(err => {
        console.log(err)
    })
    //res.send("posted")
})

db.post('/delete', (req, res) => {
    img.findByIdAndDelete(req.body._id)
    .then(data => {
        console.log(data)
        res.send(data)
    }).catch(err => {
        console.log(err)
    })
})

db.post('/update', (req, res) => {
    img.findByIdAndUpdate(req.body.id, {
        change: req.body.change,
        notChange: req.body.notChange
    }).then(data => {
        console.log(data)
        res.send(data)
    }).catch(err => {
        console.log(err)
    })
})

db.listen(3000, ()=> {
    console.log("server is running!")
})