$(function () {

    var update_selects_for_material = function () {
        var material = $("#material_selector");
        var size = $("#size_selector");
        var coating = $("#coating_selector");
        $.ajax({
            url: $(this).attr("data-url"),
            type: "get",
            data: {
                "name_material": material.val()
            },
            dataType: "json",
            cache: false,
            success: function (data) {
                $("#product_info #amount").html(data.amount);
                $("#product_info #price").html(data.price);
                var sizes = JSON.parse(data.sizes);
                var coatings = JSON.parse(data.coatings);
                var options_sizes = [];
                var options_coatings = [];
                $.each(sizes, function (index, s) {
                    options_sizes.push(
                        '<option>'
                        + s.fields.width + 'x'
                        + s.fields.height + 'x'
                        + s.fields.length +
                        '</option>');
                });
                $.each(coatings, function (index, c) {
                    options_coatings.push(
                        '<option>'
                        + c.fields.name +
                        '</option>');
                });
                $('#size_selector').html(options_sizes);
                $('#coating_selector').html(options_coatings);
                $('#add').attr('data-id', data.concrete_product_id);
            }
        });
    };

    var update_selects_for_sizes = function () {
        var material = $("#material_selector");
        var size = $("#size_selector");
        var coating = $("#coating_selector");
        $.ajax({
            url: $(this).attr("data-url"),
            type: "get",
            data: {
                "name_material": material.val(),
                "name_size": size.val()
            },
            dataType: "json",
            cache: false,
            success: function (data) {
                $("#product_info #amount").html(data.amount);
                $("#product_info #price").html(data.price);
                $("#btn").data("id", data.concrete_product_id);
                var coatings = JSON.parse(data.coatings);
                var options_coatings = [];
                $.each(coatings, function (index, c) {
                    options_coatings.push(
                        '<option>'
                        + c.fields.name +
                        '</option>');
                });
                $('#coating_selector').html(options_coatings);
                $('#add').attr('data-id', data.concrete_product_id);
            }
        });
    };

    var update_selects_for_coatings = function () {
        var material = $("#material_selector");
        var size = $("#size_selector");
        var coating = $("#coating_selector");
        $.ajax({
            url: $(this).attr("data-url"),
            type: "get",
            data: {
                "name_material": material.val(),
                "name_coating": coating.val(),
                "name_size": size.val()
            },
            dataType: "json",
            cache: false,
            success: function (data) {
                $("#product_info #amount").html(data.amount);
                $("#product_info #price").html(data.price);
                $('#add').attr('data-id', data.concrete_product_id);
            }
        });
    };

    var add_to_cart = function () {
        var add_btn = $("#add");
        //alert(add_btn.data('id'));
        $.ajax({
            url: add_btn.attr("data-url"),
            type: "get",
            data: {
                "id": add_btn.attr("data-id")
            },
            dataType: "json",
            cache: false,
            success: function (data) {
                $("#counter").text(data.quantity);
            }
        });
    };

    var update_cart = function () {
        var number = $(this);
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            url: "/ajax_update_cart",
            type: "post",
            data: {
                "id": number.attr("data-id"),
                'quantity': number.val()
            },
            dataType: "json",
            cache: false,
            success: function (data) {
                $("#counter").text(data.quantity);
                $("td[data-id=" + number.attr("data-id") + "]").text(data.price);
                $("#summary_price").text(data.summary_price);
            }
        });
    };

    $("#material_selector").on('change', update_selects_for_material);
    $("#size_selector").on('change', update_selects_for_sizes);
    $("#coating_selector").on('change', update_selects_for_coatings);
    $("#add").on('click', add_to_cart);
    $("td .productQuantity").on('click', update_cart);

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