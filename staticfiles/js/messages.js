$(document).ready(function() {
    let hasVisibleMessages = $('#messageModal .modal-body p').filter(function() {
        return $.trim($(this).text()).length > 0;
    }).length > 0;

    if (hasVisibleMessages) {
        $('#messageModal').modal('show');
        setTimeout(function() {
            $('#messageModal').modal('hide');
        }, 5000);
    }
});
