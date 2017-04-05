/**
 * Created by happy on 05.04.2017.
 */
function validate() {
    if (document.getElementById('isDelivered').checked) {
        document.getElementById("delivery_label").style.display = "initial";
        document.getElementById("delivery_address").style.display = "initial";

    } else {
        document.getElementById("delivery_label").style.display = "none";
        document.getElementById("delivery_address").style.display = "none";
    }
}
function validate_personal() {
    if (document.getElementById('isDelivered_personal').checked) {
        document.getElementById("delivery_label_personal").style.display = "initial";
        document.getElementById("delivery_address_personal").style.display = "initial";

    } else {
        document.getElementById("delivery_label_personal").style.display = "none";
        document.getElementById("delivery_address_personal").style.display = "none";
    }
}
$(document).ready(function () {
    $(".edit_order").click(function () {
            var order_id = $(this).data('order_id');
            $("#order_id").val(order_id);
        }
    );
    $(".edit_personal_order").click(function () {
            var order_id = $(this).data('order_id');
            $("#personal_order_id").val(order_id);
        }
    );

});
