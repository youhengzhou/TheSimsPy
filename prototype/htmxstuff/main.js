class Event {
  constructor(key, desc, action) {
    this.key = key;
    this.desc = desc;
    this.action = action;
  }
}

class Place {
  constructor(key, name, neighbors, events) {
    this.key = key;
    this.name = name;
    this.neighbors = neighbors;
    this.events = events;
  }
}

// function handleKeyPress(event) {
//   if (event.keyCode === 13) {
//     // Check if the pressed key is Enter (key code 13)
//     updateDiv();
//   }
// }

// function updateDiv(info) {
//   const userInput = document.getElementById("userInput").value;
//   document.getElementById("output").textContent = userInput;
// }

function getUserInput() {
  return document.getElementById("userInput").value;
}

function updateView(info) {
  document.getElementById("output").textContent = info;
}

function waitForButtonClick() {
  return new Promise(function (resolve) {
    const button = document.getElementById("userInputButton");
    const input = document.getElementById("userInput");

    let isClicking = false;

    const clickHandler = function () {
      isClicking = true;
      resolve();
    };

    const keyHandler = function (event) {
      if (event.key === "Enter" && !isClicking) {
        isClicking = true;
        button.click();
        resolve();
      }
    };

    button.addEventListener("click", clickHandler);
    input.addEventListener("keydown", keyHandler);
  });
}

async function update() {
  updateView("welcome to the game, do anything here!");
  while (true) {
    await waitForButtonClick();
    // Perform your update action here

    text = getUserInput();
    updateView(text);
    console.log("Update action performed");
  }
}

update();
