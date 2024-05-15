document.addEventListener('DOMContentLoaded', function() {
    const deleteButton = document.querySelector('.delete-btn');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));

    deleteButton.addEventListener('click', function() {
        deleteModal.show();
    });

    window.onload = function() {
        const messages = document.querySelector('.messages');
        if (messages) {
            messages.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    };
 });


const deleteCommentModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
const confirmDeleteComm = document.getElementById('confirm-delete');

 document.addEventListener('click', function(event) {
    if (event.target.classList.contains('delete-comm-btn')) {
        const commentId = event.target.getAttribute('comment_id');
        confirmDeleteComm.onclick = function() {
            window.location.href = `delete_comment/${commentId}`;
        };
        deleteCommentModal.show();
    }
});