document.addEventListener("DOMContentLoaded", function() {
    let mySwiper = new Swiper('.swiper-container', {
        direction: 'horizontal',
        loop: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });

    function hideSuccessMessage() {
        let successMessage = document.getElementById('contact-message-success');
        if (successMessage) {
            setTimeout(function() {
                successMessage.style.display = 'none';
            }, 3000);
        }
    }

    hideSuccessMessage();
});