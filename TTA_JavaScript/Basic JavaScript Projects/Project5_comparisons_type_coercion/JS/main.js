//Displays the data type of 3.2
document.write("Data type of 3.2: ");
document.write(typeof 3.2);

//Function that displays infinity and -infinity
function firstFunction() {
    document.getElementById("negInfinite").innerHTML = -3E310;
    document.getElementById("posInfinite").innerHTML = 100E1000000;
}

//Function that displays true and false using boolean logic
function booleanFunction() {
    document.getElementById("x").innerHTML = 12>2;
    document.getElementById("y").innerHTML = 200<1;
}

//Displays 4 in the console
console.log(2+2);

//Function utilizing type coercion (combining a string and a number)
function coercion() {
    document.getElementById("z").innerHTML = ("20" + 3);
}

//Displays false in the console
console.log(3<1);

//Function that displays true and false using double equal signs
function doubleEqualSign() {
    document.getElementById("a").innerHTML = ("a"=="a");
    document.getElementById("b").innerHTML = ("b"=="a");
}

//Function that displays true or false using the === operator
function tripleEqual() {
    document.getElementById("c").innerHTML = '3= = =3: '+(3===3);
    document.getElementById("d").innerHTML = '2= = = "two": '+(2==="two");
    document.getElementById("e").innerHTML = "1= = = '1': " +(1==='1');
    document.getElementById("f").innerHTML = '4 = = = 5: ' +(4===5);
}

//Function that displays true or false using the && and || operator
function andOr() {
    document.getElementById("q").innerHTML = '"a"= ="a" && 11 < 2 is ' + ("a"=="a" && 11<2);
    document.getElementById("r").innerHTML = '"a"= ="a" && 2 > 1 is' +("a"=="a" && 2>1);
    document.getElementById("s").innerHTML = '1 = = = 1 | | 2 < 1 is ' +(1===1)||2<1;
    document.getElementById("t").innerHTML = '"you" = = "u" | | 3 > 90 is ' +("you"=="u" || 3>90);
}

//Function that displays ture or false using the ! operator
function notOperator() {
    document.getElementById("not").innerHTML = '! (3 > 1) is ' +!(3>1);
    document.getElementById("not1").innerHTML = '! (1 > 3) is ' +!(1>3);
}
