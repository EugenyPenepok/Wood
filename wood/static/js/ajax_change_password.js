$(document).ready(function () {

    $("#submit_btn").click(function () {
        var old = $("#old").val();
        var newp = $("#new").val();
        var confirm = $("#confirm").val();

        if (newp != confirm) {

            $('#errorMessage').html('Пароли не совпадают');
            $('#errorMessage').removeClass('hidden');
            return false;
        }
        else {
            $('#errorMessage').html('');
            $('#errorMessage').addClass('hidden');
        }
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({ // Отправляем запрос
            type: "POST",
            url: "change_password",
            data: {
                old_password: old,
                new_password: newp,
                confirm_password: confirm
            }
        })
            .done(function (data) { // Разбираем полученные данные и пишем в блок grades
                if (data != 'OK') {
                    $('#errorMessage').html(data);
                    $('#errorMessage').removeClass('hidden');
                }
                else {
                    $('#errorMessage').html('');
                    $('#errorMessage').addClass('hidden');
                    $('#successMessage').html('Пароль успешно сменен');
                    $('#successMessage').removeClass('hidden');
                }
            });
        return false;
    });
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