// === 11 - JavaScript and HTML Tasks ===

// Global variables
const totalTables = 10;
let bookedTables = 6;
const bookings = [];

// Task 2: Check Availability
function checkAvailability() {
  let available = totalTables - bookedTables;
  let counterElement = document.getElementById("availability-counter");
  counterElement.innerHTML = "Available tables: " + available;
}

// Task 3: Book a Table
function bookTable() {
  let fname = document.getElementById("fname").value;
  let lname = document.getElementById("lname").value;
  let email = document.getElementById("email").value;
  let date = document.getElementById("date").value;

  let booking = {
    firstName: fname,
    lastName: lname,
    email: email,
    date: date
  };

  bookings.push(booking);
  bookedTables++;
  alert("Booking confirmed for " + fname + " " + lname);
}

// Task 4: Search for a Booking
function findBooking() {
  let userEmail = document.getElementById("booking-email").value;
  let found = false;

  for (let i = 0; i < bookings.length; i++) {
    if (bookings[i].email === userEmail) {
      alert("Booking found: " + bookings[i].firstName + " " + bookings[i].lastName + " on " + bookings[i].date);
      found = true;
    }
  }

  if (!found) {
    alert("No booking found for that email.");
  }
}
