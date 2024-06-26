/*
LECTURE 6: CODING WITH JAVASCRIPT
*/

// console.log("HELLO MADLANGPEOPLE MABUHAY")

// Creating variables
let x = 5
var y = 6
const z = 7

// console.log(x, y, z)

// if statements
if (x == y) {
    console.log(x.toString().concat(" is equal to ", y.toString()))
} else if (x == z) {
    console.log(x.toString().concat(" is equal to ", z.toString()))
} else {
    console.log(x.toString().concat(" is not equal to anything"))
}

const students = ["peter", "maja", "aj", "quinmar"]
console.log(students.length)

// COMPARING TWO VALUES AND DATA TYPES
console.log(0 === "0")
console.log(0 == "0")

for (var i = 0; i < z; i++){
    console.log(i)
}

for (var student of students){
    for (var i = 0; i < student.length; i++){
        console.log(student[i])
    }  
}

console.log(students[2])

function degreesToRadians (num) {
    var value = num * Math.PI / 180
    return value
}

console.log(degreesToRadians(180))

function getLatitude(distance, azimuth) {
    var latitude = - distance * Math.cos(degreestoRadians(azimuth))
    return latitude
}

console.log(getLatitude(12, 50))
