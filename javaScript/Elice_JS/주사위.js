// 주사위게임 만들기!
// rand 함수는 1부터 6까지 출력하는 함수
// Math.random()은 0부터 1까지의 실수를 랜덤으로 출력하는 메서드
function rand(maxNum){
    var dice = Math.floor(Math.random() * maxNum) + 1;
    document.write(dice);
}

rand(6);
