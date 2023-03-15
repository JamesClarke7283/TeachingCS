// A method which takes id as a parameter and edits the todo item by using the fetch api to send a request to the /edit endpoint with the id as a POST argument under id and title and todo.
// To get the title and description, insert an edit model and get the values from the input fields.
// the post request uses raw values not json
function editTodoItem(id) {
    let title = document.getElementById("title").value;
    let description = document.getElementById("description").value;
    let todo = document.getElementById("todo").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/edit?id=" + encodeURIComponent(id) + "&title=" + encodeURIComponent(title) + "&description=" + encodeURIComponent(description));
    xhr.send();
}