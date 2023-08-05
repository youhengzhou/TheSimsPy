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

async function view(info) {
  updateView(info);
  await waitForButtonClick();
  return getUserInput();
}

async function main() {
  time = 0;
  place = new Place("test", "test", []);

  await view("welcome to the game, do anything here!");
  while (true) {
    text = await view(`it is day ${time}
you are in the ${place.name}
available actions:
0. rest
1. move
2. events
`);
    if (text == "quit") {
      await view("thank you for playing");
      break;
    } else if (text == "0") {
    } else if (text == "1") {
      await view("ok");
    }
    console.log("Update action performed");
  }
}

main();
