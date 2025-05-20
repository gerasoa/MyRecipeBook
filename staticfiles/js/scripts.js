document.addEventListener('DOMContentLoaded', function () {
  const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
  document.querySelectorAll('.favorite-icon').forEach(function (icon) {
    icon.addEventListener('click', function () {
      var recipeId = this.getAttribute('data-recipe-id');
      var iconElement = this;
      fetch(`/recipes/toggle_favorite/${recipeId}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken,
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