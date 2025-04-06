$(document).ready(function() {
    function fetchSuggestions(query, $suggestionsContainer) {
        $.ajax({
            url: "{% url 'search' %}",  // Убедитесь, что этот URL корректен
            data: { 'query': query },
            dataType: 'json',
            success: function(data) {
                $suggestionsContainer.empty().show(); // Показать предложения
                let allResults = [];
                // Обработка данных для создания результатов
                data.forEach(item => {
                    if (item.data && item.data.name && item.data.url) {
                        allResults.push({
                            name: item.data.name,
                            url: item.data.url
                        });
                    }
                });
                data.forEach(item => {
                    if (item.data && item.data.fio && item.data.url) {
                        allResults.push({
                            name: item.data.fio,
                            url: item.data.url
                        });
                    }
                });
                // Добавление результатов в контейнер предложений
                if (allResults.length > 0) {
                    $.each(allResults, function(index, result) {
                        $suggestionsContainer.append('<div><a href="' + result.url + '">' + result.name + '</a></div>');
                    });
                } else {
                    $suggestionsContainer.hide(); // Скрыть, если нет результатов
                }
            },
            error: function() {
                $suggestionsContainer.hide(); // Скрыть при ошибке
            }
        });
    }

    // Поиск в навбаре
    $('#search-input').on('keyup', function() {
        let query = $(this).val();
        if (query.length > 2) {
            fetchSuggestions(query, $('#suggestions'));
        } else {
            $('#suggestions').hide();
        }
    });

    // Поиск в хедере
    $('#header-search-input').on('keyup', function() {
        let query = $(this).val();
        if (query.length > 2) {
            fetchSuggestions(query, $('#header-suggestions'));
        } else {
            $('#header-suggestions').hide();
        }
    });

    // Выбор предложения
    $(document).on('click', '#suggestions div, #header-suggestions div', function() {
        let $input = $(this).closest('.form-control-container').find('input');
        $input.val($(this).text());
        $(this).parent().hide(); // Скрыть предложения после выбора
    });

    // Нажатие клавиши Enter для поиска
    $('#search-input, #header-search-input').on('keydown', function(event) {
        if (event.key === 'Enter') {
            let query = $(this).val();
            window.location.href = '/search/?query=' + encodeURIComponent(query);
        }
    });

    // Закрытие предложений при клике вне
    $(document).on('click', function(event) {
        if (!$(event.target).closest('#suggestions, #header-suggestions, #search-input, #header-search-input').length) {
            $('#suggestions, #header-suggestions').hide();
        }
    });
    
    // Показать карточку с контактами
    $('#phoneDropdown').on('mouseenter', function() {
        $('#contactCard').show();
    }).on('mouseleave', function() {
        $('#contactCard').hide();
    });

    // Закрытие карточки при клике вне области
    $(document).on('click', function(event) {
        if (!$(event.target).closest('#contactCard').length && !$(event.target).is('#phoneDropdown')) {
            $('#contactCard').hide();
        }
    });
});
