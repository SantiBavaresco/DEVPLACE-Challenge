//Challenge POO
//EJ6

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
    public Persons() {
        this.firstName = "";
        this.lastName = "";
        this.bday = "";
    }

//Clase Employee realizada utilizando herencia
public class Employee extends Person{
    private string file;
    private string department;

    public Employee() {
        super();
        this.file = "";
        this.department = "";
    }
}