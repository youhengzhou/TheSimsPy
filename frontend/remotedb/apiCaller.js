const axios = require("axios");

// Base URL for the API
const baseURL = "http://localhost:3000/api";

// Function to make a POST request to create a new record
async function createRecord(record) {
    try {
        const response = await axios.post(`${baseURL}/records`, record);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

// Function to make a GET request to retrieve all records
async function getAllRecords() {
    try {
        const response = await axios.get(`${baseURL}/records`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

// Function to make a GET request to retrieve a specific record by ID
async function getRecordById(id) {
    try {
        const response = await axios.get(`${baseURL}/records/${id}`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

// Function to make a PUT request to update a record by ID
async function updateRecordById(id, updatedRecord) {
    try {
        const response = await axios.put(
            `${baseURL}/records/${id}`,
            updatedRecord
        );
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

// Function to make a DELETE request to delete a record by ID
async function deleteRecordById(id) {
    try {
        const response = await axios.delete(`${baseURL}/records/${id}`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

// Example usage
async function main() {
    // Create a new record
    const newRecord = { id: 1, name: "John Doe", age: 30 };
    const createdRecord = await createRecord(newRecord);
    console.log("Created Record:", createdRecord);

    // // Retrieve all records
    // const allRecords = await getAllRecords();
    // console.log("All Records:", allRecords);

    // // Retrieve a specific record by ID
    // const recordId = 1;
    // const recordById = await getRecordById(recordId);
    // console.log("Record by ID:", recordById);

    // // Update a record by ID
    // const updatedRecord = { name: "Jane Doe", age: 35 };
    // const updatedRecordById = await updateRecordById(recordId, updatedRecord);
    // console.log("Updated Record:", updatedRecordById);

    // // Delete a record by ID
    // const deletedRecord = await deleteRecordById(recordId);
    // console.log("Deleted Record:", deletedRecord);
}

main();
