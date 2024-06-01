// Input
const input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Output: buildProductArray(input)
// [2*3*4*5, 1*3*4*5, 1*2*4*5, 1*2*3*5, 1*2*3*4]
[120, 60, 40, 30, 24];
const output = []
//store partial product in a hashtable 

hashtable_product_before_index = {

}

hashtable_product_after_index = {

}




function product_array(input) {
    let merker;
    for (let i = 0; i < input.length; i++) {
        let product = 1;
        for (let j = 0; j < input.length; j++) {
            if (i !== j) {
            product *= input[j]
            }
        }
        output.push(product);
        


    }
    return output

}




//brute force solution, bad
// function product_array(input) {
//     for (let i = 0; i < input.length; i++) {
//         let product = 1;
//         let copy = input;
//         copy.splice(i,1)
//         console.log(copy)
//         for (let j = 0; j < input.length; j++) {
//             if (i !== j) {
//                 product *= input[j]
//             }
//         }
//         output.push(product);
        


//     }
//     return output

// }


console.log(product_array(input))