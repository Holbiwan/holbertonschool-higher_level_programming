document.addEventListener('DOMContentLoaded', function () {
    const characterElement = document.getElementById('character');
    const apiURL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

    fetch(apiURL)
        .then(response => response.json())
        .then(data => {
            characterElement.textContent = data.name;
        })
        .catch(error => console.error('Error obtaining data:', error));
});
