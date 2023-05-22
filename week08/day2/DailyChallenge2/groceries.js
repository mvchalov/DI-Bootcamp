let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
};

const displayGroceries = () => {
    groceries.fruits.forEach(e=>{
        console.log(e)
    });
};

const cloneGroceries = () => {
    let user = client;
    user = "Betty";
    console.log(user, client);

    const clientRef = [client];
    const userRef = clientRef;
    userRef[0] = "Betty";
    console.log(...userRef, ...clientRef);

    const shopping = groceries;
    shopping.totalPrice = "35$";
    shopping.other.payed = false;

    console.log(groceries.totalPrice, shopping.totalPrice);
    console.log(groceries.other.payed, shopping.other.payed);

};

cloneGroceries()