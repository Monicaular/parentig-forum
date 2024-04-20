document.addEventListener('DOMContentLoaded', function() {
    const deleteButton = document.querySelector('.delete-btn');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));

    const editButtons = document.getElementsByClassName("edit-comm-btn");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitBtn");
    const commentBody = document.getElementById("id_content");

    const deleteCommentModal = new bootstrap.Modal(document.getElementById("delete-modal"));
    const deleteCommentButtons = document.getElementsByClassName('delete-comm-btn');
    const confirmDeleteComm = document.getElementById('confirm-delete');

    deleteButton.addEventListener('click', function() {
        deleteModal.show();
    });

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("comment_id");
            let commentContent = document.getElementById(`comment${commentId}`).innerText;
            commentBody.value = commentContent;
            submitButton.innerText = "Update";
            commentForm.setAttribute("action", `edit_comment/${commentId}`);
        });
    }

    let messageContainer = document.querySelector('.message-container');
        if (messageContainer) {
            let successMessages = messageContainer.querySelectorAll('.success-message');
            successMessages.forEach(function(message) {
                setTimeout(function() {
                    message.style.display = 'none';
                }, 3000);
            });
        }

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
    