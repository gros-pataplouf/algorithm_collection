import functools

myList = ["butter", "bread", "bananas", "apples"]
myNumbers = [34, 99, 34, 66, 100, -23, 0.5]
# print(myNumbers)

# # // Be able to iterate over and find items in an array
# for item in myList: 
#     print(item)

# for i in range(0, len(myList)):
#     print(myList[i])


# // append 
myList.append("soy milk")
# pop takes the index to be popped and returns the popped element
result = myList.pop(2)

# append takes an element and appends it at the end. NO RETURN VALUE
myList.append("broccoli")

#insert object before index

myList.insert(0, "tofu")

#remove 1st occurence in list. NO RETURN VALUE. throws if not in list
myList.remove("tofu")
# clear removes all items from list. No return value

#myList.clear()

# sort sorts the lsit in ascending order and returns none
myList.sort()

#count return num of an elt
howMuchButter = myList.count("butter")

# extend appends elts from another iterable
myList.extend(["crisps", "cheese"]) # if you pass it a string and not an array, it gets split into array


#index returns the index of an element. raises value error if elt not present
myList.index("cheese")

#in place method
myList.reverse()
#in place method
myList.sort()

newList = myList.copy()

#Tools like map(), filter(), reduce(), sum(), len(), any(), all(), min(), max(), and so on
#map(function, iterable) => takes function without calling it. It then has to be converted to a list
mappedListString = list(map(lambda x: x + " x2", myList))
mappedListLength = list(map(len, myList))
print(mappedListLength, mappedListString)

#if the function takes 2 parameters, you can merge several iterable: 

lst_1 = [1, 2, 4, 16]
lst_2 = [1, 2, 4, 16]
print(list(map(pow, lst_1, lst_2)))
# output : [1, 4, 256, 18446744073709551616]
#filter yields the items of the input iterable for which the function returns true

filteredList = list(filter(lambda x: len(x) > 6, newList))
print(filteredList)

#reduce : 
result = functools.reduce(lambda x, y: x*y, lst_1)
print(result)
#reduce() can also be combined with operator functions to achieve the similar functionality as with lambda functions and makes the code more readable.

#Reduce function i.e. reduce() function works with 3 parameters in python3 as well as for 2 parameters. To put it in a simple way reduce() places the 3rd parameter before the value of the second one, if it’s present. Thus, it means that if the 2nd argument is an empty sequence, then 3rd argument serves as the default one. 



# let inserted = testArray.push("grashopper")
# console.log(testArray)
# console.log("return value of push operation", inserted) // return the index of the inserted item

# // remove from the end
# let popped = testArray.pop("grashopper")
# console.log(testArray)
# console.log(popped) // ---> pop returns the popped value """ grashopper"""


# // insert at index n (n is the index of the inserted element)
# let spliceInsert = testArray.splice(2,0,"hornet")
# //let spliceInsert2 = testArray.splice(1, "wonderwoman") //if delete count is missing, nothing happens here
# //console.log("wonderwoman insert", testArray)
# // splice returns the deleted elements
# let spliceDelete = testArray.splice(2,2, "wasp") //insertion is optional
# console.log(spliceDelete)
# // delete element from beginning
# let removedFirstElement = testArray.shift() // "shift it" == aus dem Schulbus raus
# console.log(removedFirstElement, testArray);
# let insertedFirstElement = testArray.unshift("genericInsect"); // unshift => rein 
# console.log("unshift", testArray)
# // delete element from end: 
# let removedLastElement = testArray.pop()
# console.log(removedLastElement, testArray)

# // remove at index n
# // testArray.fill("buzz") changes the original array AND returns it
# let newArraySlice = testArray.slice(2,-1) // starting index included, last index excluded
# console.log(testArray, newArraySlice)

# //combine arrays
# let newArray = testArray.concat(testArray) // returns a new array, leaves the old one unchanged
# //combine into a string testArray.join
# let insectString = testArray.join(" bzzz ")
# console.log(insectString)
# // modify the array in place: 
# let forEachReturnValue = testArray.forEach(item => {
#     item = "what"
#     // won't work bc string immutable
# })

# arrayOfObjects = [{"one":"butterfly"}, {"two": "bee"}]

# arrayOfObjects.forEach(item => {
#     item.one = "test"
# })

# console.log(forEachReturnValue) /// ---> undefined
# // !!!! forEach() expects a synchronous function — it does not wait for promises. Make sure you are aware of the implications while using promises (or async functions) as forEach callbacks.

# console.log(testArray)

# // higher order functions with arrays: 
# // testing arrays: 
# // testArray.every  // whether all members of the array pass the specified test
# //  testArray.includes // whether an array contains a certain element. Return T/F
# // testArray.some // --> whether certain elements of the array satisfy the condition 

# let resultEvery = testArray.every(_ => _.length < 50)
# let resultSome = testArray.some(_ => _.startsWith("w"))
# let resultIncludes = testArray.includes("water")
# console.log(resultSome, resultEvery, resultIncludes)


# testArray.filter
# let arrayFiltered = testArray.filter(_ => _.length <= 9)
# let arrayFind = testArray.find(_ => _.length <= 8) // returns the 1st occurence satisfing the condition
# let arrayMapBzz = testArray.map(_ => _ = "bzz")
# console.log(arrayFiltered, arrayFind, arrayMapBzz)

# // REDUCE

# let hummingCrowd = testArray.reduce(
#     (accumulator, currentValue) => accumulator + currentValue, "bzzz"
# )  
# let testResult = [1,2,3,4].reduce(
#     (accumulator, currentValue) => {
#         return accumulator + currentValue
#     }
# )

# const range = (start, stop, step) =>
#   Array.from({ length: (stop - start) / step + 1 }, (_, i) => start + i * step);


# function factorial(num) {
#     return range(3, num, 1).reduce(
#         (accumulator, currentValue) => {
#             return accumulator * currentValue
#         }
#     )
# }
# console.log(factorial(4))
# // Know how to handle an array of objects or other data structures
# // Iterate a matrix (two-dimensional arrays and higher)
# // An array may or may not be sorted - you should typically ask if the prompt does not state
# // Assume sorting an array is O(n log n) when using native sort functions
# // Know the implications of having sorted vs unsorted data
# // Know how to group/create subarrays from an input array
# // Compare multiple arrays based on values, lengths, etc.
# // Utilize an array for fast lookups like a hash table when the keys can be integers
# // Assume arrays are dynamic for higher-level or scripted languages (ie. JavaScript, Python)
# // Commonly assume you can use dynamic arrays for compiled languages unless a fixed size is given or memory management is important
