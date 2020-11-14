//Dictionary that displays the value associated with the key Animal
function my_Dictionary() {
    var Country = {
        Name: "Philippines",
        Language: "Tagalog",
        Islands: 7641,
        Flower: "Sampaguita",
        Animal: "Carabao"
    };
    delete Country.Animal; //Word operator "delete" deletes the key Animal
    document.getElementById("Dictionary").innerHTML = Country.Animal; //Retrieves the value under the key Animal
}