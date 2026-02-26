const scoreEl = document.getElementById("score");
const streakEl = document.getElementById("streak");
const levelEl = document.getElementById("level");
const problemEl = document.getElementById("problem");
const answerInput = document.getElementById("answer");
const messageEl = document.getElementById("message");
const answerForm = document.getElementById("answer-form");
const newProblemBtn = document.getElementById("new-problem");
const resetGameBtn = document.getElementById("reset-game");

const gameState = {
  score: 0,
  streak: 0,
  level: 1,
  currentAnswer: 0,
};

function randomInt(maxInclusive) {
  return Math.floor(Math.random() * (maxInclusive + 1));
}

function createProblem() {
  const max = gameState.level * 5;
  const useAddition = Math.random() >= 0.5;
  let a = randomInt(max);
  let b = randomInt(max);

  if (!useAddition && b > a) {
    [a, b] = [b, a];
  }

  const operator = useAddition ? "+" : "-";
  gameState.currentAnswer = useAddition ? a + b : a - b;
  problemEl.textContent = `${a} ${operator} ${b}`;
}

function updateStats() {
  scoreEl.textContent = gameState.score;
  streakEl.textContent = gameState.streak;
  levelEl.textContent = gameState.level;
}

function setMessage(text, type = "") {
  messageEl.textContent = text;
  messageEl.className = "message";
  if (type) {
    messageEl.classList.add(type);
  }
}

function levelUpIfNeeded() {
  if (gameState.streak > 0 && gameState.streak % 3 === 0) {
    gameState.level += 1;
    setMessage("Awesome! You leveled up! 🎉", "success");
  }
}

answerForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const playerAnswer = Number(answerInput.value);

  if (Number.isNaN(playerAnswer)) {
    setMessage("Please type a number.", "error");
    return;
  }

  if (playerAnswer === gameState.currentAnswer) {
    gameState.score += 10;
    gameState.streak += 1;
    levelUpIfNeeded();
    if (gameState.streak % 3 !== 0) {
      setMessage("Great job! That's correct! ✅", "success");
    }
  } else {
    gameState.streak = 0;
    setMessage(`Nice try! The answer was ${gameState.currentAnswer}.`, "error");
  }

  updateStats();
  createProblem();
  answerInput.value = "";
  answerInput.focus();
});

newProblemBtn.addEventListener("click", () => {
  createProblem();
  setMessage("Here's a new one!");
  answerInput.focus();
});

resetGameBtn.addEventListener("click", () => {
  gameState.score = 0;
  gameState.streak = 0;
  gameState.level = 1;
  updateStats();
  createProblem();
  setMessage("Game reset. Let's play! 🚀");
  answerInput.value = "";
  answerInput.focus();
});

updateStats();
createProblem();
answerInput.focus();
