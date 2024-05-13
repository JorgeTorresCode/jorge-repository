"use strict";

const publications = document.querySelector(".publications");

const createPublication = (nam, content) => {
    let publication = document.createElement("div");

    let text = `
    <div class="publication">
        <h3>${nam}</h3>
        <p>${content}</p>
        <div class="comments">
            <input type="text" id="comment" placeholder="Add comment">
            <input type="submit" id="send">
        </div>
    </div>`;

    publication.innerHTML = text;
    return publication;
};

const loadMorePublications = entry => {
    if (entry[0].isIntersecting) loadPublications(3);
}

const observer = new IntersectionObserver(loadMorePublications);

let counter = 0;
const loadPublications = num => {
    fetch('info.json')
    .then(response => response.json())
    .then(data => {
        for (let i = 0; i < num; i++) {
            let publication = createPublication(data.content[counter].name, data.content[counter].content);
            publications.appendChild(publication);
            counter++;

            if (counter == data.content.length) {
                let h3 = document.createElement("h3");
                h3.classList.add("end");
                h3.textContent = "No more publications";
                publications.appendChild(h3);
                break;
            }

            if (i == num-1) observer.observe(publication);
        };
    });
}

loadPublications(1);