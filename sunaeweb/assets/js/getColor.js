const colors = ['#FF9D37', '#3974B7', '#3292F9'];
const randomColor = colors[Math.floor(Math.random() * colors.length)];
document.querySelector('.title').style.color = randomColor;