$(function () {

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
                    alert(data.inform);
                }
            });
            //set_button();
        };


        var update_product = function () {
            var material = $("#material_selector");
            var size = $("#size_selector");
            var coating = $("#coating_selector");
            $.ajax({
                url: $(this).attr("data-url"),
                type: "get",
                data: {
                    "name_material": material.val(),
                    "name_size": size.val(),
                    "name_coating": coating.val()
                },
                dataType: "json",
                cache: false,
                success: function (data) {
                    $("#product_info").html(data.html_info);
                    update_button_add();
                }
            });
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


        $("#product_info").on({"change": update_product},
            "#material_selector, #size_selector, #coating_selector");
    }
);