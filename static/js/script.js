// Initialization for ES Users
import { Input, Ripple, initMDB } from "mdb-ui-kit";

initMDB({ Input, Ripple });

function validateForm() {
    var product1 = document.getElementById("productDropdown1").value;
    var product2 = document.getElementById("productDropdown2").value;

    if (product1 === "" || product2 === "") {
        alert("Please select two products");
        return false;
    }

    return true;
}

$(document).ready(function() {
    $('.select2').select2();
});


