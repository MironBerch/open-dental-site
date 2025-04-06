document.querySelectorAll('.group-name').forEach(groupName => {
    groupName.addEventListener('click', function(event) {
        const url = this.dataset.href; // Получаем URL из data-атрибута
        window.location.href = url; // Переходим по ссылке
    });
    // Предотвращаем дальнейшее распространение события клика на кнопку
    groupName.addEventListener('click', function(event) {
        event.stopPropagation();
    });
});
