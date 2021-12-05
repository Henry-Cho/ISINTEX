const nav = document.querySelector(".nav_bar");

const nav_height = nav.getBoundingClientRect().height;
const gotoTop = document.querySelector(".toTop");

document.addEventListener('scroll', ()=> {
    gotoTop.style.opacity = `${window.scrollY / (nav_height)}`;
})

const search = document.querySelector('#search');
const btn = document.querySelector('.btn');
const filter = document.querySelector('#filter');

btn.addEventListener('mouseenter', ()=> {
    if (search.value === '') {
        if (filter.checked) {
            return;
        }
        alert("Please type a word before search.")
    }
})