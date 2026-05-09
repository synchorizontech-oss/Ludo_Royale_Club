const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send("Ludo Royale Club backend is running!");
});

app.listen(PORT, () => console.log(`Running on ${PORT}`));
