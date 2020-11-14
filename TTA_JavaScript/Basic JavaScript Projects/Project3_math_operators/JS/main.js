//Function that adds 10 and 3 and displays it as 10 + 3 = 13
function additionFunction(){
    var addition = 10 +3;
    document.getElementById("Math").innerHTML = "10 + 3 = " + addition;
}

//Function that subtracts 9 from 21 and displays it as 21 - 9 = 12
function subtractionFunction() {
    var subtraction = 21 - 9;
    document.getElementById("minus").innerHTML = "21 - 9 = " + subtraction;
}

//Function that multiplies 8 times 8 and displays it as 8 x 8 = 64
function multiplyFunction() {
    var multiplication = 8*8;
    document.getElementById("multiply").innerHTML = "8 x 8 = " + multiplication;
}

//Function that divides 100 by 25 and displays it as 100 / 25 = 4
function divisionFunction() {
    var division = 100/25;
    document.getElementById("divide").innerHTML = "100 / 25 = " + division;
}

//Function that uses multiple mathematical operations and displays the result
function moreMath() {
    var someMath = (3*2)/1 + (3-1);
    document.getElementById("math").innerHTML = "( (3 x 2) / 1 ) + (3 - 1) = " + someMath;
}

//Function that uses the modulus operator and displays the result 100 / 26 has a remainder of: 
function modulusFunction() {
    var x = 25%6;
    document.getElementById("mod").innerHTML = "25 / 6 has a remainder of: " + x;
}

//Function that uses the negation operator and displays the result -3
function negationOperator(){
    var y = 3;
    document.getElementById("negate").innerHTML = -y;
}

//Increment and Decrement Function that increases 12 by one and decreases 100 by one 
function inc_dec() {
    var z = 12;
    z++;
    var t = 100;
    t--;
    document.getElementById("number").innerHTML= "12 is now "+ z + " and 100 is now "+ t;
}

//Random number function between 0 and 200 dispalyed in a window alert
window.alert(Math.random() * 200);

//Math object method function displaying
function maxNum(){
    var m = Math.max(2, 3, 8, 22, 22.2);
    document.getElementById("max").innerHTML = "Between these numbers [2,3,8,22] the highest value is: " + m;
}
