$(document).ready(function(){
    $('input[name="isOff"]').change(function () {
        if( $('input[name="isOff"]').is(':checked') ) {
            $('input[name="numDeliveries"]').hide();
        }
        else {
            $('input[name="numDeliveries"]').show();
        }
    })
})