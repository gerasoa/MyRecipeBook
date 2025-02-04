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

        // Obter o token CSRF do cookie
        var csrftoken = getCookie('csrftoken');

        fetch(`/recipes/toggle_favorite/${recipeId}/`, {
          method: 'POST',
          headers: {
            'X-CSRFToken': csrftoken,
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

  // Função para obter o token CSRF do cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se o cookie começa com o nome desejado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}