function bubblesort(arr) {
    let flag = true;
    while (flag) {
        flag = false;
        for (let i=0;i<arr.length-1;i++) {
            if (arr[i] < arr[i+1]) {
                flag = true;
                arr[i+1] = arr[i] - arr[i+1];
                arr[i] -= arr[i+1];
                arr[i+1] += arr[i];
            }
        }
    }
    return arr
}

const numbers = [5,0,9,1,7,4,2,6,3,8];

console.log(numbers.toString());
console.log(numbers.join("+"));
console.log(numbers.join(" "));
console.log(numbers.join(""));

console.log(bubblesort(numbers));
