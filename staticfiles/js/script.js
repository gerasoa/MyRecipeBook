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

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.favorite-icon').forEach(function (icon) {
      icon.addEventListener('click', function () {
        var recipeId = this.getAttribute('data-recipe-id');
        var iconElement = this;
        fetch(`/recipes/toggle_favorite/${recipeId}/`, {
          method: 'POST',
          headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({})
        })
          .then(response => response.json())
          .then(data => {
            if (data.is_favorite) {
              iconElement.classList.remove('far');
              iconElement.classList.add('fas');
            } else {
              iconElement.classList.remove('fas');
              iconElement.classList.add('far');
            }
          });
      });
    });
  });