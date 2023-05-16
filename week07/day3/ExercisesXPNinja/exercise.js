// Exercise 1 : Checking The BMI

function calculateBMI() {
    return this.Mass/(this.Height/100)**2
}

function compareBMI(persons) {
    let max = [0,''];
    for (let i=0; i<persons.length; i++) {
        if (persons[i].BMI() > max[0]) {
            max[0] = persons[i].BMI();
            max[1] = persons[i].FullName;
        }
    }
    return `${max[1]} has ${max[0].toFixed(2)} BMI`
}

function Person(fullname, mass, height) {
    this.FullName = fullname;
    this.Mass = mass;
    this.Height = height;
    this.BMI = calculateBMI
}

const person1 = new Person("Mary", 60, 160);
const person2 = new Person("John", 90, 170);

console.log(compareBMI([person1, person2]))


// Exercise 2 : Grade Average
function findAvg(gradesList) {

    function isSucceeded() {
        return (sum > 65);
    }
    let sum = 0;
    for (let i=0; i<gradesList.length; i++) {
        sum += gradesList[i]
    }
    sum = Math.round(sum/gradesList.length);
    console.log("Your score is", sum+'.', (isSucceeded())?"Congratulations! You have passed the exam!":"You have to repeat the course. The score is not enough to pass.")
}

findAvg([90,90,4,8,90,80])
findAvg([90,90,44,8,90,80])