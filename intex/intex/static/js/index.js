const nav = document.querySelector(".nav_bar");
const nav_height = nav.getBoundingClientRect().height;
// const nav_height = nav.getBoundingClientRect().height;
const gotoTop = document.querySelector(".toTop");

document.addEventListener("scroll", () => {
  if (window.scrollY > nav_height) {
    nav.classList.add("navbar--dark");
  } else {
    nav.classList.remove("navbar--dark");
  }

  gotoTop.style.opacity = `${window.scrollY / screen.height}`;
});
