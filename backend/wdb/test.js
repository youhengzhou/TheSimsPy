const axios = require("axios");

const baseURL = "http://localhost:3000";

async function testAPI() {
  try {
    // Test create endpoint
    let response = await axios.post(`${baseURL}/create?dirname=test`, {
      key: "value",
    });
    console.log("Create response:", response.data);

    // Test read endpoint
    response = await axios.get(`${baseURL}/read?dirname=test`);
    console.log("Read response:", response.data);

    // Test update endpoint
    response = await axios.put(`${baseURL}/update?dirname=test`, {
      key: "new value",
    });
    console.log("Update response:", response.data);

    // Test patch endpoint
    response = await axios.patch(`${baseURL}/patch?dirname=test`, {
      newKey: "newValue",
    });
    console.log("Patch response:", response.data);

    // // Test delete endpoint
    // response = await axios.delete(`${baseURL}/delete?dirname=test`);
    // console.log("Delete response:", response.data);
  } catch (error) {
    console.error("Error:", error.response.data);
  }
}

testAPI();
