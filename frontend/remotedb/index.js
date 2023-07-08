const express = require("express");
const fs = require("fs");
const app = express();
const PORT = 3000;

// Middleware to parse JSON data
app.use(express.json());

// Read data from the JSON file
function readData() {
    const data = fs.readFileSync("data.json");
    return JSON.parse(data);
}

// Write data to the JSON file
function writeData(data) {
    fs.writeFileSync("data.json", JSON.stringify(data, null, 2));
}

// Create a new record
app.post("/api/records", (req, res) => {
    const data = readData();
    const newRecord = req.body;
    data.push(newRecord);
    writeData(data);
    res.status(201).json(newRecord);
});

// Retrieve all records
app.get("/api/records", (req, res) => {
    const data = readData();
    res.json(data);
});

// Retrieve a specific record
app.get("/api/records/:id", (req, res) => {
    const data = readData();
    const record = data.find((r) => r.id === parseInt(req.params.id));
    if (record) {
        res.json(record);
    } else {
        res.status(404).json({ message: "Record not found" });
    }
});

// Update a record
app.put("/api/records/:id", (req, res) => {
    const data = readData();
    const recordIndex = data.findIndex((r) => r.id === parseInt(req.params.id));
    if (recordIndex !== -1) {
        data[recordIndex] = { ...data[recordIndex], ...req.body };
        writeData(data);
        res.json(data[recordIndex]);
    } else {
        res.status(404).json({ message: "Record not found" });
    }
});

// Delete a record
app.delete("/api/records/:id", (req, res) => {
    const data = readData();
    const recordIndex = data.findIndex((r) => r.id === parseInt(req.params.id));
    if (recordIndex !== -1) {
        const deletedRecord = data.splice(recordIndex, 1);
        writeData(data);
        res.json(deletedRecord[0]);
    } else {
        res.status(404).json({ message: "Record not found" });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
