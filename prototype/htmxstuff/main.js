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

home = new Place("home", "home", ["school"], []);
school = new Place("school", "school", ["home"], []);

p_map = {
  home: home,
  school: school,
};

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

async function view(info) {
  function getUserInput() {
    return document.getElementById("userInput").value;
  }

  function updateView(info) {
    document.getElementById("userInput").value = "";
    document.getElementById("output").innerHTML = info;
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

  updateView(info);
  // console.log(info);
  await waitForButtonClick();
  return getUserInput();
}

async function changeCurrentPlace(time, currentPlace) {
  let out = `available neighbors:<br>`;
  for (let i = 0; i < currentPlace.neighbors.length; i++) {
    out += `${i}. ${p_map[currentPlace.neighbors[i]].name}.<br>`;
  }

  let choice = await view(out);

  if (
    !isNaN(choice) &&
    parseInt(choice) >= 0 &&
    parseInt(choice) <= currentPlace.neighbors.length - 1
  ) {
    let chosen_neighbor = currentPlace.neighbors[parseInt(choice)];
    currentPlace = p_map[chosen_neighbor];
  } else {
    await view("Invalid neighbor choice.", "red");
  }

  return currentPlace;
}

async function main() {
  time = 0;
  place = home;

  await view("welcome to the game, do anything here!");
  
  while (true) {
    text = await view(`it is day ${time}<br>
you are in ${place.name}<br>
available actions:<br>
0. rest<br>
1. move<br>
2. events<br>
`);
    if (text == "quit") {
      await view("thank you for playing");
      break;
    } else if (text == "0") {
    } else if (text == "1") {
      place = await changeCurrentPlace(time, place);
    }
    time += 1;
    console.log(`day ${time}`);
  }
}

main();
