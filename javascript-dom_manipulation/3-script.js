document.addEventListener('DOMContentLoaded', () => {
    const toggleHeader = document.getElementById('toggle_header');
    const header = document.querySelector('header');

    toggleHeader.addEventListener('click', () => {
        header.classList.toggle('red');
        header.classList.toggle('green');
        console.log(header);
    });
});
