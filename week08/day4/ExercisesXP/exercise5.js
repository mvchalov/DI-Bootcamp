class Dog {
    constructor(name) {
        this.name = name;
    }
}

class Labrador extends Dog {
    constructor(name, size) {
        super(name);
        this.size = size;
    }
}

console.log(new Dog('Bob'));
console.log(new Labrador('Jane', 2));