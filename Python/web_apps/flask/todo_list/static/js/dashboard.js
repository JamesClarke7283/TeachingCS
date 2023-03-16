// A method which takes id as a parameter and edits the todo item by using the fetch api to send a request to the /edit endpoint with the id as a POST argument under id and title and todo.
// To get the title and description, insert an edit model and get the values from the input fields.
// the post request uses raw values not json
function openEditModal(id, title, description) {
    // Populate the form with the current todo's data
    document.getElementById('edit-todo-id').value = id;
    document.getElementById('edit-todo-title').value = title;
    document.getElementById('edit-todo-description').value = description;

    // Show the modal
    var modal = document.getElementById('edit-todo-modal');
    modal.style.display = 'block';
}


/*
let title = document.getElementById("title").value;
let description = document.getElementById("description").value;
var xhr = new XMLHttpRequest();
xhr.open("POST", "/edit?id=" + encodeURIComponent(id) + "&title=" + encodeURIComponent(title) + "&description=" + encodeURIComponent(description));
xhr.send();
*/