// Daily Challenge: Stars

for (let i=0;i<6;i++) {
    console.log('* '.repeat(i+1))
}

for (let i=0; i<6; i++) {
    let s = []
    for (let j=0; j<=i; j++) {
        s.push("*")
    }
    console.log(s.join(" "))
}