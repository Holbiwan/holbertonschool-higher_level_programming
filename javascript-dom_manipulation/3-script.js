document.addEventListener('DOMContentLoaded', function () {
    var toggleHeader = document.getElementById('toggle_header');
    var header = document.querySelector('header');

    toggleHeader.addEventListener('click', function () {
        header.classList.toggle('red');
        header.classList.toggle('green');
        console.log(header);
    });
});
