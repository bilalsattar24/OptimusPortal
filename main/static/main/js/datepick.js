// JavaScript File
var date = "2017-05-19";
document.getElementById("test").setAttribute("value", date);

$( "#numDelivery1" ).on("input", function() {
  var numDeliveries = $("#numDelivery1").html();
  alert(numDeliveries * 36);
  $("#pay1").html("$ " + newPay);
});
