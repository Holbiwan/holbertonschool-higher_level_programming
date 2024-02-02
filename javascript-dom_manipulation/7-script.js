document.addEventListener('DOMContentLoaded', () => {
  const listMoviesElement = document.getElementById('list_movies');
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => data.results.forEach(movie => {
      listMoviesElement.appendChild(
        Object.assign(document.createElement('li'), { textContent: movie.title })
      );
    }))
    .catch(error => console.error('Error obtaining data:', error));
});
