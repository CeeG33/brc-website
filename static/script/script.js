const myCarouselElement = document.querySelector('#myCarousel')

const projectsCarousel = document.querySelector('#projectsCarousel')

const carousel = new bootstrap.Carousel(myCarouselElement, {
    interval: 2000,
    touch: false
})

const carousel2 = new bootstrap.Carousel(projectsCarousel, {
    interval: 2000,
    touch: false
})