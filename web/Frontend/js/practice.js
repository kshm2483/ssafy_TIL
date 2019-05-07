var _ = require('lodash');
let list = ['짜장면', '짬뽕', '탕수육',]
let numbers = _.range(1, 46)
let pick = _.sample(list)
let lottary = _.sampleSize(numbers, 6)
let menu = {
    짜장면: 'https://i.ytimg.com/vi/Tpks897NSx8/maxresdefault.jpg',
    짬뽕: 'http://dimg.donga.com/wps/NEWS/IMAGE/2018/09/12/91933341.4.jpg',
    탕수육: 'http://cdnweb01.wikitree.co.kr/webdata/editor/201811/14/img_20181114204446_85b31dc8.jpg',
}


console.log(`오늘의 메뉴는 ${pick}입니다.`)
console.log(menu[pick])
console.log(`행운의 번호: ${lottary}`)

let getMin = (a, b) => {
    let min;
    if (a > b) {
        min = b
    } else {
        min = a
    }
    return min
}

let getMinFromArray = nums => {
    let min = Infinity
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}

ssafy = [1, 2, 3, 4, 5]
console.log(getMinFromArray(ssafy))

const myObject = {
    key: 'Value'
}

console.log(myObject.key)
console.log(myObject['key'])

const concat = (str1, str2) => `${str1} - ${str2}`

const checkLongStr = string => {
    if (string.length > 10) {
        return true
    } else {
        return false
    }
}

if (checkLongStr(concat('Happy', 'Hacking'))) {
    console.log(concat('Happy', 'Hacking'))
    console.log('LONG STRING')
} else {
    console.log(concat('Happy', 'Hacking'))
    console.log('SHORT STRING')
}