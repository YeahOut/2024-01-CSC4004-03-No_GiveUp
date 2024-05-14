const timer = document.querySelector(".timer-js-timer");
const toggleBtn = document.querySelector("recording_button");

let TIME = 0;
let cron; // setInterval을 위한 변수
let isTimerRunning = false;

function toggleTimer() {
  if (isTimerRunning) {
    stopTimer();
  } else {
    startTimer();
  }
}

function startTimer() {
  updateTimer();
  cron = setInterval(updateTimer, 1000);
  isTimerRunning = true;
  toggleBtn.innerText = "Stop Timer";
  timer.classList.add("hide");
}

function stopTimer() {
  clearInterval(cron);
  isTimerRunning = false;
  toggleBtn.innerText = "Start Timer";
  timer.classList.remove("hide");
}

function updateTimer() {
  const hours = Math.floor(TIME / 3600);
  const checkMinutes = Math.floor(TIME / 60);
  const seconds = TIME % 60;
  const minutes = checkMinutes % 60;

  timer.innerText = `${hours < 10 ? `0${hours}` : hours}:${
    minutes < 10 ? `0${minutes}` : minutes
  }:${seconds < 10 ? `0${seconds}` : seconds}`;
  TIME++;
}

toggleBtn.addEventListener("click", toggleTimer);
