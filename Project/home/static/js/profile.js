document.querySelectorAll("[data-slider]").forEach((slider) => {
    const slides = Array.from(slider.querySelectorAll(".profile-slide"));
    const prevButton = slider.querySelector("[data-slider-prev]");
    const nextButton = slider.querySelector("[data-slider-next]");
    const counter = slider.querySelector("[data-slider-counter]");
    let currentIndex = 0;

    function showSlide(index) {
        if (slides.length === 0) {
            return;
        }

        currentIndex = (index + slides.length) % slides.length;

        slides.forEach((slide, slideIndex) => {
            slide.classList.toggle("active", slideIndex === currentIndex);
        });

        if (counter) {
            counter.textContent = `${currentIndex + 1} / ${slides.length}`;
        }
    }

    if (prevButton) {
        prevButton.addEventListener("click", () => showSlide(currentIndex - 1));
    }

    if (nextButton) {
        nextButton.addEventListener("click", () => showSlide(currentIndex + 1));
    }
});
