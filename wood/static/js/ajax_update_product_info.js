/**
 * Created by admin on 22.03.2017.
 */
$(function () {

    var update_info = function() {
        var select = $(this);
        alert(select.val());
        $.ajax({
            url: select.attr("data-url"),
            type: "get",
            data: {"material": select.val()},
            dataType: 'json',
            cache: false,
            success: function(data){
                if(data.none){  // смотрим ответ от сервера и выполняем соответствующее действие
                    alert("Нет изделий из данного материала.");
                }else{
                    alert("Есть изделия.");
                }
            }
});
    };

    $("#materialSelector").on("change", update_info);

});
