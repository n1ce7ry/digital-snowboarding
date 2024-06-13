const container = document.querySelector(".container");
const seats = document.querySelectorAll(".row .seat:not(.sold)");
const count = document.getElementById("count");
const total = document.getElementById("total");
const payment = document.getElementById("payment");
const quantity = document.getElementById('seat_data')
const movieSelect = document.getElementById("movie");

populateUI();

let ticketPrice = +movieSelect.value;


function setMovieData(movieIndex, moviePrice) {
  localStorage.setItem("selectedMovieIndex", movieIndex);
  localStorage.setItem("selectedMoviePrice", moviePrice);
}


function updateSelectedCount() {
  const selectedSeats = document.querySelectorAll(".row .seat.selected");

  const seatsIndex = [...selectedSeats].map((seat) => [...seats].indexOf(seat));

  localStorage.setItem("selectedSeats", JSON.stringify(seatsIndex));

  const selectedSeatsCount = selectedSeats.length;

  count.innerText = selectedSeatsCount;
  total.innerText = selectedSeatsCount * ticketPrice;
  payment.innerText = selectedSeatsCount * ticketPrice;

  const selectedDivs = document.querySelectorAll('.selected');
    const seatInfoValues = Array.from(selectedDivs).map(div => {
    const seatInfo = div.getAttribute('data-seat-info');
    return seatInfo ? seatInfo.trim() : null;
  }).filter(value => value !== null);

  quantity.value = seatInfoValues;

  setMovieData(movieSelect.selectedIndex, movieSelect.value);
}


function populateUI() {
  const selectedSeats = JSON.parse(localStorage.getItem("selectedSeats"));

  if (selectedSeats !== null && selectedSeats.length > 0) {
    seats.forEach((seat, index) => {
      if (selectedSeats.indexOf(index) > -1) {
        console.log(seat.classList.add("selected"));
      }
    });
  }

  const selectedMovieIndex = localStorage.getItem("selectedMovieIndex");

  if (selectedMovieIndex !== null) {
    movieSelect.selectedIndex = selectedMovieIndex;
    console.log(selectedMovieIndex)
  }
}
console.log(populateUI())

movieSelect.addEventListener("change", (e) => {
  ticketPrice = +e.target.value;
  setMovieData(e.target.selectedIndex, e.target.value);
  updateSelectedCount();
});


container.addEventListener("click", (e) => {
  if (
    e.target.classList.contains("seat") &&
    !e.target.classList.contains("sold")
  ) {
    e.target.classList.toggle("selected");

    updateSelectedCount();
  }
});

updateSelectedCount();


document.addEventListener('DOMContentLoaded', function() {
  var selectElement = document.getElementById('movie');
  var gameIDField = document.getElementsByName('game_id')[0];

  function updateGameId() {
      var selectedOption = selectElement.options[selectElement.selectedIndex];
      var gameDayId = selectedOption.getAttribute('data-game-id');
      gameIDField.value = gameDayId;
  }

  updateGameId();

  selectElement.addEventListener('change', updateGameId);
});