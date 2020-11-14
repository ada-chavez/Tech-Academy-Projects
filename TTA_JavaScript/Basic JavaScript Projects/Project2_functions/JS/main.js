//Function to display "This text is green" in the font-color green
function My_First_Function () {
    var str = "This text is green";
    var result = str.fontcolor("green");
    document.getElementById("Green_Text").innerHTML = result;
}

//Function that uses the += operator to concatenate two string varialbes
function myFunction() {
    var sentence = "I am learning";
    sentence += " a lot from this course!";
    document.getElementById("Concatenate").innerHTML = sentence;
}

//Function that multiplies the number 3 and 4 together 
function multiply() {
    var answer = 3*4; //Multiplies 3 and 4 and stores the product in the variable answer
    document.getElementById("demo").innerHTML = answer; //the variable answered is displayed in the HTML where the id is labeled "demo"
}



    