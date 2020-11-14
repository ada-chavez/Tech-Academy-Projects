// Function that determines if you are tall enough to ride
function Ride_Function() {
    var Height, Can_ride;
    Height = document.getElementById("Height").value;
    Can_ride = (Height < 52) ? "You are too short":"You are tall enough";
    document.getElementById("Ride").innerHTML = Can_ride + " to ride.";
}

//Function that determines if you are old enough to vote
//Uses ternary operators
function voteFunction() {
    var Age, canVote;
    Age = document.getElementById("Age").value;
    canVote = (Age < 18) ? "You are not old enough to vote":"You can vote!";
    document.getElementById("Vote").innerHTML = canVote;
}

//Function that is an object constructor
function Vehicle(Make, Model, Year, Color) {
    this.Vehicle_Make = Make; //"this" keyword indicates that this is the object
    this.Vehicle_Model = Model;
    this.Vehicle_Year = Year;
    this.Vehicle_Color = Color;
}
//"new" keyword is used to create new objects
var Jack = new Vehicle("Dodge", "Viper", 2020, "Red");
var Emily = new Vehicle("Jeep", "Trail Hawk", 2019, "White and Black");
var Erik = new Vehicle("Ford", "Pinto", 1971, "Mustard");
function myFunction() {
    document.getElementById("Keywords_and_Constructors").innerHTML=
    "Erik drives a " + Erik.Vehicle_Color + "-colored " + Erik.Vehicle_Model + " manufactured in " + Erik.Vehicle_Year;
}

//Object constructor for a dog
function dog(Breed, Age) {
    this.dog_Breed = Breed;
    this.dog_Age = Age;
}

//Creates new objects from the dog() object constructor
var Mochi = new dog("shitzu", 3);
var Paco = new dog("chihuahua", 13);
var Georgia = new dog("terrier", 4);
var Hero = new dog("pinscher", 2);
function this_function() {
    document.getElementById("New_and_This").innerHTML=
    "Paco is a " + Paco.dog_Breed + " and is " + Paco.dog_Age + " years old."
}

//Nested Function
function add_Function(){
    document.getElementById("Nested_Function").innerHTML = add();
    function add() { //first function sums two variables
        var x=3;
        var y=2;
        var sum = x + y;
        function Plus_one() {sum+= 1;} //second function adds one to the sum
        Plus_one();
        return sum; //displays the final sum
    }
}

