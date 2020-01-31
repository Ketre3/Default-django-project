const HTMLCategory = ({ name }) => {
    return `<li>
        <a href="?catalog=${name}">
            ${name}
        </a>
    </li>`
};

const renderData = results => {
    let menuHtml = results.map(HTMLCategory).join('');
    let menu = document.getElementById('catalog');
    menu.innerHTML += menuHtml;
};
