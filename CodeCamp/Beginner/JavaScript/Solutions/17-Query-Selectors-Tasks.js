// === 17 - Query Selectors Tasks ===

// Task 1: Change a Heading
let title = document.querySelector("#title");
title.innerHTML = "New Title Text";

// Task 2: Style a Button on Click
function styleButton() {
  let btn = document.querySelector("button");
  btn.style.backgroundColor = "coral";
}

// Task 3: Restyle All Paragraphs
let infoParagraphs = document.querySelectorAll(".info");
infoParagraphs.forEach(function(p) {
  p.style.color = "blue";
  p.style.fontSize = "20px";
});

// Task 4: Highlight on Click
function highlightItems() {
  let items = document.querySelectorAll("li");
  items.forEach(function(item) {
    item.style.backgroundColor = "yellow";
  });
}

// Stretch Task: Toggle Styles
let isRed = false;

function toggleStyle() {
  let paragraphs = document.querySelectorAll(".info");
  paragraphs.forEach(function(p) {
    if (isRed) {
      p.style.color = "black";
    } else {
      p.style.color = "red";
    }
  });
  isRed = !isRed;
}
