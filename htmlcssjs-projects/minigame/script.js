class Pokemon {
    constructor (_nombre, _velocidad, _ataque) {
        this.nombre = _nombre;
        this.vida = 100;
        this.velocidad = _velocidad;
        this.ataque = _ataque;
    }

    ataquePuno(pk) {
        pk.vida -= this.ataque*0.05;
    }

    ataqueEspada(pk) {
        pk.vida -= this.ataque*0.1;
    }

    ataqueBola(pk) {
        pk.vida -= this.ataque*0.4;
    }
}

const p1 = document.getElementById("p1");
const p2 = document.getElementById("p2");
const p3 = document.getElementById("p3");

const bolita1 = document.getElementById("bolita1");
const bolita2 = document.getElementById("bolita2");

const vida1 = document.getElementById("vida1");
const vida2 = document.getElementById("vida2");

const pokemon1 = document.getElementById("pokemon1");
const pokemon2 = document.getElementById("pokemon2");

let poke1 = new Pokemon("Dereck", 90, 100);
let poke2 = new Pokemon("Jorsh", 95, 85);

let life = false

function handleClick(ataque) {
    p1.style.pointerEvents = "none";
    p2.style.pointerEvents = "none";
    p3.style.pointerEvents = "none";

    if (life) {
        console.log(`${poke2.nombre} is dead`);
        return;
    }

    const threshold = ataque === "p1" ? 0.05 : (ataque === "p2" ? 0.1 : 0.4);
    
    if (poke1.ataque * threshold >= poke2.vida) {
        console.log(`${poke2.nombre} has died`);
        poke2.vida = 0
        life = true;
        return;
    }

    switch (ataque) {
        case "p1":
            poke1.ataquePuno(poke2);
            break;
        case "p2":
            poke1.ataqueEspada(poke2);
            break;
        case "p3":
            poke1.ataqueBola(poke2);
            break;
    }

    console.log(`${poke2.nombre} tiene ${poke2.vida} de vida`);
}

function barraVida() {
    setTimeout(() => {
        bolita1.style.display = "none";
        vida2.style.width = `${poke2.vida}%`;

        p1.style.pointerEvents = "all";
        p2.style.pointerEvents = "all";
        p3.style.pointerEvents = "all";
        if (poke2.vida == 0) {
            vida2.remove();

            pokemon2.style.animation = "none";
            pokemon2.style.transform = "rotate(180deg)";
        }
    }, 700)
}

p1.addEventListener("click", () => {
    handleClick("p1");
    bolita1.style.display = "block";
    bolita1.style.animation = "puno .7s";
    barraVida();
});

p2.addEventListener("click", () => {
    handleClick("p2");
    bolita1.style.display = "block";
    bolita1.style.animation = "espada .7s";
    barraVida();
});

p3.addEventListener("click", () => {
    handleClick("p3");
    bolita1.style.display = "block";
    bolita1.style.animation = "bola .7s";
    barraVida();
});