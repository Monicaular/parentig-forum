document.addEventListener("DOMContentLoaded", function() {
    
    const deleteButton = document.querySelector('.delete-btn');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));

   
    deleteButton.addEventListener('click', function() {
        deleteModal.show();
    });


    function hideLikeMessage() {
        let message = document.getElementById("like-message");
        if (message) {
            setTimeout(function() {
                message.style.display = "none";
            }, 3000);
        }
    }

    let likeForm = document.getElementById("like-form");
    if (likeForm) {
        likeForm.addEventListener("submit", function() {
            document.getElementById("like-message").style.display = "block";
            hideLikeMessage();
        });
    }

    
    let unlikeForm = document.getElementById("unlike-form");
    if (unlikeForm) {
        unlikeForm.addEventListener("submit", function() {
            document.getElementById("like-message").style.display = "block";
            hideLikeMessage();
        });
    }
});