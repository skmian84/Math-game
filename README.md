# Math Adventure Game

A kid-friendly browser game for practicing **addition** and **subtraction**.

## Features
- Random addition and subtraction questions.
- Score tracking and streak tracking.
- Level system that increases number range every 3 correct answers.
- Friendly design for young learners.

## How to run the game

### Option 1 (quickest): open the file directly
1. In your file explorer, open this project folder.
2. Double-click `index.html`.

### Option 2 (recommended): run a local web server
From a terminal:

```bash
cd /workspace/Math-game
python3 -m http.server 8000
```

Then open this URL in your browser:

- <http://localhost:8000>

## Troubleshooting
- If you still see a blank page, make sure you are opening `http://localhost:8000` (not another port).
- If port 8000 is busy, run:

  ```bash
  python3 -m http.server 8080
  ```

  Then open <http://localhost:8080>.
