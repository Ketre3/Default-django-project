const big_review = ({name, color}) => {
    return `<div class="big_review"><div class="review_product"><div class="images"><div class="small_images"><img src="" alt="Blazer"> <img src="{{ object.prod_image.url }}" alt="Zoom blazer"><img src="{{ object.prod_image.url }}" alt="Back blazer"></div> <div class="main_image"><img src="{{ object.prod_image.url }}" alt="Main photo blazer"> </div></div><div class="product_content"> <h2>${name}</h2><h3><span class="prise">Prise<br></span><span class="dollar">{{ object.cost }}&#36;</span></h3><form action=""><a href="#">Buy</a></form><p>Details</p><ul class="details"><li >Clothing line:<span>{{ object.Clothing_line }}</span></li><li >Color:<span>{{ object.Color }}</span> </li> </ul> </div></div><div class="relation"><p>{{ object.description }}</p></div>`
};

const renderData = res => {
    let menuHTML = res.data.results.map(big_review).join('');
    let menu = document.getElementById('big_review2');
    menu.innerHTML += menuHTML;
};
