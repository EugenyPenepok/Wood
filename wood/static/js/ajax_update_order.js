$(function () {

    var update_cost_delivery = function () {
        var number = $(this);
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            }
        });
        $.ajax({
            url: '/ajax_update_cost_delivery',
            type: 'post',
            data: {
                'id': number.attr('data-id'),
                'cost': number.val()
            },
            dataType: 'json',
            cache: false
        });
    };

    var update_date_delivery = function () {
        var number = $(this);
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            }
        });
        $.ajax({
            url: '/ajax_update_date_delivery',
            type: 'post',
            data: {
                'id': number.attr('data-id'),
                'date': number.val()
            },
            dataType: 'json',
            cache: false
        });
    };

    $('.cost-delivery').on('change', update_cost_delivery);
    $('.date-delivery').on('change', update_date_delivery);

});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}