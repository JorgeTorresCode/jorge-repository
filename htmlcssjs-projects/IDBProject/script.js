"use strict";

const IDBRequest = indexedDB.open("database", 1);

IDBRequest.addEventListener("upgradeneeded", ()=> {
    const db = IDBRequest.result;
    db.createObjectStore('names', {
        autoIncrement: true
    });
});

IDBRequest.addEventListener('success', ()=> {
    readObj();
    console.log("all good");
});

IDBRequest.addEventListener('error', ()=> {
    console.log("an error has occurred with the database");
});

document.getElementById("add").addEventListener("click", ()=> {
    let namer = document.getElementById("name").value;
    if (namer.length > 0) {
        if (document.querySelector(".posible") != undefined) {
            if (confirm("There are unsaved items: You want to continue?")) {
                addObj({name: namer});
                readObj();
            }
        } else {
            addObj({name: namer});
            readObj();
        }
    }
})

const addObj = obj => {
    const IDBData = getIDBData("readwrite");
    IDBData.add(obj);
};

const readObj = obj => {
    const IDBData = getIDBData("readonly");
    const cursor = IDBData.openCursor();
    const fragment = document.createDocumentFragment();
    document.querySelector(".names").innerHTML = "";
    cursor.addEventListener("success", ()=> {
        if (cursor.result) {
            let element = HTMLElementname(cursor.result.key, cursor.result.value);
            fragment.appendChild(element)
            cursor.result.continue();
        } else document.querySelector(".names").appendChild(fragment);
    });
};

const modifyObj = (key, obj) => {
    const IDBData = getIDBData("readwrite");
    IDBData.put(obj, key);
};

const deleteObj = key => {
    const IDBData = getIDBData("readwrite");
    IDBData.delete(key);
};

const getIDBData = (rw)=> {
    const db = IDBRequest.result;
    const IDBtransaction = db.transaction("names", rw);
    const objStore = IDBtransaction.objectStore("names");
    IDBtransaction.addEventListener("complete", ()=> {
        console.log("action made successfully");
    });
    return objStore;
};

const HTMLElementname = (id, namer)=> {
    const container = document.createElement("div");
    const h2 = document.createElement("h2");
    const options = document.createElement("div");
    const saveButton = document.createElement("button");
    const deleteButton = document.createElement("button");

    container.classList.add("showname");
    options.classList.add("options");
    saveButton.classList.add("imposible");
    deleteButton.classList.add("delete");

    saveButton.textContent = "Save";
    deleteButton.textContent = "Delete";

    h2.textContent = namer.name
    h2.setAttribute("contenteditable", "true");
    h2.setAttribute("spellcheck", "false");

    options.appendChild(saveButton);
    options.appendChild(deleteButton);

    container.appendChild(h2);
    container.appendChild(options);

    h2.addEventListener("keyup", ()=> {
        saveButton.classList.replace("imposible", "posible");
    })

    saveButton.addEventListener('click', ()=> {
        if (saveButton.className == "posible") {
            modifyObj(id, {name: h2.textContent});
            saveButton.classList.replace("posible", "imposible");
        }
    })

    deleteButton.addEventListener("click", ()=> {
        deleteObj(id);
        document.querySelector(".names").removeChild(container)
    })

    return container;
}