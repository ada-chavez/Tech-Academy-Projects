//Utilizes while loop 
function Call_Loop() {
    var Digit = "";
    var X = 1;
    while(X < 11) {
        Digit += "<br>" + X;
        X++;
    }
    document.getElementById("Loop").innerHTML = Digit;
}

//String length function
//str retuns the number of character in a string
function stringLength() {
    var a = "Super Nova Girl";
    var n = a.length; //assigns the number of characters of variable 'a' to variable 'n'
    document.getElementById("length").innerHTML = n;
}


var Instruments = ["Guitar", "Piano", "Drums", "Violin", "Harmonica", "Harp"];
var content = "";
var y;
//For loop function that runs for a certain number of times based on the
//string length of the variable Instruments array
function for_Loop() {
    for(y=0; y < Instruments.length; y++) {
        content += Instruments[y] + "<br>";
    }
    document.getElementById("List_of_Instruments").innerHTML = content;
}

//Function that creates an array and object
//and displays the value of the array at index 2
function array_Function() {
    var studentAge = [];
    studentAge[0] = 12;
    studentAge[1] = 9;
    studentAge[2] = 15;
    studentAge[3] = 11;
    studentAge[4] = 17;
    document.getElementById("Array").innerHTML = "This student is " + studentAge[2] + " years old.";
}

//Create an object with const keyword
function constant_function() {
    const dog = {breed:"labrador retriever", cost:"$500", age:"9 weeks"};
    dog.sex = "female";
    dog.name = "Lady";
    dog.name = "Charlie";
    dog.toy = "tennis ball";
    document.getElementById("Constant").innerHTML = "The name of the " + dog.breed + " was " + dog.name + ", and their favorite toy was a " + dog.toy + ".";
}

//Function that utilizes the let keyword
function let_function() {
    var num1 = 3;
    document.getElementById("someNum1").innerHTML = num1;
    {
        let num1 = 2;
        document.getElementById("someNum2").innerHTML = num1;
    }
    document.getElementById("someNum3").innerHTML = num1;
}

//Function that utilizes the return statement
function my_function(name) {
    return "Hello " + name;
}
document.getElementById("demo").innerHTML = my_function("Ada");

//Creates an object using the let keyword
let food = {
    type: "breakfast",
    temperature: "hot",
    name: "oatmeal",
    description: function() {
        return "This is a " + this.temperature + " " +this.type + " called " + this.name + ".";
    }
};
document.getElementById("foodObject").innerHTML = food.description();

//Loop with a break statement
function break_Loop() {
    for(y=0; y < 100; y++) {    
        if (y === 12) {break;} //when y is 12 it jumps out of the for loop using 'break'
        content += "The number is " + y + "<br>";
    }
    document.getElementById("breakup").innerHTML = content;
}

//Loop with a continue statement
function continue_Loop() {
    for(y=0; y < 10; y++) {    
        if (y === 4) {continue;} //when y is 4 it jumps over one iteration in the loop
                                //and will not display "The number is 4"
        content += "The number is " + y + "<br>";
    }
    document.getElementById("continues").innerHTML = content;
}
