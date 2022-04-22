function orderPriceCalculation() {
    var orderSubTotal = document.getElementById("orderSubTotal");
    var orderDiscount = document.getElementById("orderDiscount");
    var orderTotal = document.getElementById("orderTotal");
    var orderPrice = document.getElementById("orderPrice");
    var tblBody = document.getElementById("protable");
    var rows = tblBody.rows;
    var cells = tblBody.cells;
    var subTotal = 0;
    var discountRatio = 0.03;
    for (var i = 0; i < rows.length; i++) {
        subTotal = subTotal + parseFloat(rows[i].cells[3].innerHTML);
    }
    orderSubTotal.innerHTML = subTotal;
    var d = parseFloat(orderSubTotal.innerHTML) * discountRatio;
    d = d.toFixed(2)
    orderDiscount.innerHTML = d

    orderTotal.innerHTML = parseFloat(orderSubTotal.innerHTML) - parseFloat(orderDiscount.innerHTML);
    orderPrice.value = orderTotal.innerHTML;
}