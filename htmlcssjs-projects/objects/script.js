const objectsHTML = document.querySelector(".objects");
const objectHTML = document.querySelector(".object");

const objects = [
    {
        nameN: "Physics 3",
        noteN: 7
    },
    {
        nameN: "Math 4",
        noteN: 8
    },
    {
        nameN: "Databases 4",
        noteN: 9
    },
    {
        nameN: "Python 3",
        noteN: 7
    }
]

const getObject = (id) => {
    return new Promise((res, rej) => {
        let object = objects[id];
        if (object == undefined) rej("The object doesn't exist");
        else res(object);
    })
}

const showInfo = async () => {
    let obj = [];
    for (let i = 0; i < objects.length; i++) {
        obj[i] = getObject(i);
        obj[i].then(obj => console.log(obj))
    }
}
showInfo()


const fragment = document.createDocumentFragment();

for (let i = 0; i < objects.length; i++) {

    let div = document.createElement("div");
    div.classList.add("object");

    objectsHTML.appendChild(div);

    let nameN = document.createElement("div");
    let noteN = document.createElement("div");

    nameN.classList.add("name");
    nameN.innerHTML = objects[i].nameN;

    noteN.classList.add("note");
    noteN.innerHTML = objects[i].noteN;

    div.appendChild(nameN);
    div.appendChild(noteN);

    fragment.appendChild(div);
}

objectsHTML.appendChild(fragment);