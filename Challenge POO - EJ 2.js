//Challenge POO
//EJ2

class Person{
    public string name;
    public string lastName;
    public string bday;

    //Constructor Parametrizado
    public Person(string firstName, string lastName, string bday) {
        this.name = name;
        this.lastName = lastName;
        this.bday = bday;
    }

    //Constructor sin Parametrizar
    public Person() {
        this.firstName = "";
        this.lastName = "";
        this.bday = "";
    }

    //Sobrecarga del metodo toString
    @Override
    public String toString() {
        return this.firstName + " " + this.lastName;
    }