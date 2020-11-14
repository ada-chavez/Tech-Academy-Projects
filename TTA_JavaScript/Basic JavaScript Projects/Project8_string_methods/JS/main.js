//Function that concatenates string variables
function express() {
    var a = "I ";
    var b = "love ";
    var c = "you.";
    var feelings = a.concat(b, c);
    document.getElementById("true_feelings").innerHTML = feelings;
}

//Function that uses the slice methon on a string variable
function sushi() {
    var yellowtail = "hamachi";
    var section = yellowtail.slice(0,3); //slices the first three characters in hamachi "ham"
    document.getElementById("not_fish").innerHTML = section;
}

//Function that uses the toUpperCase method
function allCaps() {
    var y = document.getElementById("call").innerHTML; //setting the value in p in the variable y
    var z = y.toUpperCase();
    document.getElementById("call").innerHTML = z;
}

//Function that uses the search method to find the character place that the word "Ted" starts
function where() {
    var str = document.getElementById("find").innerHTML;
    var pos = str.search("Ted");
    document.getElementById("place").innerHTML = "It starts at the "+ pos + "th character."
}

//Function that changes a number value to a string value using the toString method
function numStr() {
    var number_value = 323;
    var string_value = number_value.toString();
    document.getElementById("threeTwentyThree").innerHTML = string_value;
}

//Function that formats a number to a specif lenght of 11 using the toPrecision method
function edit_number() {
    var original_number = 12345.498579843759834593485;
    var new_number = original_number.toPrecision(11);
    document.getElementById("precise_number").innerHTML = new_number;
}

//Function that returns a string with the number written with a specified
//number of decimals using the toFixed method
function fix_function() {
    var x = 203.5698;
    var y = x.toFixed(3);
    document.getElementById("num1").innerHTML = y;
}

//Function that returns a number as a number using the valueOf method
function value_of() {
    var number_1 = 666;
    var number_2 = number_1.valueOf();
    document.getElementById("some_numbers").innerHTML = number_2;
    
}