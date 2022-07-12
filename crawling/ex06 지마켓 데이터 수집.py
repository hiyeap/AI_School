{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d4e15a18",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver as wb\n",
    "from selenium.webdriver.common.by import By\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "80eb93df",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = wb.Chrome()\n",
    "driver.get(\"http://corners.gmarket.co.kr/Bestsellers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "66de6961",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 첫번째 상품 클릭\n",
    "img = driver.find_elements(By.CLASS_NAME, \"lazy\")\n",
    "img[0].click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "fe92ee25",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2-2. 상품의 이름 수집\n",
    "title = driver.find_element(By.CSS_SELECTOR, \"h1.itemtit\").text\n",
    "#2-3. 상품의 가격 수집\n",
    "price = driver.find_element(By.CSS_SELECTOR, \"strong.price_real\").text\n",
    "#2-4 상품의 카테고리 수집\n",
    "cate = driver.find_element(By.CSS_SELECTOR, \"li.on>a\").text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "c8e29779",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('진짜진짜 촉촉한 올리브 토너 2개 + 로션 1개/+사은품', '10,500원', '스킨/토너')"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title, price, cate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "61e0e798",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8d154059",
   "metadata": {},
   "outputs": [],
   "source": [
    "titleList = []\n",
    "priceList = []\n",
    "cateList= []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0619087d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 상품 10개를 수집!\n",
    "for i in range(0,10):\n",
    "    img = driver.find_elements(By.CLASS_NAME, \"lazy\")\n",
    "    img[i].click()\n",
    "    # 중간중간 코드에 쉬는 시간을 부여\n",
    "    # 서버에게 부담을 주지 않기 위해서\n",
    "    # 화면에 전환이 있었을 때(클라이언트와 서버가 통신)\n",
    "    # time.sleep(10) = 무조건 10초를 멈춤\n",
    "    # driver.implicitly_wait(10) = 최대 10초\n",
    "    # html파일을 다 받아오면 그 중간에 멈추고 뒤 코드를 실행!\n",
    "    time.sleep(5)\n",
    "    title = driver.find_element(By.CSS_SELECTOR, \"h1.itemtit\").text\n",
    "    titleList.append(title)\n",
    "    price = driver.find_element(By.CSS_SELECTOR, \"strong.price_real\").text\n",
    "    priceList.append(price)\n",
    "    cate = driver.find_element(By.CSS_SELECTOR, \"li.on>a\").text\n",
    "    cateList.append(cate)\n",
    "    driver.back()\n",
    "    time.sleep(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fcc3e1a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['진짜진짜 촉촉한 올리브 토너 2개 + 로션 1개/+사은품',\n",
       " '제스프리 제스프리 썬골드키위 특대과 3.2kg(23~25과 개당 130g~140g내외)+스푼3개',\n",
       " '완도 전복 쿠폰가 26340 초복 선물용 횟감용 14-16미 1KG 더큰 전복 국내산',\n",
       " '소울키친 빅마마 이혜정의 시크릿코인 205개',\n",
       " '소문난오부자 재래도시락김5g 72봉 최근생산',\n",
       " '도드람한돈 생 삼겹살 500g 구이용',\n",
       " '(추가할인+사은품) 책과함께 떠나는 북캉스 추천도서 188종 선택/무료배송',\n",
       " '올반 볶음밥 3종 10봉(새우4+김치4+우삼겹2)',\n",
       " '촉촉한 초코칩 16개입 x 5박스',\n",
       " '몽베스트 1L 24병 /생수전문배송']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titleList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "558ee474",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['10,500원',\n",
       " '27,740원',\n",
       " '30,000원',\n",
       " '55,640원',\n",
       " '18,900원',\n",
       " '11,900원',\n",
       " '3,900원',\n",
       " '15,700원',\n",
       " '17,000원',\n",
       " '11,880원']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "priceList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "af06a139",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['스킨/토너',\n",
       " '키위/참다래',\n",
       " '전복',\n",
       " '기타조미료/양념',\n",
       " '김',\n",
       " '국내산돼지고기',\n",
       " '유아동전집',\n",
       " '볶음/비빔밥',\n",
       " '비스킷',\n",
       " '생수/탄산수']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cateList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "05d10715",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(cateList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d0e0c9f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "dic = {\"물품명\":titleList, \"가격\":priceList, \"카테고리\":cateList}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "942aad70",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>물품명</th>\n",
       "      <th>가격</th>\n",
       "      <th>카테고리</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>진짜진짜 촉촉한 올리브 토너 2개 + 로션 1개/+사은품</td>\n",
       "      <td>10,500원</td>\n",
       "      <td>스킨/토너</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>제스프리 제스프리 썬골드키위 특대과 3.2kg(23~25과 개당 130g~140g내...</td>\n",
       "      <td>27,740원</td>\n",
       "      <td>키위/참다래</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>완도 전복 쿠폰가 26340 초복 선물용 횟감용 14-16미 1KG 더큰 전복 국내산</td>\n",
       "      <td>30,000원</td>\n",
       "      <td>전복</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>소울키친 빅마마 이혜정의 시크릿코인 205개</td>\n",
       "      <td>55,640원</td>\n",
       "      <td>기타조미료/양념</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>소문난오부자 재래도시락김5g 72봉 최근생산</td>\n",
       "      <td>18,900원</td>\n",
       "      <td>김</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>도드람한돈 생 삼겹살 500g 구이용</td>\n",
       "      <td>11,900원</td>\n",
       "      <td>국내산돼지고기</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>(추가할인+사은품) 책과함께 떠나는 북캉스 추천도서 188종 선택/무료배송</td>\n",
       "      <td>3,900원</td>\n",
       "      <td>유아동전집</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>올반 볶음밥 3종 10봉(새우4+김치4+우삼겹2)</td>\n",
       "      <td>15,700원</td>\n",
       "      <td>볶음/비빔밥</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>촉촉한 초코칩 16개입 x 5박스</td>\n",
       "      <td>17,000원</td>\n",
       "      <td>비스킷</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>몽베스트 1L 24병 /생수전문배송</td>\n",
       "      <td>11,880원</td>\n",
       "      <td>생수/탄산수</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 물품명       가격      카테고리\n",
       "0                    진짜진짜 촉촉한 올리브 토너 2개 + 로션 1개/+사은품  10,500원     스킨/토너\n",
       "1  제스프리 제스프리 썬골드키위 특대과 3.2kg(23~25과 개당 130g~140g내...  27,740원    키위/참다래\n",
       "2    완도 전복 쿠폰가 26340 초복 선물용 횟감용 14-16미 1KG 더큰 전복 국내산  30,000원        전복\n",
       "3                           소울키친 빅마마 이혜정의 시크릿코인 205개  55,640원  기타조미료/양념\n",
       "4                           소문난오부자 재래도시락김5g 72봉 최근생산  18,900원         김\n",
       "5                               도드람한돈 생 삼겹살 500g 구이용  11,900원   국내산돼지고기\n",
       "6          (추가할인+사은품) 책과함께 떠나는 북캉스 추천도서 188종 선택/무료배송   3,900원     유아동전집\n",
       "7                        올반 볶음밥 3종 10봉(새우4+김치4+우삼겹2)  15,700원    볶음/비빔밥\n",
       "8                                 촉촉한 초코칩 16개입 x 5박스  17,000원       비스킷\n",
       "9                                몽베스트 1L 24병 /생수전문배송  11,880원    생수/탄산수"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "bestItem = pd.DataFrame(dic)\n",
    "bestItem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "738f3b7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "bestItem.to_csv(\"G마켓 베스트.csv\", encoding=\"euc-kr\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f545d01",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1132af4",
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
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
