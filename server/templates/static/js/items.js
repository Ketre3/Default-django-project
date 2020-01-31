const renderItem = ({id, name, image_url, count, total, url}) => {
  return `    <div class="content_basket" id="item_id-${id}">
              <div class="goodes"><a href="${url}">
              <img src="${image_url}" alt="${name}" class="little_img"></a>
              <a href="${url}"><p>${name}</p></a>
              </div>
              <h2>${total}&#36;</h2>
              <h2><a href="#" data-id=${id} data-type="delete">
                      <img src="/static/IMAGE/arrow_rotated.png"></a>
                <span>${count}</span>
              <a href="#" data-id=${id} data-type="add">
                      <img src="/static/IMAGE/arrow_rotateda.png"></a></h2>
              </div>
  `
};
// w 30 h 58
// <a href="#"><img src="/media/image/arrow_rotateda.png"></a>
