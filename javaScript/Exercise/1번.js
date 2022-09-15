// 1. random number로 두개의 정수가 주어집니다.(첫번째 값의 범위는 1~20, 
//     두 번째 값의 범위는 10~30이며 첫 번째 값은 두 번째 값보다 작아야 합니다). 
//     첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭제곱 배열을 
//     출력하는 프로그램을 만드세요. 
//     단, 배열의 두 번째 요소와 뒤에서 두 번째 요소는 삭제한 뒤 출력하세요. 

let first = Math.ceil(Math.random() * 20);        // 1 ~ 20
let second = 0;
while (second < first + 4) {
    second = Math.ceil(Math.random() * 21 + 9);   // 10 ~ 30
}
console.log(first, second);
const powerArray = [];
for (let i = first; i <= second; i++) {
    if (i == first + 1 || i == second - 1)      // 앞에서 두번째, 뒤에서 두번째는 제외
        continue;
    powerArray.push(Math.pow(2, i));
}
console.log(powerArray);
console.clear()