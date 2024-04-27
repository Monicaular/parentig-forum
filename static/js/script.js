document.addEventListener('DOMContentLoaded', function() {
    const deleteButton = document.querySelector('.delete-btn');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));


    const deleteCommentModal = new bootstrap.Modal(document.getElementById("delete-modal"));
    const deleteCommentButtons = document.getElementsByClassName('delete-comm-btn');
    const confirmDeleteComm = document.getElementById('confirm-delete');

    deleteButton.addEventListener('click', function() {
        deleteModal.show();
    });


    for (let button of deleteCommentButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("comment_id");
            confirmDeleteComm.addEventListener("click", function() {
                window.location.href = `delete_comment/${commentId}`;
            });
            deleteCommentModal.show();
        });
    }
 });