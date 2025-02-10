document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.star-rating .fa-star');
    const ratingValue = document.querySelector('.rating-value');

    stars.forEach(star => {
      star.addEventListener('click', function () {
        const rating = this.getAttribute('data-rating');
        ratingValue.value = rating;

        stars.forEach(s => {
          s.classList.remove('checked');
        });

        for (let i = 0; i < rating; i++) {
          stars[i].classList.add('checked');
        }
      });
    });
  });