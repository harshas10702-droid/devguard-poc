import express from "express";

const app = express();

app.get("/calc", (req, res) => {
  const result = eval(req.query.input as string); // dangerous: code injection
  res.send(String(result));
});

app.listen(3000);
