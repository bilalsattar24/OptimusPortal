$(document).ready(function(){
    //change color of text and required attribute based on off day selection
    $('input[name="isOff"]').change(function () {
        if( $('input[name="isOff"]').is(':checked') ) {
            $('#isOff').css('color', 'green');

            $('.numDeliveries').css('color', 'gray');
            $('#numDeliveries').removeAttr('required');

            $('.helperName').css('color', 'gray');
            $('#helperName').removeAttr('required');

            $('.driverName').css('color', 'gray');
            $('#driverName').removeAttr('required');

            $('.storeNum').css('color', 'gray');
            $('#storeNum').removeAttr('required');
        }
        else {
            document.getElementsByClassName("numDeliveries").required = true;
            $('#isOff').css('color', 'gray');

            $('.numDeliveries').css('color', 'black');
            $('#numDeliveries').attr('required', 'required');

            $('.helperName').css('color', 'black');
            $('#helperName').attr('required', 'required');

            $('.driverName').css('color', 'black');
            $('#driverName').attr('required', 'required');

            $('.storeNum').css('color', 'black');
            $('#storeNum').attr('required', 'required');
        }
    })

})