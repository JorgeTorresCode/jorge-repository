const container = document.querySelector(".container");

function createKey(name, model, price) {
    img = "<img class='key-img' src='key.png'>";
    name = `<h2>${name}</h2>`;
    model = `<h3>${model}</h3>`;
    price = `<p>Price: $${price}</p>`;
    return [img, name, model, price];
}

const changeHidden = (number) => {
    document.querySelector(".keydata").value = number;
}

let fragment = document.createDocumentFragment();

for (let i = 0; i < 20; i++) {
    let randomPrice = Math.round(Math.random()*10000);
    let randomModel = Math.round(Math.random()*1000);
    let key = createKey(`Key ${i + 1}`, `model ${randomModel}`, randomPrice);
    let div = document.createElement("DIV");
    div.tabIndex = i;
    div.addEventListener("click", ()=>{
        document.querySelector(".keydata").value = randomModel;
    });
    div.classList.add(`item-${i}`, 'div');
    div.innerHTML = key[0] + key[1] + key[2] + key[3];
    fragment.appendChild(div);
}

container.appendChild(fragment)

changeHidden