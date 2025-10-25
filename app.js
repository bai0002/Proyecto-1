// app.js
const express = require('express');
const app = express();

// Ruta principal
app.get('/', (req, res) => {
  res.send('<h1>Hello, World!</h1>');
});

// Iniciar servidor
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor escuchando en http://localhost:${PORT}`);
});
