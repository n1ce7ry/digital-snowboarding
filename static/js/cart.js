function addToCart(souvenir_id, csrfToken) {
    fetch(window.location.protocol + '//' + window.location.host + '/shop/cart/add/' + souvenir_id + '/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
          'quantity': 1,
          'update': false,
        },
        )
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        return response.json();
    })
    
    .then(data => {
      if (data.success === 'success') {

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
            <a class="cart__alert" href="/shop/cart/">Перейти в корзину</a>
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
            title: data.souvenir + " " + "добавлено в Вашу корзину!"
        });
      } else {
        Swal.fire({
          title: 'Ошибка!',
          text: 'Не удалось добавить товар в корзину.',
          icon: 'error',
          confirmButtonText: 'ОК'
        });
      }
    })
    .catch(error => {
        console.error(error);
    });
}


document.querySelectorAll('.add__btn').forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
        const souvenir_id = event.target.closest('.shop-add__form').getAttribute('data-souvenir-id');
        addToCart(souvenir_id, csrfToken);
    });
});