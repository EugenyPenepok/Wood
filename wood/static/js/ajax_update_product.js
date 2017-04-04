$(function () {

    var update_btn = function () {
        $(".my-cart-btn").myCart({
            classCartIcon: "my-cart-icon",
            classCartBadge: "my-cart-badge",
            classProductQuantity: "my-product-quantity",
            classProductRemove: "my-product-remove",
            classCheckoutCart: "my-cart-checkout",
            affixCartIcon: true,
            showCheckoutModal: true,
            clickOnAddToCart: function ($addTocart) {
                goToCartIcon($addTocart);
            },
            clickOnCartIcon: function ($cartIcon, products, totalPrice, totalQuantity) {
                console.log("cart icon clicked", $cartIcon, products, totalPrice, totalQuantity);
            },
            checkoutCart: function (products, totalPrice, totalQuantity) {
                console.log("checking out", products, totalPrice, totalQuantity);
            },
            getDiscountPrice: function (products, totalPrice, totalQuantity) {
                console.log("calculating discount", products, totalPrice, totalQuantity);
                return totalPrice * 0.9;
            }
        });
    };

    var update_button_add = function () {
        var material = $("#material_selector");
        var size = $("#size_selector");
        var coating = $("#coating_selector");
        $.ajax({
            url: $("#button_add").attr("data-url"),
            type: "get",
            data: {
                "name_material": material.val(),
                "name_size": size.val(),
                "name_coating": coating.val()
            },
            dataType: "json",
            cache: false,
            success: function (data) {
                //alert(data.html_info);

                $(".action #btn").data("id", data.id);
                $(".action #btn").data("name", data.product);
                $(".action #btn").data("summary", data.inform);
                $(".action #btn").data("price", data.price);
                $(".action #btn").data("quantity", 1);
                $(".action #btn").data("image", data.image);
                update_btn();
            }
        });
        //set_button();
    };


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
                update_button_add();
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
                var coatings = JSON.parse(data.coatings);
                var options_coatings = [];
                $.each(coatings, function (index, c) {
                    options_coatings.push(
                        '<option>'
                        + c.fields.name +
                        '</option>');
                });
                $('#coating_selector').html(options_coatings);
                update_button_add();
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
                update_button_add();
            }
        });
    };


    $("#material_selector").on('change', update_selects_for_material);
    $("#size_selector").on('change', update_selects_for_sizes);
    $("#coating_selector").on('change', update_selects_for_coatings);

});