const colors = ['#FF9D37', '#3974B7', '#3292F9'];
const elements = document.getElementsByClassName('title');

for(let i = 0; i < elements.length; i++) {
    let randomColor = colors[Math.floor(Math.random() * colors.length)];
    elements[i].style.color = randomColor;
}