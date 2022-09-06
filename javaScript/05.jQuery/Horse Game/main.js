// 1. left라는 버튼을 눌렀을 때, 말이 왼쪽으로 50px씩 이동
// 2. right라는 버튼을 눌렀을 때, 말이 오른쪽으로 50px씩 이동
// 단, 말이 배경사진 밖으로 나가지 않게 할 것!

let cnt = 0
$('.btn.left').click(()=>{
    if(cnt<24){
    cnt ++
    $('#horse').css('right',`${cnt*50}px`)
    }
}) 



$('.btn.right').click(()=>{
    if(cnt>0){
    cnt += 50
    $('#horse').css('right',`${cnt}px`)
    }
})

// 키보드 방향키로 말의 위치를 이동
$('body').on('keydown',(event)=>{
    console.log(event.keyCode)

    if(event.keyCode ==37){
        if(cnt<24){
            cnt ++
            $('#horse').css('right',`${cnt*50}px`)
        } 
    }
    if(event.keyCode ==39){
        if(cnt>0){
            cnt --
            $('#horse').css('right',`${cnt*50}px`)
        }
    }
    if(event.keyCode ==32){
        // animate() 함수
        // css 속성들을 이용해서 애니메이션을 수행하는 것
        // 단, 수치형 속성값으로만 가능하다
        // ex) width, height, left등 가능
        // background-color 등 불가능

        // .animate(css속성들, 속도)
        $('#horse').animate({bottom:'400px'},"slow").animate({bottom:'200px'},"slow")
         
        

    }
})

