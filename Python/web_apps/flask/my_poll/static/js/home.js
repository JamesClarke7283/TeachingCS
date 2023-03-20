function openNewPollModal() {
    // Show the modal
    var modal = document.getElementById('new-poll-modal');
    modal.style.display = 'block';
}

// Display the modal if the poll_id is set as a cookie
function displayModal() {
    var cookies = document.cookie;
    if (cookies) {
        openNewPollModal();
    }
}

// Check every 300ms if the poll_id cookie is set
// If it is, display the modal
setInterval(function() {
    displayModal();
}, 300);