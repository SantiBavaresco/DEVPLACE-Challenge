//Challenge POO
//EJ4

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

    //Funcion MyInfo para ver los datos de la clase Persona

    public String MyInfo(){
        return "El nombre de la persona es " + this.firstName this.lastName + "y su cumpleanos es el " + this.bday;
    }
}
