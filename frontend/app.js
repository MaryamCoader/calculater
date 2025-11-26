document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('display');
    const historyList = document.getElementById('history-list');
    const clearButton = document.getElementById('clear');
    const equalsButton = document.getElementById('equals');
    const numberButtons = document.querySelectorAll('.number');
    const operatorButtons = document.querySelectorAll('.operator');

    let currentInput = '0';
    let previousInput = '';
    let operation = null;
    let history = [];

    const API_BASE_URL = 'http://127.0.0.1:5000/api/calc'; // Assuming backend runs on 5000

    function updateDisplay() {
        display.textContent = currentInput;
    }

    function addToHistory(entry) {
        history.unshift(entry); // Add to the beginning
        if (history.length > 10) {
            history.pop(); // Keep only last 10
        }
        renderHistory();
    }

    function renderHistory() {
        historyList.innerHTML = '';
        history.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            historyList.appendChild(li);
        });
    }

    async function performCalculation() {
        if (!operation || previousInput === '' || currentInput === '') {
            return;
        }

        const a = parseFloat(previousInput);
        const b = parseFloat(currentInput);

        // Basic validation before sending to backend
        if (isNaN(a) || isNaN(b)) {
            currentInput = 'Error: Invalid input';
            updateDisplay();
            return;
        }

        try {
            const response = await fetch(API_BASE_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ op: operation, a: a, b: b }),
            });

            const data = await response.json();

            if (data.error) {
                currentInput = `Error: ${data.error}`;
            } else {
                currentInput = String(data.result);
                addToHistory(`${previousInput} ${getOperationSymbol(operation)} ${currentInput} = ${data.result}`);
            }
        } catch (error) {
            currentInput = 'Error: Network or server issue';
            console.error('Calculation error:', error);
        }

        operation = null;
        previousInput = '';
        updateDisplay();
    }

    function getOperationSymbol(op) {
        switch(op) {
            case 'add': return '+';
            case 'subtract': return '-';
            case 'multiply': return '*';
            case 'divide': return '/';
            case 'modulo': return '%';
            case 'power': return '^';
            default: return '';
        }
    }

    numberButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (currentInput === '0' || currentInput.startsWith('Error')) {
                currentInput = button.textContent;
            } else {
                currentInput += button.textContent;
            }
            updateDisplay();
        });
    });

    operatorButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (currentInput.startsWith('Error')) {
                currentInput = '0';
            }
            if (operation && previousInput !== '') { // If an operation was already selected, calculate first
                performCalculation();
            }
            operation = button.dataset.op;
            previousInput = currentInput;
            currentInput = '0'; // Reset current input for the next number
        });
    });

    clearButton.addEventListener('click', () => {
        currentInput = '0';
        previousInput = '';
        operation = null;
        updateDisplay();
    });

    equalsButton.addEventListener('click', () => {
        performCalculation();
    });

    updateDisplay(); // Initialize display
    renderHistory(); // Initialize history display
});
