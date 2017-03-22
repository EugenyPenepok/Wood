$(function () {

    var update_product = function() {
        var material = $('#material_selector');
        var size = $('#size_selector');
        var coating = $('#coating_selector');
        $.ajax({
            url: $(this).attr("data-url"),
            type: "get",
            data: {"name_material": material.val(),
                "name_size": size.val(),
                "name_coating": coating.val()
            },
            dataType: 'json',
            cache: false,
            success: function(data){
                $("#product_info").html(data.html_info);
            }
        });
    };

    $("#product_info").on('change', "#material_selector, #size_selector, #coating_selector" , update_product);
    //$("#product_info").on('change', '#material_selector', update_product);
});