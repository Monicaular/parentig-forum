document.addEventListener("DOMContentLoaded", function() {
    
    const deleteButton = document.querySelector('.delete-btn');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));

   
    deleteButton.addEventListener('click', function() {
        deleteModal.show();
    });
});