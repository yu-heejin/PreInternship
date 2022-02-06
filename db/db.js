const express = require('express');
const db = express();
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

mongoose.connect("mongodb+srv://timmy:tjdskacjdsus@cluster0.pszbu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
.then(()=>console.log('MongoDB Connected...'))
.catch(err=>console.log(err))

db.get('/', (req, res) => {
    res.send("welcome to ghibli world!");
});

db.listen(3000, ()=> {
    console.log("server is running!");
});