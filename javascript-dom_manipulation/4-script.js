document.addEventListener("DOMContentLoaded", () => {
    const addItemElement = document.getElementById("add_item");
    const myList = document.querySelector(".my_list");

    addItemElement.addEventListener("click", () => myList.appendChild(document.createElement("li")).textContent = "Item");
});
