const express = require('express');
const { PythonShell } = require('python-shell');
const cors = require('cors')
const bodyParser = require('body-parser');
const app = express();
const http = require('http');
const server = http.createServer(app);
const path = require('path');
const puppeteer = require('puppeteer');

const { Server } = require("socket.io");


let i = 0
let color = [0,0,0]

function jump(){
  if(character.classList == "animate"){return}
  character.classList.add("animate");
  setTimeout(function(){
      character.classList.remove("animate");
  },300);
} 

app.use(express.static('public'));
app.use(cors())

app.get('/jump', (req, res) => {
  io.emit('jump', null);
  res.send('Données reçues !');
});

app.listen(3000, () => {
  console.log('Serveur en écoute sur le port 3000...');
});

const io = new Server(3001,{
  cors: {origin:'*',}
});
io.on('connection', function (socket) {
  console.log('User connected');
  
})


// const PORT = process.env.PORT || 3000;
// app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));




