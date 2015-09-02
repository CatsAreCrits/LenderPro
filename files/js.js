setInterval(function() {
    var currentTime = new Date ( );    
    var currentHours = currentTime.getHours ( );   
    var currentMinutes = currentTime.getMinutes ( );   
    var currentSeconds = currentTime.getSeconds ( );
    currentMinutes = ( currentMinutes < 10 ? "0" : "" ) + currentMinutes;   
    currentSeconds = ( currentSeconds < 10 ? "0" : "" ) + currentSeconds;    
    var timeOfDay = ( currentHours < 12 ) ? "AM" : "PM";    
    currentHours = ( currentHours > 12 ) ? currentHours - 12 : currentHours;    
    currentHours = ( currentHours == 0 ) ? 12 : currentHours;    
    var currentTimeString = currentHours + ":" + currentMinutes + " " + timeOfDay;
    document.getElementById("time").innerHTML = currentTimeString;
}, 1000);
var green = "#7FFF00";
var red = "red";
$("#dollarchange:contains('+')").each(function(i , v){
    $(this).closest("#dollarchange").css("color" , green);
});
$("#dollarchange:contains('-')").each(function(i , v){
    $(this).closest("#dollarchange").css("color" , red);
});
$("#percentchange:contains('+')").each(function(i , v){
    $(this).closest("#percentchange").css("color" , green);
});
$("#percentchange:contains('- +')").each(function(i , v){
    $(this).closest("#percentchange").css("color" , green);
});
$("#percentchange:contains('-')").each(function(i , v){
    $(this).closest("#percentchange").css("color" , red);
});
