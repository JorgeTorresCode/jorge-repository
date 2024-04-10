"use strict";

const zone = document.querySelector(".zone");

const textureChange = (n, e) => {
    e.dataTransfer.setData("texture", n.toString());
};

zone.addEventListener("dragover", (e) => {
    e.preventDefault();
});

zone.addEventListener("drop", (e) => {
    let n = e.dataTransfer.getData("texture");
    zone.style.background = `url("texture-${n}.jpg")`;
});

for (let i = 1; i < document.querySelector(".textures").children.length + 1; i++) {
    document.querySelector(`.texture-${i}`).addEventListener("dragstart", (e) => textureChange(i, e));
}