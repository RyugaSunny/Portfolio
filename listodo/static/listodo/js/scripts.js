const taskForm = document.getElementById('taskForm');
const taskInput = document.getElementById('taskInput');
const dateInput = document.getElementById('dateInput');
const taskList = document.getElementById('taskList');

taskForm.addEventListener('submit', addTask);

function addTask(event) {
  event.preventDefault();
  const taskText = taskInput.value;
  const taskDate = dateInput.value;

  if (taskText === '' || taskDate === '') {
    return;
  }

  const taskItem = document.createElement('li');
  const taskTextSpan = document.createElement('span');
  taskTextSpan.innerText = taskText;
  taskTextSpan.classList.add('task-text');

  const taskDateSpan = document.createElement('span');
  taskDateSpan.innerText = taskDate;
  taskDateSpan.classList.add('task-date');

  const buttonWrapper = document.createElement('div');
  buttonWrapper.classList.add('button-wrapper');

  const completeBtn = document.createElement('button');
  completeBtn.innerHTML = '&#x2713;';
  completeBtn.className = 'complete-btn';
  completeBtn.addEventListener('click', completeTask);

  const deleteBtn = document.createElement('button');
  deleteBtn.innerHTML = '&times;';
  deleteBtn.className = 'delete-btn';
  deleteBtn.addEventListener('click', deleteTask);

  buttonWrapper.appendChild(completeBtn);
  buttonWrapper.appendChild(deleteBtn);

  taskItem.appendChild(buttonWrapper);
  taskItem.appendChild(taskTextSpan);
  taskItem.appendChild(document.createElement('br'));
  taskItem.appendChild(taskDateSpan);
  taskList.appendChild(taskItem);

  taskInput.value = '';
  dateInput.value = '';
}

function deleteTask(event) {
  const taskItem = event.target.parentNode.parentNode;
  taskList.removeChild(taskItem);
}

function completeTask(event) {
  const taskItem = event.target.parentNode.parentNode;
  taskItem.classList.toggle('completed');
}
