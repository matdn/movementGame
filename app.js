const express = require('express');
const { PythonShell } = require('python-shell');

const app = express();

app.use(express.static('public'));

app.get('/data', (req, res) => {
  let options = {
    mode: 'text',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: './',
    args: []
  };

  PythonShell.run('script.py', options, (err, result) => {
    if (err) throw err;
    res.send(result);
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));