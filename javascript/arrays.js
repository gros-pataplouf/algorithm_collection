// Be able to iterate over and find items in an array
let testArray = ["butter", "butterfly", "fly", "honey", "bee", "disc-ray"]

testArray.sort()
// iterate
for (let i = 0; i < testArray.length; i++) {
    console.log(testArray[i])
}

for (let i of testArray) { // access the items or the array
    console.log(i)
}

for (let i in testArray) { //iterating with IN treats the array like a dictionary and allows to access indices 
    console.log(i)
}

// append = push

let inserted = testArray.push("grashopper")
console.log(testArray)
console.log("return value of push operation", inserted) // return the index of the inserted item

// remove from the end  POP removes the last element from an array and returns that element. T
let popped = testArray.pop()
console.log(testArray)
console.log(popped) // ---> pop returns the popped value " removes the last ele removes the last ele removes the last element from an array and returns that element. Tment from an array and returns that element. Tment from an array and returns that element. T"" grashopper"""


// insert at index n (n is the index of the inserted element)
let spliceInsert = testArray.splice(2,0,"hornet")
//let spliceInsert2 = testArray.splice(1, "wonderwoman") //if delete count is missing, nothing happens here
//console.log("wonderwoman insert", testArray)
// splice returns the deleted elements
let spliceDelete = testArray.splice(2,2, "wasp") //insertion is optional
console.log(spliceDelete)
// delete element from beginning
let removedFirstElement = testArray.shift() // "shift it" == aus dem Schulbus raus
console.log(removedFirstElement, testArray);
let insertedFirstElement = testArray.unshift("genericInsect"); // unshift => rein 
console.log("unshift", testArray)
// delete element from end: 
let removedLastElement = testArray.pop()
console.log(removedLastElement, testArray)

// remove at index n
// testArray.fill("buzz") changes the original array AND returns it
let newArraySlice = testArray.slice(2,-1) // starting index included, last index excluded
console.log(testArray, newArraySlice)

//combine arrays
let newArray = testArray.concat(testArray) // returns a new array, leaves the old one unchanged
//combine into a string testArray.join
let insectString = testArray.join(" bzzz ")
console.log(insectString)
// modify the array in place: 
let forEachReturnValue = testArray.forEach(item => {
    item = "what"
    // won't work bc string immutable
})

arrayOfObjects = [{"one":"butterfly"}, {"two": "bee"}]

arrayOfObjects.forEach(item => {
    item.one = "test"
})

console.log(forEachReturnValue) /// ---> undefined
// !!!! forEach() expects a synchronous function — it does not wait for promises. Make sure you are aware of the implications while using promises (or async functions) as forEach callbacks.

console.log(testArray)

// higher order functions with arrays: 
// testing arrays: 
// testArray.every  // whether all members of the array pass the specified test
//  testArray.includes // whether an array contains a certain element. Return T/F
// testArray.some // --> whether certain elements of the array satisfy the condition 

let resultEvery = testArray.every(_ => _.length < 50)
let resultSome = testArray.some(_ => _.startsWith("w"))
let resultIncludes = testArray.includes("water")
console.log(resultSome, resultEvery, resultIncludes)


testArray.filter
let arrayFiltered = testArray.filter(_ => _.length <= 9)
let arrayFind = testArray.find(_ => _.length <= 8) // returns the 1st occurence satisfing the condition
let arrayMapBzz = testArray.map(_ => _ = "bzz")
console.log(arrayFiltered, arrayFind, arrayMapBzz)

// REDUCE

let hummingCrowd = testArray.reduce(
    (accumulator, currentValue) => accumulator + currentValue, "bzzz"
)  
let testResult = [1,2,3,4].reduce(
    (accumulator, currentValue) => {
        return accumulator + currentValue
    }
)

const range = (start, stop, step) =>
  Array.from({ length: (stop - start) / step + 1 }, (_, i) => start + i * step);


function factorial(num) {
    return range(3, num, 1).reduce(
        (accumulator, currentValue) => {
            return accumulator * currentValue
        }
    )
}
console.log(factorial(4))

//sort returns and sorts the array in ascending order 
testArray.sort()
// Know how to handle an array of objects or other data structures
// Iterate a matrix (two-dimensional arrays and higher)
// An array may or may not be sorted - you should typically ask if the prompt does not state
// Assume sorting an array is O(n log n) when using native sort functions
// Know the implications of having sorted vs unsorted data
// Know how to group/create subarrays from an input array
// Compare multiple arrays based on values, lengths, etc.
// Utilize an array for fast lookups like a hash table when the keys can be integers
// Assume arrays are dynamic for higher-level or scripted languages (ie. JavaScript, Python)
// Commonly assume you can use dynamic arrays for compiled languages unless a fixed size is given or memory management is important
