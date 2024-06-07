document.querySelectorAll('.filter__param').forEach(type => {
    type.addEventListener('click', (event) => {
        event.preventDefault(); 
        const selectedType = type.getAttribute('data-filter');

        document.querySelectorAll('.filter__param').forEach(t => {
            t.classList.remove('filter__param-active');
        });

        type.classList.add('filter__param-active');

        document.querySelectorAll('.shop__element').forEach(souvenir => {
            if (selectedType === 'all' || souvenir.classList.contains(selectedType)) {
                souvenir.style.display = 'block';
            } else {
                souvenir.style.display = 'none';
            }
        });
    });
});