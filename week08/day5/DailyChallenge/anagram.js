const isAnagram = (a,b) => {
    const unify = (s) => {
        return s.toLowerCase().split``.filter(e => e.match(/[a-zA-Z]/g)).sort((x, y) => x.charCodeAt(0) - y.charCodeAt(0)).join``
    }

    return unify(a)===unify(b)
}

console.log(isAnagram("Astronomer", "Moon starer"))
console.log(isAnagram("School master", "The classroom"))
console.log(isAnagram("The Morse Code", "Here     come dots"))
console.log(isAnagram("The Morse Code", "Here come dot"))