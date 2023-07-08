const express = require("express");
const cors = require("cors");
const JDB = require("jsoneng");
const app = express();
const db = new JDB("./jdb");

app.use(express.json());
app.use(cors());

app.post("/create", async (req, res) => {
  try {
    await db.create(req.body, req.query.dirname);
    res.status(200).send("Data created successfully");
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.get("/read", async (req, res) => {
  try {
    const data = await db.read(req.query.dirname);
    res.status(200).json(data);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.put("/update", async (req, res) => {
  try {
    await db.update(req.body, req.query.dirname);
    res.status(200).send("Data updated successfully");
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.patch("/patch", async (req, res) => {
  try {
    await db.patch(req.body, req.query.dirname);
    res.status(200).send("Data patched successfully");
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.delete("/delete", async (req, res) => {
  try {
    await db.delete(req.query.dirname);
    res.status(200).send("Data deleted successfully");
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.listen(3000, () =>
  console.log("The jsoneng API wrapper is running on port 3000")
);
