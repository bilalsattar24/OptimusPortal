$(".newDatePick").change(function() {
    console.log("test2")
    var inputDate = String($(".newDatePick").val());
    console.log(inputDate)
    var day = String();
    var year = String();
    var month = String();
    var count = 0;
    //separate date into month, year, day variables.
    //todo: move to external method for use in multiple places
    for (i=0; i<inputDate.length; i++) {
        if (i<4) {
            year += inputDate[i];
        }
        else if (i>4 && i<7) {
            month += inputDate[i];
        }
        else if (i>7) {
            day += inputDate[i];
        }
    }
    year = parseInt(year);
    month = parseInt(month)-1;
    day = parseInt(day);
    date = new Date(year,month,day);
    console.log(date);
    dayNumber = date.getDay();
    console.log(dayNumber);
    var days = 
    [ 
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ];
    console.log(days[dayNumber]);
    var dayName = days[dayNumber];
    $(".newDayName").val(dayName);
})
//prefill date and day that comes over from index.html into datepick   
$( document ).ready(function() {
    var days = 
    [ 
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ];
    
    var inputDate = String($(".newDatePick").val());
    console.log(inputDate)
    var day = String();
    var year = String();
    var month = String();
    var count = 0; 
    for (i=0; i<inputDate.length; i++) {
        if (i<4) {
            year += inputDate[i];
        }
        else if (i>4 && i<7) {
            month += inputDate[i];
        }
        else if (i>7) {
            day += inputDate[i];
        }
    }
    year = parseInt(year);
    month = parseInt(month)-1;
    day = parseInt(day);
    date = new Date(year,month,day);
    console.log(date);
    dayNumber = date.getDay();
    console.log(dayNumber);
    console.log(days[dayNumber]);
    var dayName = days[dayNumber];
    $(".newDayName").val(dayName);
});
