// [2] === [2]
// false

// {} === {}
// false

const object1 = { number: 5 };
const object2 = object1;
const object3 = object2;
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number)
console.log(object3.number)
console.log(object4.number)

// 4, 4, 5


class Animal {
    constructor(name, type, color) {
        this.name = name;
        this.type = type;
        this.color = color
    }
}

class Mammal extends Animal {
    constructor(name, type, color) {
        super(name, type, color);
    }

    sound(sound) {
        console.log(`${sound} I'm a ${this.type}, named ${this.name} and I'm ${this.color}`)
    }
}

class farmerCow extends Mammal {
    constructor(name, type, color) {
        super(name, type, color);
        this.sound("Moo")
    }

}

const cowLily = new farmerCow("Lily", "cow", "brown and white")