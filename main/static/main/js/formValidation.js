$(document).ready(function(){
    $('input[name="isOff"]').change(function () {
        if( $('input[name="isOff"]').is(':checked') ) {
            $('input[name="numDeliveries"]').hide();
            $('#isOff').css('color', 'green');
            $('.numDeliveries').css('color', 'gray');
            $('.helperName').css('color', 'gray');
            $('.driverName').css('color', 'gray');
            $('.storeNum').css('color', 'gray');

        }
        else {
            $('input[name="numDeliveries"]').show();
            $('#isOff').css('color', 'gray');
            $('.numDeliveries').css('color', 'black');
            $('.helperName').css('color', 'black');
            $('.driverName').css('color', 'black');
            $('.storeNum').css('color', 'black');
        }
    })
})