// // let 블록 스코프 예제
// {
//     let x = '정운지'
//     console.log(x)
//     {
//         let x = 1
//         console.log(x)
//     }
//     console.log(x)
// }
// console.log(typeof x)

// // 전역 변수의 오염
// {
//     var x = '정운지'
//     console.log(x)
//     {
//         var x = 1
//         console.log(x)
//     }
//     console.log(x)
// }
// console.log(typeof x)

// var로 선언하면 현재 스코프(유효범위) 안이라면 어디서든 사용할 수 있으며, 선언하기도 전에 사용할 수 있다.
// let으로 선언하면 그 변수는 선언하기 전에는 존재하지 않는다.

// // hoisting
// y
// var y = 1
// y
// // JS가 이해한 코드
// var y
// y       // undefined
// y = 1   // 1
// y

// not good
// if (x !== 1) {
//     console.log(y)  // undefined
//     var y = 3
//     if (y === 3) {
//         var x = 1
//     }
//     console.log(y)  // 3
// }

// if (x === 1) {
//     console.log(y)  // 3
// }

// // var 로 변수를 선언하면 JS 는 같은 변수를 여러번 정의하더라도 무시한다.
// hoisting
// var x = 1
// if (x === 1) {
//     var x = 2
//     console.log(x)  // 2
// }
// console.log(x)      // 2
// JS
// var x
// x = 1
// if (x === 1) {
//     x = 2
//     console.log(x)
// }
// console.log(x)

// // function hoisting
// // 함수가 선언되기 전에 호출된 형태
// ssafy()
// function ssafy() {
//     console.log('hoi~')
// }

// // 변수에 담았을 땐 hoisting 사용 불가
// ssafy()
// let ssafy = _ => console.log('hoi')