$(".reportsDateSearch").change(function(){
    var inputDate = String($(".reportsDateSearch").val());
    console.log(inputDate);
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
    if (days[dayNumber] != "Saturday") {
        $(".saturdayWarning").text("SELECTED DATE NOT A SATURDAY");
    }
    else {
        $(".saturdayWarning").text("");
    }
});