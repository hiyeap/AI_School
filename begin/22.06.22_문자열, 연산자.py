{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8c5965b6",
   "metadata": {},
   "source": [
    "### 포매팅 첫번째 방법"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c95c6326",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오늘은 6월 22일 입니다.'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "month = 6\n",
    "day = 22\n",
    "s = \"오늘은 %d월 %d일 입니다.\"%(month, day)\n",
    "s"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a89d61aa",
   "metadata": {},
   "source": [
    "### 포매팅 두번째 방법"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6e107d85",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오늘은 7월 7일 입니다.'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "month = 7\n",
    "day = 7\n",
    "s = f\"오늘은 {month}월 {day}일 입니다.\"\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dbb46ce4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100와 200의 합은 300입니다.\n"
     ]
    }
   ],
   "source": [
    "x = 100\n",
    "y = 200\n",
    "sum2 = x+y\n",
    "print(f\"{x}와 {y}의 합은 {sum2}입니다.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e97bcbe",
   "metadata": {},
   "source": [
    "### 자주 사용하는 문자열 함수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3c6c5d0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# count 함수 : 문자열에 포함된 문자 개수 세기\n",
    "s=\"오늘 점심 메뉴는 탕수육입니다. 저는 탕수육을 매우 좋아해서 탕수육만 먹을겁니다.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "804f8d5b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.count(\"탕수육\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "51055815",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'  오늘 점심 메뉴는 탕수육입니다.   '"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# strip 함수 : 양쪽 공백 지우기\n",
    "s = \"  오늘 점심 메뉴는 탕수육입니다.   \"\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5ad4e035",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오늘 점심 메뉴는 탕수육입니다. 저는 탕수육을 매우 좋아해서 탕수육만 먹을겁니다.'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s=\"오늘 점심 메뉴는 탕수육입니다. 저는 탕수육을 매우 좋아해서 탕수육만 먹을겁니다.\"\n",
    "s.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b2f41421",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오늘 점심 메뉴는 마라탕입니다. 저는 마라탕을 매우 좋아해서 마라탕만 먹을겁니다.'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.replace(\"탕수육\", \"마라탕\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5cbdc714",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['오늘 점심 메뉴는 탕수육입니다', ' 저는 탕수육을 매우 좋아해서 탕수육만 먹을겁니다', '']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# split 함수 : 문자열을 특정 문자 기준으로 나눠주기\n",
    "s.split(\".\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fca24fbe",
   "metadata": {},
   "source": [
    "### 산술 연산자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2bc64f02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "더하기 결과:  26\n",
      "빼기 결과:  20\n",
      "곱하기 결과:  69\n",
      "나누기 결과:  7.666666666666667\n"
     ]
    }
   ],
   "source": [
    "num1 = 23\n",
    "num2 = 3\n",
    "print(\"더하기 결과: \", num1+num2)\n",
    "print(\"빼기 결과: \", num1-num2)\n",
    "print(\"곱하기 결과: \", num1*num2)\n",
    "print(\"나누기 결과: \", num1/num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9c8666a7",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수를 입력하세요 >>1313\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"정수를 입력하세요 >>\")) #input 값은 기본값이 문자열이다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1f4a10e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1313"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8484b4cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수를 입력하세요 >>11\n",
      "정수를 입력하세요 >>25\n",
      "더하기 결과:  36\n",
      "빼기 결과:  -14\n",
      "곱하기 결과:  275\n",
      "나누기 결과:  0.44\n"
     ]
    }
   ],
   "source": [
    "num1 = int(input(\"정수를 입력하세요 >>\"))\n",
    "num2 = int(input(\"정수를 입력하세요 >>\"))\n",
    "print(\"더하기 결과: \", num1+num2)\n",
    "print(\"빼기 결과: \", num1-num2)\n",
    "print(\"곱하기 결과: \", num1*num2)\n",
    "print(\"나누기 결과: \", num1/num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ef802eb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python 점수 입력>>100\n",
      "머신러닝 점수 입력 >>90\n",
      "딥러닝 점수 입력 >>80\n",
      "합계 : 270\n",
      "평균 : 90.0\n"
     ]
    }
   ],
   "source": [
    "num1 = int(input(\"python 점수 입력>>\"))\n",
    "num2 = int(input(\"머신러닝 점수 입력 >>\"))\n",
    "num3 = int(input(\"딥러닝 점수 입력 >>\"))\n",
    "total = num1 +num2+num3\n",
    "\n",
    "print(\"합계 : {}\".format(total))\n",
    "print(\"평균 : {}\".format(total/3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "4bbe7ca8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "시간 입력 >> 3523\n",
      "0시간 58분 43초\n"
     ]
    }
   ],
   "source": [
    "time = int(input(\"시간 입력 >> \"))\n",
    "hour = time//3600\n",
    "minute = time%3600//60\n",
    "second = time%60\n",
    "print(\"{}시간 {}분 {}초\".format(hour, minute, second))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "b614a0d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "xxxxxxxxxx\n"
     ]
    }
   ],
   "source": [
    "s = \"x\"\n",
    "print(s*10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "969f43df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'안녕하세요안녕하세요'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = \"안녕하세요\"\n",
    "s*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "82788272",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "********** 연산하기 **********\n",
      "정수입력>>10\n",
      "정수입력>>20\n",
      "+연산자 입력>>+\n",
      "10 + 20 = 30\n"
     ]
    }
   ],
   "source": [
    "print(\"*\"*10, \"연산하기\", \"*\"*10)\n",
    "num1 = int(input(\"정수입력>>\"))\n",
    "num2 = int(input(\"정수입력>>\"))\n",
    "cal = input(\"+연산자 입력>>\")\n",
    "print(\"{} {} {} = {}\".format(num1, cal, num2, num1+num2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4d625519",
   "metadata": {},
   "source": [
    "### 지수 연산자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "c515c6aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수 입력>>5\n",
      "지수 입력>>3\n",
      "5의 3승은 125입니다.\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"정수 입력>>\"))\n",
    "power = int(input(\"지수 입력>>\"))\n",
    "print(f\"{num}의 {power}승은 {num**power}입니다.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "755cdc4f",
   "metadata": {},
   "source": [
    "### 치환"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "0aab112c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a : 3\n",
      "b : 7\n"
     ]
    }
   ],
   "source": [
    "a = 3\n",
    "b = 7\n",
    "print(\"a : {}\".format(a))\n",
    "print(\"b : {}\".format(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "246ce89a",
   "metadata": {},
   "outputs": [],
   "source": [
    "temp = a\n",
    "a = b\n",
    "b = temp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "8cd25c64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7 3\n"
     ]
    }
   ],
   "source": [
    "a, b = b, a\n",
    "print(a, b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "9cebd9a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "53a599ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a :8, b:10\n"
     ]
    }
   ],
   "source": [
    "a = random.randint(1, 10)\n",
    "b = random.randint(1, 10)\n",
    "print(\"a :{}, b:{}\".format(a,b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "40a0d7ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수입력>>5\n",
      "정수입력>>6\n",
      "b: 6\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"정수입력>>\"))\n",
    "b = int(input(\"정수입력>>\"))\n",
    "print(\"b:\", b) if a<b else print(\"a: \",a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "ec08480c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "첫 번째 정수 입력>>5\n",
      "두 번째 정수 입력>>2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"첫 번째 정수 입력>>\"))\n",
    "b = int(input(\"두 번째 정수 입력>>\"))\n",
    "print(a-b if a>b else b-a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "aba0ef1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수입력>>2\n",
      "짝수\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"정수입력>>\"))\n",
    "print(\"짝수\" if num%2==0 else \"홀수\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e16b4581",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd0249dd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33cf8fbc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e6bf3d7",
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
