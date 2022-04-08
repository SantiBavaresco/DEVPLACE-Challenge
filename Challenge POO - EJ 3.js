//Challenge POO
//EJ3

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
}
conts persona_parametrizada = new Person("Santiago","Bavaresco","20-03-94")
conts persona_sin_parametrizada = new Person()