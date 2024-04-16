document.addEventListener('DOMContentLoaded', function() {
    const deleteButton = document.querySelector('.delete-btn');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));

   
    deleteButton.addEventListener('click', function() {
        deleteModal.show();
    });

    const editButtons = document.getElementsByClassName("edit-comm-btn");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitBtn");
    const commentBody = document.getElementById("id_content");

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
 });
    