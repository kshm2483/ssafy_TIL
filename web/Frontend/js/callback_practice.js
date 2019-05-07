// // 배열로 이루어진 숫자들을 모두 더하는 함수
// var numbers = [1, 2, 3, 4, 5]
// const numbersAddEach = numbers => {
//     let sum = 0
//     for (const number of numbers) {
//         sum += number
//     }
//     return sum
// }
// console.log(numbersAddEach(numbers))

// // 배열로 이루어진 숫자들을 모두 빼는 함수
// const numbersSubEach = numbers => {
//     let sum = 0
//     for (const number of numbers) {
//         sum -= number
//     }
//     return sum
// }
// console.log(numbersSubEach(numbers))

// // 배열로 이루어진 숫자들을 모두 곱하는 함수.ver1
// const numbersMulEach = numbers => {
//     let mul = 1
//     for (const number of numbers) {
//         mul *= number
//     }
//     return mul
// }
// console.log(numbersMulEach(numbers))

// // 함수.ver2
// const numbersEach = (numbers, callback) => {
//     let acc
//     for (const number of numbers) {
//         acc = callback(number, acc)
//     }
//     return acc
// }
// const addEach = (number, acc = 0) => acc + number
// console.log(numbersEach(numbers, addEach))
// const subEach = (number, acc = 0) => acc - number
// console.log(numbersEach(numbers, subEach))
// const mulEach = (number, acc = 1) => acc * number
// console.log(numbersEach(numbers, mulEach))

// 함수.ver3 익명함수
const NUMBERS = [1, 2, 3, 4, 5]
const numbersEach = (numbers, callback) => {
    let acc
    for (let i = 0; i < numbers.length; i++) {
        number = numbers[i]
        acc = callback(number, acc)
    }
    return acc
}

console.log(numbersEach(NUMBERS, (number, acc = 0) => acc + number))