const output = document.getElementById("output");
const copyButton = document.getElementById("copy-button");
const lengthInput = document.getElementById("length");
const upperCaseInput = document.getElementById("uppercase");
const lowerCaseInput = document.getElementById("lowercase");
const numbersInput = document.getElementById("numbers");
const symbolsInput = document.getElementById("symbols");
const generateButton = document.getElementById("generate-button");

const letters = "abcdefghijklmnopqrstuvwxyz".split('');
const numbers = "1234567890".split('');
const symbols = "[]()/._,?¿!¡@*&#^`'+-><${}".split('');

function randomUpperCase() {
    let randomNum = Math.floor(Math.random() * letters.length);
    let randomLetter = letters[randomNum].toUpperCase();
    return randomLetter;
};

function randomLowerCase() {
    let randomNum = Math.floor(Math.random() * letters.length);
    let randomLetter = letters[randomNum];
    return randomLetter;
};

function randomNumber() {
    let randomNum = Math.floor(Math.random() * numbers.length);
    let randomNumber = numbers[randomNum];
    return randomNumber;
};

function randomSymbol() {
    let randomNum = Math.floor(Math.random() * symbols.length);
    let randomSymbol = symbols[randomNum];
    return randomSymbol;
};

generateButton.addEventListener("click", () => {
    let functions = [randomLowerCase, randomUpperCase, randomNumber, randomSymbol];
    let result = ""

    if (!symbolsInput.checked) {
        let x = functions.indexOf(randomSymbol);
        functions.splice(x, 1);
    }

    if (!numbersInput.checked) {
        let x = functions.indexOf(randomNumber);
        functions.splice(x, 1);
    }

    if (!lowerCaseInput.checked) {
        let x = functions.indexOf(randomLowerCase);
        functions.splice(x, 1);
    }

    if (!upperCaseInput.checked) {
        let x = functions.indexOf(randomUpperCase);
        functions.splice(x, 1);
    }

    if (functions.length >= 1 && lengthInput.value >= 1) {

        for (let i = 0; i < lengthInput.value; i++) {
            let random = Math.floor(Math.random() * functions.length);
            result += functions[random]();
        }

    } else {
        output.innerText = "None";
        return
    }

    output.innerText = result;
})

copyButton.addEventListener("click", () => {
    if (output.textContent.length >= 1) {
        navigator.clipboard.writeText(output.textContent);
    }
})