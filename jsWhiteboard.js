// Takes a string and returns new string without first and last letter
trimmer = (string) => {
    return string.slice(1, -1)
}

console.log(trimmer("poop"))

//  You are given an odd-length array of integers, 
// in which all of them are the same, except for one single number.
//  Complete the method which accepts such an array,
//  and returns that single different number.
//  [1,1,3] ==> 3
//  [2,2,2,4,2] ==> 4
uniqueChecker = (array) => {
    let uniqueNum = 0
    for(let i = 0; i < array.length; i ++){
        if (i[1] === i[0] || i[1] === i[2]){
        }
    }
}

// Complete the method that takes a boolean value 
// and return a "Yes" string for true, or a "No" string for false.


// Create a function that takes 2 numbers in form of a string as an input,
//  and outputs the sum (also as a string) 

/* Given a list of words, determine if any of them are palindromes   more descriptive   def return_palindrome(list):     pal_list = []     for word in list:         if word == word[::-1]:             pal_list.append(word)     return pal_list */

// Write code that outputs the Fibonacci series
// F_{n}=F_{n-1}+F_{n-2},}
// 1,\;1,\;2,\;3,\;5,\;8,\;13,\;21,\;34,\;55,\;89,\;144,\;\ldots }

// Implement FizzBuzz

// return true or fales if each character is unique in a string

// Check if string of characters is a permutation of a palindrome