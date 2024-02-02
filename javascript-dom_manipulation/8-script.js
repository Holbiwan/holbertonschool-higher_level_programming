document.addEventListener("DOMContentLoaded", function() {
    var helloElement = document.getElementById("hello");
    var apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

    fetch(apiUrl)
      .then(response => response.text())
      .then(data => {
        helloElement.textContent = data;
      })
      .catch(error => {
        console.error("Error obtaining translation:", error);
      });
});
