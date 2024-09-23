document.getElementById('add-task-btn').addEventListener('click', function() {
    const taskText = document.getElementById('new-task').value;
    if (taskText === '') return;

    const newTask = document.createElement('li');
    newTask.textContent = taskText;

    const removeBtn = document.createElement('button');
    removeBtn.textContent = 'Remove';
    removeBtn.addEventListener('click', function() {
        newTask.remove();
    });

    newTask.appendChild(removeBtn);

    newTask.addEventListener('click', function() {
        newTask.classList.toggle('completed');
    });

    document.getElementById('todo-list').appendChild(newTask);
    document.getElementById('new-task').value = '';
});
