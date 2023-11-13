// server.js

const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/order', (req, res) => {
    const { size, type, cup } = req.body;

    const pythonProcess = spawn('python', ['coffee_bot.py', size, type, cup]);

    pythonProcess.stdout.on('data', (data) => {
        const result = data.toString().trim();
        res.json({ result });
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python Error: ${data}`);
        res.status(500).json({ error: 'Internal Server Error' });
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
