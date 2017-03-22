$(function () {

    var update_product = function() {
        var select = $(this);
        $.ajax({
            url: select.attr("data-url"),
            type: "get",
            data: {"name_material": select.val()},
            dataType: 'json',
            cache: false,
            success: function(data){
                if(data.none){  // смотрим ответ от сервера и выполняем соответствующее действие
                    alert("Нет изделий с такими параметрами.");
                }else{
                    //$("#plants-blog").html(data.html_plants_blog);
                    alert("Есть изделия.");
                }
            }
        });
    };

    $("#material_selector").on("change", update_product);
});