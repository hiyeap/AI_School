
// while문과 if~else문을 활용하여 소수를 판별하는 isPrime 함수
// 매개변수 n이 소수라면 true를, 소수가 아니라면 false를 반환
function isPrime(n){
    var divisor = 2;
    if(n==1){
        return false;
    }
    while(n>divisor){
        if(n%divisor==0){
            return false;
        }else{
            divisor++;
        }
    }
    return true;
}


// isPrime함수 출력!
for(var i = 1; i <= 10; i++) {
    document.writeln(i, isPrime(i));
}