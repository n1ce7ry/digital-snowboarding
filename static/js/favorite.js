function addToFavorite(souvenir_id, csrfToken) {
    fetch('http://' + window.location.host + '/add-favorite/' + souvenir_id, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        return response.json();
    })
    
    .then(data => {
      if (data.success === 'success') {

        updateSouvenir(data.souvenir_id)

        const Toast = Swal.mixin({
            toast: true,
            position: "bottom-end",
            showConfirmButton: false,
            timer: 5000,
            customClass: {
              title: 'title__alert',
              popup: 'popup__alert',
              timerProgressBar: 'timer__alert',
            },
            html: `
            <a class="cart__alert" href="/favorite/">Перейти в избранное</a>
            `,
            background: '#000000',
            color: '#FFFFFF',
            timerProgressBar: true,
            didOpen: (toast) => {
              toast.onmouseenter = Swal.stopTimer;
              toast.onmouseleave = Swal.resumeTimer;
            }
        });
          Toast.fire({
            icon: "success",
            title: data.souvenir + " " + "добавлено в избранное!"
        });
      } else {
        Swal.fire({
          title: 'Ошибка!',
          text: 'Не удалось добавить в избранное.',
          icon: 'error',
          confirmButtonText: 'ОК'
        });
      }
    })
    .catch(error => {
        console.error(error);
    });
}

function updateSouvenir(souvenir_id) {
    document.getElementById("image_" + souvenir_id).src="/static/images/favorite-fill.svg";
    document.getElementById("image_" + souvenir_id).style="cursor: default;"
    document.getElementById("button_" + souvenir_id).disabled = true;
}


document.querySelectorAll('.favorite__btn').forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
        const souvenir_id = event.target.closest('.shop-favorite__form').getAttribute('data-souvenir-id');
        addToFavorite(souvenir_id, csrfToken);
    });
});