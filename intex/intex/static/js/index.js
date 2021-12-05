const nav = document.querySelector(".nav_bar");

// const nav_height = nav.getBoundingClientRect().height;
const gotoTop = document.querySelector(".toTop");

document.addEventListener('scroll', ()=> {
    gotoTop.style.opacity = `${window.scrollY / (screen.height)}`;
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

const checkInput = () => {
    const search1 = document.querySelector('#search1');
    const search2 = document.querySelector('#search2');
    const search3 = document.querySelector('#search3');
    const search4 = document.querySelector('#search4');
    const search5 = document.querySelector('#search5');
    const search6 = document.querySelector('#search6');

    if (search1.value !== null && (search6.value === '' && search5.value === '' && search4.value === '' && search3.value === '' && search2.value === '' && search1.value === "")) {
        alert("Please type a word or select at least one filter before search.")
    }
}

const prebtn = document.querySelector('#presearch');

prebtn.addEventListener('mouseenter', ()=> {
    checkInput();   
})
