document.addEventListener('DOMContentLoaded', function() {
    const deletePostModal = new bootstrap.Modal(document.getElementById('deletePostModal'));
    const deleteCommentModal = new bootstrap.Modal(document.getElementById('deleteCommentModal'));
    const confirmDeletePost = document.getElementById('confirm-post-delete');
    const confirmDeleteComm = document.getElementById('confirm-comm-delete');

    // Delete Post
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-btn') && !event.target.classList.contains('delete-comm-btn')) {
            const postId = event.target.getAttribute('post_id');
            confirmDeletePost.onclick = function() {
                window.location.href = `delete_post/${postId}`;
            };
            deletePostModal.show();
        }
    });

    //Delete Comment
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-comm-btn')) {
            const commentId = event.target.getAttribute('comment_id');
            confirmDeleteComm.onclick = function() {
                window.location.href = `delete_comment/${commentId}`;
            };
            deleteCommentModal.show();
        }
    });

   
    window.onload = function() {
        const messages = document.querySelector('.messages');
        if (messages) {
            messages.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    };

    document.querySelectorAll('.btn-close, .btn-secondary').forEach(function(cancelButton) {
        cancelButton.addEventListener('click', function() {
            if (deletePostModal._isShown) {
                deletePostModal.hide();
            }
            if (deleteCommentModal._isShown) {
                deleteCommentModal.hide();
            }
        });
    });
});
