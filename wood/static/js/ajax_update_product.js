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
                $('#add').data('id', data.concrete_product_id);
                //alert($('#add').data('id'));

                //var btn_url = $('#btn_add #add').data('url');
                //$('#btn_add').html('<button id="add" class="btn btn-primary"  data-id="' + data.concrete_product_id +
                //    '" data-url="' + btn_url + '" type="button"> Добавить в корзину </button>');
                //var cp = $("#btn").data("id", data.concrete_product_id);
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
                $('#add').data('id', data.concrete_product_id);
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
                $('#add').data('id', data.concrete_product_id);
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


    $("#material_selector").on('change', update_selects_for_material);
    $("#size_selector").on('change', update_selects_for_sizes);
    $("#coating_selector").on('change', update_selects_for_coatings);
    $("#add").on('click', add_to_cart);


});