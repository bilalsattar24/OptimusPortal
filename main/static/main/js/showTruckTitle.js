$( "#selectTruck" ).change(function() {
  //alert( "Handler for .change() called." );
  var truckName = $("#selectTruck").val();
  $("#newWeekHeader").html("New Week for: " + truckName);
});

$(document).ready(function(){
            $("#numDelivery1").change(function(){
                //alert("hi");
                var a = parseInt($("#numDelivery1").val());
                var newPay = a*36;
                $("#pay1").html("$ " + newPay);
                //alert(newPay/*$("#numDelivery1").val()*/); 
            });
        });