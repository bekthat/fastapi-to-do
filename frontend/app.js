const API_URL = "http://127.0.0.1:8000/todos";

async function loadTodos() {
    const response = await fetch(API_URL);
    const todos = await response.json();
    const todoList = document.getElementById("todo-list");
    todoList.innerHTML = "";

    todos.forEach(todo => {
        const card = document.createElement("div");
        card.className = "bg-white shadow-md rounded-lg p-4 flex flex-col";

        const title = document.createElement("input");
        title.className = "text-lg font-bold border rounded p-1";
        title.value = todo.title;

        const description = document.createElement("textarea");
        description.className = "text-gray-600 border rounded p-1 mt-2";
        description.value = todo.description || "Без описания";

        const completedCheckbox = document.createElement("input");
        completedCheckbox.type = "checkbox";
        completedCheckbox.checked = todo.completed;
        completedCheckbox.className = "mt-2";
        completedCheckbox.onchange = async () => {
            await updateTodo(todo.id, title.value, description.value, completedCheckbox.checked);
        };

        const updateBtn = document.createElement("button");
        updateBtn.className = "mt-2 bg-yellow-500 text-white px-3 py-1 rounded";
        updateBtn.textContent = "Сохранить";
        updateBtn.onclick = async () => {
            await updateTodo(todo.id, title.value, description.value, completedCheckbox.checked);
        };

        const deleteBtn = document.createElement("button");
        deleteBtn.className = "mt-2 bg-red-500 text-white px-3 py-1 rounded";
        deleteBtn.textContent = "Удалить";
        deleteBtn.onclick = async () => {
            await fetch(`${API_URL}/${todo.id}`, { method: "DELETE" });
            loadTodos();
        };

        card.appendChild(title);
        card.appendChild(description);
        card.appendChild(completedCheckbox);
        card.appendChild(updateBtn);
        card.appendChild(deleteBtn);
        todoList.appendChild(card);
    });
}

async function updateTodo(id, title, description, completed) {
    await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description, completed })
    });
    loadTodos();
}

document.getElementById("todo-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description })
    });

    event.target.reset();
    loadTodos();
});

loadTodos();
