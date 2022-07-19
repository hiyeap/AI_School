{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a333c735",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'name': 'SW', 'age': 26, 'phone': '010-0000-0000'}"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1 = {\"name\":\"SW\", \"age\":26, \"phone\" : \"010-0000-0000\"}\n",
    "dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0eed851f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(dic1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "39ebdba3",
   "metadata": {},
   "outputs": [],
   "source": [
    "dic1['birth'] = '02/08'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "539fb4af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'name': 'SW', 'age': 26, 'phone': '010-0000-0000', 'birth': '02/08'}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a8ef322a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'노래제목': '참고사항', '가수': '이무진', '날짜': '2022.06.23'}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic_test = {\"노래제목\":\"참고사항\", \"가수\":\"이무진\", \"날짜\":\"2022.06.23\"}\n",
    "dic_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4d900f4f",
   "metadata": {},
   "outputs": [],
   "source": [
    "del dic1['age']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a0964c2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'name': 'SW', 'phone': '010-0000-0000', 'birth': '02/08'}"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "721b5fac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'SW'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1['name']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b7d157af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'02/08'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1['birth']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "631ce29f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'SW'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1.get('name')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "fea3be4c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['name', 'phone', 'birth'])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7468d2e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['name', 'phone', 'birth']"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(dic1.keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2259bb78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values(['SW', '010-0000-0000', '02/08'])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "82f45b34",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['SW', '010-0000-0000', '02/08']"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(dic1.values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c9ea2776",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name\n",
      "phone\n",
      "birth\n"
     ]
    }
   ],
   "source": [
    "for key in dic1.keys():\n",
    "    print(key)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "bf6b18fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SW\n",
      "010-0000-0000\n",
      "02/08\n"
     ]
    }
   ],
   "source": [
    "for value in dic1.values():\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "82b96d1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name \t SW\n",
      "phone \t 010-0000-0000\n",
      "birth \t 02/08\n"
     ]
    }
   ],
   "source": [
    "for key, value in dic1.items():\n",
    "    print(key,\"\\t\", value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "262e7a20",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'name' in dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "41f90dec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'gender' in dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2ea611a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'phone' in dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d7a03320",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'name': 'SW', 'phone': '010-0000-0000', 'birth': '02/08'}"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a915f416",
   "metadata": {},
   "outputs": [],
   "source": [
    "dic1.clear()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "b8342a47",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{}"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "cc690646",
   "metadata": {},
   "outputs": [],
   "source": [
    "def number_sum(num1, num2):\n",
    "    result = num1 + num2\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "13c8505a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "number_sum(3, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "3deaf00c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def number_minus(num1, num2):\n",
    "    if num1>num2:\n",
    "        result = num1 - num2\n",
    "    else:\n",
    "        result = num2 - num1\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "71ac2f83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "첫 번째 정수 입력 >>5\n",
      "두 번째 정수 입력 >>7\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num1 = int(input(\"첫 번째 정수 입력 >>\"))\n",
    "num2 = int(input(\"두 번째 정수 입력 >>\"))\n",
    "result = number_minus(num1, num2)\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "516ffc28",
   "metadata": {},
   "outputs": [],
   "source": [
    "def s_replace(text):\n",
    "    result = text.replace(\"ㅋ\",\"\")\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "ed1ce422",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "문자열 입력 >>ㅋ을 모두 지워주세요 ㅋㅋ\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'을 모두 지워주세요 '"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = input(\"문자열 입력 >>\")\n",
    "result = s_replace(s)\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "0dc8f4f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cal(num1, num2, op):\n",
    "    if op == \"+\":\n",
    "        result = num1+num2\n",
    "    elif op == \"-\":\n",
    "        result = num1-num2\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "927b397a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "첫 번째 정수 입력 >> 5\n",
      "두 번째 정수 입력 >> 6\n",
      "연산자 입력(+,-) >>+\n",
      "결과 :  11\n"
     ]
    }
   ],
   "source": [
    "num1 = int(input(\"첫 번째 정수 입력 >> \"))\n",
    "num2 = int(input(\"두 번째 정수 입력 >> \"))\n",
    "op = input(\"연산자 입력(+,-) >>\")\n",
    "result = cal(num1, num2, op)\n",
    "print(\"결과 : \",result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "950ab9dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "오늘 하루 정말 좋았습니다^^화이팅\n"
     ]
    }
   ],
   "source": [
    "print(\"오늘 하루 정말 좋았습니다\", \"화이팅\", sep='^^')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "7e50e180",
   "metadata": {},
   "outputs": [],
   "source": [
    "def divisor(num):\n",
    "    for i in range(1, num+1):\n",
    "        if num%i == 0:\n",
    "            print(i, end=\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "f37da896",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 5 10 "
     ]
    }
   ],
   "source": [
    "divisor(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "deb5640b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(*args):\n",
    "    return sum(args)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "efd84a5e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add(1,2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea40fda7",
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
