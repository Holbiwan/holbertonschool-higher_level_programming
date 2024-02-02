document.addEventListener("DOMContentLoaded", function() {
    const helloElement = document.getElementById("hello");
    const apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

    fetch(apiUrl)
      .then(response => response.json())  // Change this line to parse the response as JSON
      .then(data => {
        helloElement.innerText = data.hello;  // Access the 'hello' property in the JSON data
      })
      .catch(error => {
        console.error("Error obtaining translation:", error);
      });
});
