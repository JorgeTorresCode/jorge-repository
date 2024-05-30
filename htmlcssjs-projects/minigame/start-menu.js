const startMenu = document.querySelector(".start-menu");
const listaPersonajesMenu = document.querySelector(".listapersonajes-menu");
const jugarBtn = document.querySelector(".jugar-btn");
const listaPersonajesBtn = document.querySelector(".listapersonajes-btn");

listaPersonajesBtn.addEventListener("click", ()=> {
    startMenu.style.display = "none";
    listaPersonajesMenu.style.display = "flex";
});

