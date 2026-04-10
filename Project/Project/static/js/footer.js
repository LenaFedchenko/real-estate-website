const stars = document.querySelectorAll('.star');
const result = document.getElementById('result');

stars.forEach(star => {
    star.addEventListener('click', function() {
        let value = this.getAttribute('data-value');

        stars.forEach(s => s.classList.remove('active'));

        for(let i = 0; i < value; i++){
            stars[i].classList.add('active');
        }

        result.innerText = "Ваша оцінка: " + value;
    });
});