{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b60a36ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "택시를 탄다\n"
     ]
    }
   ],
   "source": [
    "money = 11000\n",
    "if money>10000:\n",
    "    print(\"택시를 탄다\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c4c4931e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "버스를 탄다.\n"
     ]
    }
   ],
   "source": [
    "money = 9000\n",
    "if money>10000:\n",
    "    print(\"택시를 탄다\")\n",
    "else:\n",
    "    print(\"버스를 탄다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "08e3c6b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수 입력>>3\n",
      "3과 5의 배수가 아닙니다.\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"정수 입력>>\"))\n",
    "if num%3==0 and num%5==0:\n",
    "    print(\"3과 5의 배수입니다.\")\n",
    "else:\n",
    "    print(\"3과 5의 배수가 아닙니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f9197216",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "주민번호 뒷자리 입력>>1234567\n",
      "당신은 남자입니다.\n"
     ]
    }
   ],
   "source": [
    "num = (input(\"주민번호 뒷자리 입력>>\"))\n",
    "if num[0]==\"1\" or num[0]==\"3\":\n",
    "    print(\"당신은 남자입니다.\")\n",
    "else:\n",
    "    print(\"당신은 여자입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "88da3e00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이름 입력>>옌\n",
      "나이 입력>>11\n",
      "카드 소지 여부(소지, 미소지)>>미소지\n",
      "옌 님은 입장료 17500원에 예약되셨습니다.\n"
     ]
    }
   ],
   "source": [
    "name = input(\"이름 입력>>\")\n",
    "age = int(input(\"나이 입력>>\"))\n",
    "card = input(\"카드 소지 여부(소지, 미소지)>>\")\n",
    "pay = 35000\n",
    "if age<19:\n",
    "    pay *=0.5\n",
    "    if card == \"소지\":\n",
    "        pay *=0.9\n",
    "else:\n",
    "    if card == \"소지\":\n",
    "        pay *=0.7\n",
    "print(name,\"님은 입장료 %d원에 예약되셨습니다.\"%pay)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "de82a404",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "마스크 개수 입력>>22\n",
      "8개들이 포장지 개수 :  2\n",
      "5개들이 포장지 개수 :  2\n"
     ]
    }
   ],
   "source": [
    "# 마스크 개수\n",
    "countOfMask = int(input(\"마스크 개수 입력>>\"))\n",
    "\n",
    "eightBox = countOfMask//8\n",
    "print(\"8개들이 포장지 개수 : \", eightBox)\n",
    "if countOfMask%8%5>0:\n",
    "    fiveBox = ((countOfMask %8)//5)+1\n",
    "else:\n",
    "    fiveBox = ((countOfMask%8)//56)\n",
    "print(\"5개들이 포장지 개수 : \", fiveBox)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "7f24ac5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x값을 입력하세요 : 5\n",
      "y값을 입력하세요 : -12\n",
      "좌표 (5,-12)는 4사분면입니다.\n"
     ]
    }
   ],
   "source": [
    "# 사분면\n",
    "x = int(input(\"x값을 입력하세요 : \"))\n",
    "y = int(input(\"y값을 입력하세요 : \"))\n",
    "side = 0\n",
    "if x>0 and y>0:\n",
    "    side = 1\n",
    "elif x>0 and y<0:\n",
    "    side = 4\n",
    "elif x<0 and y>0:\n",
    "    side = 2\n",
    "else:\n",
    "    side = 3\n",
    "print(f\"좌표 ({x},{y})는 {side}사분면입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a51d003c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "나이 입력>>66\n",
      "요금은 375원입니다.\n"
     ]
    }
   ],
   "source": [
    "# 버스요금\n",
    "age = int(input(\"나이 입력>>\"))\n",
    "pay = 1500\n",
    "if age<5:\n",
    "    pay *= 0.5\n",
    "elif age<20:\n",
    "    pay *= 0.75\n",
    "elif age>=65:\n",
    "    pay *= 0.25\n",
    "else:\n",
    "    pay=1500\n",
    "print(f\"요금은 {int(pay)}원입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "72b2ccdf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "insert coin >> 500\n",
      "메뉴 선택 >> 1\n",
      "돈을 더 넣어주세요~~!\n"
     ]
    }
   ],
   "source": [
    "# 조건문을 활용한 자판기 만들기!!\n",
    "money = int(input(\"insert coin >> \"))\n",
    "num = int(input(\"메뉴 선택 >> \"))\n",
    "# 메뉴 선택하기\n",
    "if money >= 600 :\n",
    "    # 1번 메뉴 선택\n",
    "    if num == 1 :\n",
    "        money -= 600\n",
    "    elif num == 2 :\n",
    "        money -= 800\n",
    "    elif num == 3 :\n",
    "        money -= 1000\n",
    "    else :\n",
    "        print(\"잘못된 메뉴입니다!\")\n",
    "    # 잔돈 계산하기\n",
    "    cash_1000, cash_500, cash_100 = 0,0,0\n",
    "    if money >= 1000 :\n",
    "        # 천원짜리 개수\n",
    "        cash_1000 = money // 1000\n",
    "        # 오백원짜리 개수\n",
    "        cash_500 = money % 1000 // 500\n",
    "        # 백원짜리 개수\n",
    "        cash_100 = money % 1000 % 500 // 100\n",
    "    # 천원 미만 오백원 이상일 경우\n",
    "    elif money >= 500 :\n",
    "        cash_500 = money // 500\n",
    "        cash_100 = money % 500 // 100\n",
    "    # 오백원 미만일 경우\n",
    "    else :\n",
    "        chas_100 = money // 100\n",
    "    print(f\"잔돈 >> 천원 {cash_1000}개, 오백원 {cash_500}개, 백원 {cash_100}개\")\n",
    "else :\n",
    "    print(\"돈을 더 넣어주세요~~!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8a9c709",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30c83e3a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba8296cf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "048b5f10",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd8cadf2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
