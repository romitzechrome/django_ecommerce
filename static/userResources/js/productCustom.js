// function productTotal() {
//
//     var productQuantity=document.getElementById("productQuantity");
//     var productPrice=document.getElementById("productPrice");
//     var productTotal=document.getElementById("productTotal");
//     console.log(productPrice.innerHTML);
//     console.log(productQuantity.value);
//
//     productTotal.value=parseFloat(productQuantity.value)*parseFloat(productPrice.innerHTML);
//     console.log(productTotal.value);
//
// }

var a = 1;
var b = productPrice.innerHTML;

function fn(m) {
    var productQuantity = document.getElementById("productQuantity");
    var productPrice = document.getElementById("productPrice");
    var productTotal = document.getElementById("productTotal");
    g = productQuantity.value;
    h = parseInt(g) + 1
    productTotal.value = b * h;
    productQuantity.value = parseInt(g) + a;

}

function fn1(n) {
    var productQuantity = document.getElementById("productQuantity");
    var productPrice = document.getElementById("productPrice");
    var productTotal = document.getElementById("productTotal");
    g = productQuantity.value;
    i = productPrice.innerHTML;
    if (g != 1) {
        productTotal.value = productTotal.value - b;
        productQuantity.value = g - a;
    }
}


