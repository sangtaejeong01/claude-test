// State variables
let currentProblem = null;
let correctCount = 0;
let incorrectCount = 0;

// DOM elements
const problemDiv = document.getElementById('problem');
const answerInput = document.getElementById('answer');
const feedbackDiv = document.getElementById('feedback');
const correctSpan = document.getElementById('correct');
const incorrectSpan = document.getElementById('incorrect');
const accuracySpan = document.getElementById('accuracy');
const difficultySelect = document.getElementById('difficulty');
const submitBtn = document.getElementById('submit-btn');
const skipBtn = document.getElementById('skip-btn');
const newProblemBtn = document.getElementById('new-problem-btn');
const resetBtn = document.getElementById('reset-btn');

// Operator checkboxes
const opAdd = document.getElementById('op-add');
const opSubtract = document.getElementById('op-subtract');
const opMultiply = document.getElementById('op-multiply');
const opDivide = document.getElementById('op-divide');

// Get random number based on difficulty
function getRandomNumber() {
    const difficulty = difficultySelect.value;
    let max;

    switch(difficulty) {
        case 'easy':
            max = 10;
            break;
        case 'medium':
            max = 50;
            break;
        case 'hard':
            max = 100;
            break;
        default:
            max = 50;
    }

    return Math.floor(Math.random() * max) + 1;
}

// Get selected operators
function getSelectedOperators() {
    const operators = [];
    if (opAdd.checked) operators.push('+');
    if (opSubtract.checked) operators.push('-');
    if (opMultiply.checked) operators.push('×');
    if (opDivide.checked) operators.push('÷');

    return operators;
}

// Generate a new problem
function generateProblem() {
    const operators = getSelectedOperators();

    if (operators.length === 0) {
        alert('최소 하나의 연산자를 선택해주세요!');
        opAdd.checked = true;
        operators.push('+');
    }

    const operator = operators[Math.floor(Math.random() * operators.length)];
    let num1 = getRandomNumber();
    let num2 = getRandomNumber();
    let answer;
    let displayOperator = operator;

    switch(operator) {
        case '+':
            answer = num1 + num2;
            break;
        case '-':
            // Ensure result is positive
            if (num1 < num2) {
                [num1, num2] = [num2, num1];
            }
            answer = num1 - num2;
            break;
        case '×':
            // For multiplication, use smaller numbers
            num1 = Math.floor(num1 / 2) + 1;
            num2 = Math.floor(num2 / 2) + 1;
            answer = num1 * num2;
            break;
        case '÷':
            // For division, ensure clean division
            num2 = Math.max(2, Math.floor(num2 / 2));
            answer = Math.floor(Math.random() * 20) + 1;
            num1 = num2 * answer;
            break;
    }

    currentProblem = {
        num1: num1,
        num2: num2,
        operator: operator,
        answer: answer,
        displayText: `${num1} ${displayOperator} ${num2} = ?`
    };

    displayProblem();
}

// Display the current problem
function displayProblem() {
    problemDiv.textContent = currentProblem.displayText;
    answerInput.value = '';
    answerInput.focus();
    feedbackDiv.textContent = '';
    feedbackDiv.className = 'feedback';
}

// Check the answer
function checkAnswer() {
    const userAnswer = parseInt(answerInput.value);

    if (isNaN(userAnswer)) {
        feedbackDiv.textContent = '숫자를 입력해주세요!';
        feedbackDiv.className = 'feedback incorrect';
        return;
    }

    if (userAnswer === currentProblem.answer) {
        correctCount++;
        feedbackDiv.textContent = `정답입니다! 🎉 (${currentProblem.num1} ${currentProblem.operator} ${currentProblem.num2} = ${currentProblem.answer})`;
        feedbackDiv.className = 'feedback correct';
        setTimeout(() => {
            generateProblem();
        }, 1500);
    } else {
        incorrectCount++;
        feedbackDiv.textContent = `틀렸습니다. 😢 정답은 ${currentProblem.answer}입니다.`;
        feedbackDiv.className = 'feedback incorrect';
        setTimeout(() => {
            generateProblem();
        }, 2500);
    }

    updateStats();
}

// Skip the current problem
function skipProblem() {
    feedbackDiv.textContent = `정답은 ${currentProblem.answer}입니다.`;
    feedbackDiv.className = 'feedback incorrect';
    incorrectCount++;
    updateStats();

    setTimeout(() => {
        generateProblem();
    }, 2000);
}

// Update statistics
function updateStats() {
    correctSpan.textContent = correctCount;
    incorrectSpan.textContent = incorrectCount;

    const total = correctCount + incorrectCount;
    const accuracy = total > 0 ? Math.round((correctCount / total) * 100) : 0;
    accuracySpan.textContent = `${accuracy}%`;
}

// Reset statistics
function resetStats() {
    if (confirm('통계를 초기화하시겠습니까?')) {
        correctCount = 0;
        incorrectCount = 0;
        updateStats();
        generateProblem();
    }
}

// Event listeners
submitBtn.addEventListener('click', checkAnswer);
skipBtn.addEventListener('click', skipProblem);
newProblemBtn.addEventListener('click', generateProblem);
resetBtn.addEventListener('click', resetStats);

answerInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        checkAnswer();
    }
});

// Change difficulty or operators
difficultySelect.addEventListener('change', generateProblem);
opAdd.addEventListener('change', () => {
    if (getSelectedOperators().length > 0) generateProblem();
});
opSubtract.addEventListener('change', () => {
    if (getSelectedOperators().length > 0) generateProblem();
});
opMultiply.addEventListener('change', () => {
    if (getSelectedOperators().length > 0) generateProblem();
});
opDivide.addEventListener('change', () => {
    if (getSelectedOperators().length > 0) generateProblem();
});

// Initialize with first problem
generateProblem();
