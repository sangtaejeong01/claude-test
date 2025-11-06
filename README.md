# 혼합계산 연습기 (Mixed Calculation Practice)

Interactive application for practicing mixed arithmetic operations.
Available in both web browser and command-line (Python) versions!

## Features

- **Multiple Operations**: Practice addition (+), subtraction (-), multiplication (×), and division (÷)
- **Difficulty Levels**:
  - Easy: Numbers 1-10
  - Medium: Numbers 1-50
  - Hard: Numbers 1-100
- **Customizable**: Select which operations to practice
- **Statistics Tracking**: Track correct answers, incorrect answers, and accuracy percentage
- **Real-time Feedback**: Instant feedback on your answers
- **Responsive Design**: Works on desktop and mobile devices

## How to Use

### Web Version (Browser)

1. Open `index.html` in your web browser
2. Select your preferred difficulty level
3. Choose which operations you want to practice
4. Solve the problems and enter your answer
5. Press Enter or click "제출" (Submit) to check your answer
6. Track your progress with the statistics display

### Python Version (Terminal/Command Line)

1. Run the Python script:
   ```bash
   python3 calculator_practice.py
   ```
   or
   ```bash
   ./calculator_practice.py
   ```

2. Main menu options:
   - **문제 풀기** (Practice): Start solving problems
   - **설정** (Settings): Change difficulty and operators
   - **통계 초기화** (Reset Stats): Clear your statistics
   - **종료** (Exit): Quit the program

3. While practicing:
   - Enter your answer as a number
   - Type `skip` to skip the current problem
   - Type `menu` to return to the main menu

## Features Explained

- **난이도** (Difficulty): Choose between Easy, Medium, or Hard
- **연산자** (Operators): Check/uncheck operations to customize your practice
- **맞은 문제** (Correct): Number of correct answers
- **틀린 문제** (Incorrect): Number of incorrect answers
- **정답률** (Accuracy): Your success rate percentage
- **제출** (Submit): Check your answer
- **건너뛰기** (Skip): Skip current problem
- **새 문제** (New Problem): Generate a new problem
- **통계 초기화** (Reset Stats): Reset all statistics

## Technologies Used

### Web Version
- HTML5
- CSS3 (with Flexbox and responsive design)
- Vanilla JavaScript

### Python Version
- Python 3.x
- Standard library only (no external dependencies required)

## License

Open source - feel free to use and modify!