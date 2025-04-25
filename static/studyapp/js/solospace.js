let timer;
let isRunning = false;
let isPaused = false;
let timeRemaining;
let mode = 'pomodoro';

const modes = {
    pomodoro: 25,
    shortBreak: 5,
    longBreak: 15
};

document.getElementById('pomodoro').addEventListener('click', () => setMode('pomodoro'));
document.getElementById('short-break').addEventListener('click', () => setMode('shortBreak'));
document.getElementById('long-break').addEventListener('click', () => setMode('longBreak'));
document.getElementById('start').addEventListener('click', startTimer);
document.getElementById('pause').addEventListener('click', pauseTimer);
document.getElementById('reset').addEventListener('click', resetTimer);

function setMode(newMode) {
    mode = newMode;
    resetTimer();
    document.querySelectorAll('.timer-mode button').forEach(button => button.classList.remove('active'));
    document.getElementById(mode).classList.add('active');
}

function startTimer() {
    if (isRunning) return;
    isRunning = true;
    if (!isPaused) {
        timeRemaining = modes[mode] * 60;
    }
    isPaused = false;
    saveTimerAction('start', timeRemaining);
    timer = setInterval(() => {
        const minutes = Math.floor(timeRemaining / 60);
        const seconds = timeRemaining % 60;
        document.getElementById('minutes').textContent = String(minutes).padStart(2, '0');
        document.getElementById('seconds').textContent = String(seconds).padStart(2, '0');
        timeRemaining--;
        if (timeRemaining < 0) {
            clearInterval(timer);
            isRunning = false;
        }
    }, 1000);
}

function pauseTimer() {
    if (!isRunning) return;
    clearInterval(timer);
    isRunning = false;
    isPaused = true;
    saveTimerAction('pause', timeRemaining);
}

function resetTimer() {
    clearInterval(timer);
    isRunning = false;
    isPaused = false;
    timeRemaining = modes[mode] * 60;
    document.getElementById('minutes').textContent = String(modes[mode]).padStart(2, '0');
    document.getElementById('seconds').textContent = '00';
    saveTimerAction('reset', timeRemaining);
}

// Initialize default mode
setMode('pomodoro');

document.getElementById('addGoalBtn').addEventListener('click', addGoal);

function addGoal() {
    const goalInput = document.getElementById('goalInput');
    const goalText = goalInput.value.trim();

    if (goalText === '') return;

    const goalItem = document.createElement('li');
    goalItem.innerHTML = `
        <span>${goalText}</span>
        <input type="checkbox" class="complete-checkbox">
    `;

    document.getElementById('goalsList').appendChild(goalItem);
    goalInput.value = '';

    goalItem.querySelector('.complete-checkbox').addEventListener('change', () => {
        goalItem.classList.toggle('completed');
        sortGoals();
    });

    saveGoal(goalText);
}

function sortGoals() {
    const goalsList = document.getElementById('goalsList');
    const goals = Array.from(goalsList.children);

    goals.sort((a, b) => {
        if (a.classList.contains('completed') && !b.classList.contains('completed')) return 1;
        if (!a.classList.contains('completed') && b.classList.contains('completed')) return -1;
        return 0;
    });

    goals.forEach(goal => goalsList.appendChild(goal));
}

function saveTimerAction(action, remainingTime) {
    fetch('/save-timer-action/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        body: JSON.stringify({ action, remainingTime, mode })
    });
}

function saveGoal(goalText) {
    fetch('/save-goal/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        body: JSON.stringify({ goalText })
    });
}

function getCsrfToken() {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken'))
        .split('=')[1];
    return cookieValue;
}

let startTime;
        document.getElementById('startStopBtn').addEventListener('click', function() {
            const button = this;
            if (button.textContent === 'Start') {
                startTime = new Date();
                button.textContent = 'Stop';
            } else {
                const endTime = new Date();
                fetch('/save_study_session/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}'
                    },
                    body: JSON.stringify({
                        'start_time': startTime.toISOString(),
                        'end_time': endTime.toISOString()
                    })
                }).then(response => {
                    if (response.ok) {
                        button.textContent = 'Start';
                        alert('Study session saved!');
                    }
                });
            }
        });