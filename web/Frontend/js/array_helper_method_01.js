// 1. forEach
// forEach 함수는 아무것도 return 하지 않는다.

// // ES5
// var colors = ['red', 'blue', 'green']

// for (var i = 0; i < colors.length; i++) {
//     console.log(colors[i])
// }

// // ES6
// const COLORS = ['red', 'blue', 'green']
// COLORS.forEach(function (color) {
//     console.log(color)
// })

// COLORS.forEach(color => console.log(color))

// // 1-1 아래 함수에 for 를 forEach로 변환
// function handlePosts() {
//     const posts = [
//         {id: 23, title:'daily news'},
//         {id: 52, title:'tCode City'},
//         {id: 105, title: 'The Rudy'}
//     ]
//     // for (let i = 0; i < posts.length; i++) {
//     //     savePost(posts[i])
//     // }
//     posts.forEach(function (post) {
//         savePost(post)
//     })
// }

// // 1-2 images 배열 안에 있는 정보 height, width 를 곱해 넓이를 구하여
// // areas배열에 저장하는코드를 forEach헬퍼를 사용해 작성
// const images = [
//     {height: 10, width: 30},
//     {height: 20, width: 90},
//     {height: 54, width: 32},
// ]
// const areas = []

// images.forEach(image => areas.push(image['height'] * image['width']))
// console.log(areas)

// // 2. map
// // map 함수는 새로운 배열을 return 한다. (배열 요소를 변형)
// // map filter 는 모두 사본을 return 하며 원본 배열은 바뀌지 않는다.

// const NUMBERS = [1, 2, 3]

// const DOUBLE_NUMBERS = NUMBERS.map(function (number) {
//     return number * 2
// })

// // const DOUBLE_NUMBERS = NUMBERS.map(number => number * 2)

// console.log(DOUBLE_NUMBERS)

// // 2-1 map 헬퍼를 사용해, images 배열 안의 Object 들만 저장되어 있는 heights 배열에 저장해보자.
// const images = [
//     {height: '10px', width: '30px'},
//     {height: '20px', width: '90px'},
//     {height: '54px', width: '32px'},
// ]
// const height = images.map(image => image.height)

// // 2-2 map 헬퍼를 사용해, (distance / time) 을 저장하는 배열 speeds 를 만들어보자
// const trips = [
//     {distance: 34, time: 10},
//     {distance: 90, time: 50},
//     {distance: 59, time: 25},
// ]
// const speeds = trips.map(trip => trip.distance / trip.time)

// // 2-3 다음 두 배열을 객체로 결합한 comics 배열을 만들어보자. (brands 요소가 key, movies 요소가 value)
// const brands = ['Marvel', 'DC']
// const movies = ['Ironman', 'Batman']

// // const comics = brands.map((x, i) => ({name: x, hero: movies[i]}))

// const comics = {}
// brands.map((brand,i) => comics[brand] = movies[i])

// console.log(comics)

// // 3. filter
// const PRODUCTS = [
//     { name: 'cucumber', type: 'vegetable' },
//     { name: 'banana', type: 'fruit' },
//     { name: 'carrot', type: 'vegetable' },
//     { name: 'apple', type: 'fruit' },
// ]
// const fruitProducts = PRODUCTS.filter(function (product) {
//     return product.type === 'fruit'
//     // 해당 조건문에서 true 를 만족할 경우 return
// })
// // const fruitProducts = PRODUCTS.filter(product => product.type === 'fruit')

// // 3-1 filter 헬퍼를 사용해서, numbers 배열 중 50보다 큰 값들만 필터링해서 filteredNumbers 에 저장하라.
// const numbers = [ 15, 25, 35, 45, 55, 65, 75, 85, 95 ]

// const filteredNumbers = numbers.filter(number => number >= 50)
// console.log(filteredNumbers)

// // 3-2 users 배열에서 admin 이 true 인 user object 들만 filteredUsers 배열에 저장하라.
// const users = [
//     {id: 1, admin: true},
//     {id: 2, admin: false},
//     {id: 3, admin: false},
//     {id: 4, admin: false},
//     {id: 5, admin: true},
// ]

// const filteredUsers = users.filter(user => user.admin)
// console.log(filteredUsers)