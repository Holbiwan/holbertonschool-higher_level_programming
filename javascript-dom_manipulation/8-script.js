document.addEventListener('DOMContentLoaded', function () {
  const helloElement = document.getElementById('hello');
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      helloElement.innerText = data.hello;
    })
    .catch(error => {
      console.error('Error obtaining translation:', error);
    });
});
