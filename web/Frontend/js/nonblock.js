// // non block
// const nothing = () => {}
// console.log('start')
// setTimeout(nothing, 3000)   // callback stack
// console.log('end')

// // block like python
// const logend = () => {
//     console.log('end')
// }
// console.log('start')
// setTimeout(logend, 3000)

// function first() {
//     console.log('first')
// }
// function second() {
//     console.log('second')
// }
// function third() {
//     console.log('third')
// }

// first()
// setTimeout(second, 5000)
// third()

// func1() 를 호출했을때 아래와 같이 콘솔에 출력
// func1
// func3
// func2

// hoisting
function func1() {
    console.log('func1')
    setTimeout(func2, 0)
    func3()
}
function func2() {
    console.log('func2')
}
function func3() {
    console.log('func3')
}

func1()