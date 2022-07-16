{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5cdba590",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver as wb\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "222df968",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 크롬브라우저를 실행\n",
    "driver = wb.Chrome()\n",
    "# 1.1 한솥메뉴사이트로 이동!\n",
    "driver.get(\"https://www.hsd.co.kr/menu/menu_list\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "861f4454",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오븐구이 오리도시락'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 상품명, 상품가격정보를 수집\n",
    "menu = driver.find_elements(By.CLASS_NAME, \"h.fz_03\")\n",
    "\n",
    "# By.CSS_SELECTOR = 선택자를 직접 명시할 때 사용\n",
    "# 주의점! 아이디는 #, 클래스 ., 키워드를 항상 명시해야 한다!\n",
    "price = driver.find_elements(By.CSS_SELECTOR, \".item-price>strong\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b2f3478c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['오븐구이 오리도시락',\n",
       " '열무 감초고추장 비빔밥',\n",
       " '열무 두부강된장 비빔밥',\n",
       " '핫 치즈 닭갈비 덮밥',\n",
       " '오리지널 치즈 닭갈비 덮밥',\n",
       " '1993 왕돈까스 도시락',\n",
       " '한입 족발 도시락',\n",
       " '매화(순살 고등어 간장구이)',\n",
       " '진달래',\n",
       " '개나리(순살 고등어 간장구이)',\n",
       " '돈까스도련님고기고기',\n",
       " '탕수육도련님고기고기',\n",
       " '새치 고기고기',\n",
       " '돈치 고기고기',\n",
       " '숯불직화구이',\n",
       " '소불고기',\n",
       " '메가치킨제육',\n",
       " '칠리 찹쌀탕수육도련님',\n",
       " '동백',\n",
       " '치킨제육',\n",
       " '돈까스도련님',\n",
       " '제육볶음',\n",
       " '돈치스팸 도시락',\n",
       " '제육 김치찌개 정식',\n",
       " '제육 김치 부대찌개 정식',\n",
       " '돈치스팸 김치 부대찌개 정식',\n",
       " '빅치킨마요 김치 부대찌개 정식',\n",
       " '치킨마요 김치 부대찌개 정식',\n",
       " '빅치킨마요 김치찌개 정식',\n",
       " '치킨마요 김치찌개 정식',\n",
       " '메가스팸마요',\n",
       " '스팸마요',\n",
       " '메가치킨마요',\n",
       " '왕치킨마요',\n",
       " '빅치킨마요',\n",
       " '치킨마요',\n",
       " '참치마요',\n",
       " '돈치마요',\n",
       " '돈까스 카레',\n",
       " '스팸 김치볶음밥',\n",
       " '김치볶음밥',\n",
       " '스팸철판볶음밥',\n",
       " '소불고기 철판볶음밥',\n",
       " '나시고랭',\n",
       " '묵은지 김치찌개',\n",
       " '김치 부대찌개',\n",
       " '숯불직화구이 덮밥',\n",
       " '마파두부 덮밥',\n",
       " '왕카레돈까스덮밥',\n",
       " '새우돈까스 덮밥',\n",
       " '돈까스 덮밥',\n",
       " '소불고기 감초고추장 비빔밥',\n",
       " '시골제육 두부강된장 비빔밥',\n",
       " '참치야채 감초고추장',\n",
       " '튼튼도시락',\n",
       " '토네이도 소세지 파스타',\n",
       " '트리플 치즈 파스타',\n",
       " '토마토 미트 파스타',\n",
       " '반찬 계란말이',\n",
       " '반찬 묵은지김치찌개',\n",
       " '반찬 카레',\n",
       " '반찬 순살 고등어데리야끼',\n",
       " '반찬 김치 부대찌개',\n",
       " '반찬 치킨',\n",
       " '반찬 고기고기',\n",
       " '반찬 돈까스 도련님',\n",
       " '반찬 제육볶음',\n",
       " '반찬 토네이도 소세지',\n",
       " '반찬 반달돈까스',\n",
       " '뉴 감자고로케',\n",
       " '미니 찹쌀핫도그',\n",
       " '미니 찹쌀탕수육',\n",
       " '케이준후라이',\n",
       " '고메이 크림 고로케',\n",
       " '후라이드 순살(소)_스리라차마요소스',\n",
       " '후라이드 순살(중)',\n",
       " '후라이드 순살(소)_양념치킨소스',\n",
       " '후라이드 순살(소)_케이준소스',\n",
       " '오리지널 닭강정(중)',\n",
       " '오리지널 닭강정(소)',\n",
       " '무생채',\n",
       " '열무김치',\n",
       " '오징어젓갈',\n",
       " '오이지무침',\n",
       " '한솥 두부강된장소스',\n",
       " '한솥 감초볶음고추장소스',\n",
       " '볶음김치',\n",
       " '김치',\n",
       " '무말랭이 무침',\n",
       " '한솥밥',\n",
       " '현미밥',\n",
       " '리얼 티라미수 찰떡',\n",
       " '리얼꿀 미니호떡']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "menuList = []\n",
    "for i in menu:\n",
    "    menuList.append(i.text)\n",
    "menuList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0113af09",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['6,900',\n",
       " '4,500',\n",
       " '4,900',\n",
       " '5,900',\n",
       " '5,900',\n",
       " '9,300',\n",
       " '8,500',\n",
       " '10,000',\n",
       " '7,500',\n",
       " '8,000',\n",
       " '6,000',\n",
       " '5,800',\n",
       " '6,700',\n",
       " '5,800',\n",
       " '6,500',\n",
       " '5,400',\n",
       " '7,000',\n",
       " '4,200',\n",
       " '5,800',\n",
       " '4,700',\n",
       " '4,500',\n",
       " '4,200',\n",
       " '4,900',\n",
       " '8,200',\n",
       " '8,500',\n",
       " '8,500',\n",
       " '7,500',\n",
       " '6,900',\n",
       " '7,000',\n",
       " '6,500',\n",
       " '5,600',\n",
       " '3,700',\n",
       " '5,800',\n",
       " '4,800',\n",
       " '4,100',\n",
       " '3,500',\n",
       " '3,200',\n",
       " '3,800',\n",
       " '4,500',\n",
       " '4,700',\n",
       " '3,900',\n",
       " '4,500',\n",
       " '4,700',\n",
       " '6,000',\n",
       " '4,500',\n",
       " '5,800',\n",
       " '5,900',\n",
       " '5,000',\n",
       " '5,900',\n",
       " '4,100',\n",
       " '4,000',\n",
       " '5,200',\n",
       " '5,000',\n",
       " '3,300',\n",
       " '5,000',\n",
       " '5,500',\n",
       " '5,500',\n",
       " '4,500',\n",
       " '2,500',\n",
       " '4,000',\n",
       " '2,800',\n",
       " '3,600',\n",
       " '4,500',\n",
       " '3,600',\n",
       " '3,400',\n",
       " '3,800',\n",
       " '3,200',\n",
       " '2,600',\n",
       " '2,800',\n",
       " '2,700',\n",
       " '2,500',\n",
       " '2,200',\n",
       " '1,700',\n",
       " '3,500',\n",
       " '4,000',\n",
       " '7,500',\n",
       " '4,000',\n",
       " '4,000',\n",
       " '8,000',\n",
       " '3,400',\n",
       " '400',\n",
       " '500',\n",
       " '400',\n",
       " '700',\n",
       " '1,800',\n",
       " '500',\n",
       " '400',\n",
       " '300',\n",
       " '300',\n",
       " '1,000',\n",
       " '1,700',\n",
       " '1,500',\n",
       " '2,200']"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "priceList = []\n",
    "for i in price:\n",
    "    priceList.append(i.text)\n",
    "priceList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0b11cc64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "93"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(priceList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6138afb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 더보기 버튼을 끝까지 누르는 로직\n",
    "btn = driver.find_element(By.CSS_SELECTOR, \"#btn_more > span > a\")\n",
    "btn.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "05b5ffca",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 더보기를 반복해서 끝까지 실행!\n",
    "# 반복의 횟수가 다 다르기 때문에, while문을 활용!\n",
    "while True:\n",
    "    btn = driver.find_element(By.CSS_SELECTOR, \"#btn_more > span > a\")\n",
    "    btn.click()\n",
    "    time.sleep(1)\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6feda51e",
   "metadata": {},
   "source": [
    "## 예외처리\n",
    "- 오류가 나기전까지 실행하다가 오류가 났을 떄는 다른 코드를 실행\n",
    "- try = 오류나기 전까지의 코드\n",
    "- except = 오류가 났을 때 코드"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a1ab8058",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "더보기 완료!\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    # 오류 나기 전\n",
    "    while True:\n",
    "        btn = driver.find_element(By.CSS_SELECTOR, \"#btn_more > span > a\")\n",
    "        btn.click()\n",
    "        time.sleep(1)\n",
    "except:\n",
    "    # 오류 난 후\n",
    "    print(\"더보기 완료!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "226b5bd9",
   "metadata": {},
   "source": [
    "## 한 셀에 완벽한 크롤링 코드 짜기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d3e8b4ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "더보기 완료~\n"
     ]
    }
   ],
   "source": [
    "# 1. 크롬창 실행 후 > 한솥메뉴사이트 요청\n",
    "driver = wb.Chrome()\n",
    "driver.get(\"https://www.hsd.co.kr/menu/menu_list\")\n",
    "# 2. 더보기를 끝까지 누르는 로직\n",
    "try:\n",
    "    while True:\n",
    "        btn = driver.find_element(By.CSS_SELECTOR, \"#btn_more > span > a\")\n",
    "        btn.click()\n",
    "        time.sleep(1)\n",
    "except:\n",
    "    print(\"더보기 완료~\")\n",
    "# 3. 가격, 메뉴명을 수집\n",
    "menu = driver.find_elements(By.CLASS_NAME, \"h.fz_03\")\n",
    "price = driver.find_elements(By.CSS_SELECTOR, \".item-price>strong\")\n",
    "# 4. 순수한 텍스트 정보만 추출 => 비어있는 리스트에 텍스트만 담기!\n",
    "menuList = []\n",
    "priceList = []\n",
    "for i in range(0, len(menu)):\n",
    "    menuList.append(menu[i].text)\n",
    "    priceList.append(price[i].text)\n",
    "    \n",
    "dic = {\"메뉴\" : menuList, \"가격\":priceList}\n",
    "# 5. 데이터프레임 제작 => 판다스\n",
    "import pandas as pd\n",
    "df = pd.DataFrame(dic)\n",
    "# 6. 한글이 깨지지 않고 csv파일을 제작\n",
    "df.to_csv(\"한솥도시락.csv\", encoding=\"euc-kr\")\n",
    "# 7. 크롬창을 종료!\n",
    "driver.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9780452d",
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
       "      <th>메뉴</th>\n",
       "      <th>가격</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>오븐구이 오리도시락</td>\n",
       "      <td>6,900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>열무 감초고추장 비빔밥</td>\n",
       "      <td>4,500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>열무 두부강된장 비빔밥</td>\n",
       "      <td>4,900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>핫 치즈 닭갈비 덮밥</td>\n",
       "      <td>5,900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>오리지널 치즈 닭갈비 덮밥</td>\n",
       "      <td>5,900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>88</th>\n",
       "      <td>무말랭이 무침</td>\n",
       "      <td>300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>89</th>\n",
       "      <td>한솥밥</td>\n",
       "      <td>1,000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>90</th>\n",
       "      <td>현미밥</td>\n",
       "      <td>1,700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>91</th>\n",
       "      <td>리얼 티라미수 찰떡</td>\n",
       "      <td>1,500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>92</th>\n",
       "      <td>리얼꿀 미니호떡</td>\n",
       "      <td>2,200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>93 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                메뉴     가격\n",
       "0       오븐구이 오리도시락  6,900\n",
       "1     열무 감초고추장 비빔밥  4,500\n",
       "2     열무 두부강된장 비빔밥  4,900\n",
       "3      핫 치즈 닭갈비 덮밥  5,900\n",
       "4   오리지널 치즈 닭갈비 덮밥  5,900\n",
       "..             ...    ...\n",
       "88         무말랭이 무침    300\n",
       "89             한솥밥  1,000\n",
       "90             현미밥  1,700\n",
       "91      리얼 티라미수 찰떡  1,500\n",
       "92        리얼꿀 미니호떡  2,200\n",
       "\n",
       "[93 rows x 2 columns]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1cd6a85a",
   "metadata": {},
   "source": [
    "## 선택자 한번에 복사해오는 방법\n",
    "- F12개발자 도구에서 원하는 요소 찾기\n",
    "- 마우스 우클릭 > copy > copy selector\n",
    "- [주의점]\n",
    "- copy selector를 사용시 무조건 선택한 하나만 가지고옴\n",
    "- 복수개를 요청할때는 선택자의 수정이 필요함\n",
    "- ex) li:nth-child(3) > a 는 하나만 요청 / 복수개로 변경시에는 li > a 로 수정!"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c63f9ab",
   "metadata": {},
   "source": [
    "## ActionChains\n",
    "- ActionChains 사용법!\n",
    "- 1. 내가 액션을 줄 모든 요소들을 수집\n",
    "- 2. ActionChains(\"브라우저\") 호출\n",
    "- 3. ActionChains(\"브라우저\").기능(요소명).기능(요소명).perform()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "0b2a34ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 이벤트를 묶어서 실행하는 라이브러리\n",
    "from selenium.webdriver import ActionChains"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "3be78538",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = wb.Chrome()\n",
    "driver.get(\"https://www.hsd.co.kr/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "7e6c2946",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 메뉴탭에 마우스를 올리기!\n",
    "# 2. 올린 상태에서 전체 메뉴를 클릭\n",
    "menu = driver.find_element(By.CSS_SELECTOR, \"#gnb > div.gnb_menu > ul > li:nth-child(3) > p > a\")\n",
    "allList = driver.find_element(By.CSS_SELECTOR, \"#gnb > div.gnb_menu > ul > li:nth-child(3) > div > ul > li:nth-child(1) > a\")\n",
    "ActionChains(driver).move_to_element(menu).click(allList).perform()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc5ab64d",
   "metadata": {},
   "source": [
    "#### 크롬창을 열 때 창 크기 옵션 지정하기!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "045e8cb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\AppData\\Local\\Temp\\ipykernel_15956\\884198000.py:3: DeprecationWarning: executable_path has been deprecated, please pass in a Service object\n",
      "  driver = wb.Chrome(\"C:/Users/AI/크롤링/chromedriver.exe\", chrome_options=options)\n",
      "C:\\Users\\AI\\AppData\\Local\\Temp\\ipykernel_15956\\884198000.py:3: DeprecationWarning: use options instead of chrome_options\n",
      "  driver = wb.Chrome(\"C:/Users/AI/크롤링/chromedriver.exe\", chrome_options=options)\n"
     ]
    }
   ],
   "source": [
    "options = wb.ChromeOptions()\n",
    "options.add_argument('--start-maximized')\n",
    "driver = wb.Chrome(\"C:/Users/AI/크롤링/chromedriver.exe\", chrome_options=options)\n",
    "driver.get(\"https://www.hsd.co.kr/\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc637ab6",
   "metadata": {},
   "source": [
    "#### 크롬창을 연 후 창 최대화"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "fb994a99",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = wb.Chrome()\n",
    "driver.get(\"https://www.hsd.co.kr/\")\n",
    "driver.maximize_window()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "21182e6a",
   "metadata": {},
   "source": [
    "## Full Code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "da377c5b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "더보기 완료~\n"
     ]
    }
   ],
   "source": [
    "# 크롬창을 연 후 창 최대화 version\n",
    "from selenium import webdriver as wb\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "import time\n",
    "from selenium.webdriver import ActionChains\n",
    "import pandas as pd\n",
    "\n",
    "driver = wb.Chrome()\n",
    "driver.get(\"https://www.hsd.co.kr/\")\n",
    "driver.maximize_window()\n",
    "menu = driver.find_element(By.CSS_SELECTOR, \"#gnb > div.gnb_menu > ul > li:nth-child(3) > p > a\")\n",
    "allList = driver.find_element(By.CSS_SELECTOR, \"#gnb > div.gnb_menu > ul > li:nth-child(3) > div > ul > li:nth-child(1) > a\")\n",
    "ActionChains(driver).move_to_element(menu).click(allList).perform()\n",
    "try:\n",
    "    while True:\n",
    "        btn = driver.find_element(By.CSS_SELECTOR, \"#btn_more > span > a\")\n",
    "        btn.click()\n",
    "        time.sleep(1)\n",
    "except:\n",
    "    print(\"더보기 완료~\")\n",
    "menu = driver.find_elements(By.CLASS_NAME, \"h.fz_03\")\n",
    "price = driver.find_elements(By.CSS_SELECTOR, \".item-price>strong\")\n",
    "menuList = []\n",
    "priceList = []\n",
    "for i in range(0, len(menu)):\n",
    "    menuList.append(menu[i].text)\n",
    "    priceList.append(price[i].text)   \n",
    "dic = {\"메뉴\" : menuList, \"가격\":priceList}\n",
    "df = pd.DataFrame(dic)\n",
    "df.to_csv(\"한솥도시락.csv\", encoding=\"euc-kr\")\n",
    "driver.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "97d6302f",
   "metadata": {},
   "source": [
    "## 화면에 크롬창이 안보이게 실행(백그라운드 실행)\n",
    "- 크롬옵션을 설정\n",
    "- 크롬드라이버의 경로를 반드시 명시!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7bf872b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\AppData\\Local\\Temp\\ipykernel_10128\\1003056959.py:3: DeprecationWarning: executable_path has been deprecated, please pass in a Service object\n",
      "  driver = wb.Chrome(executable_path=\"C:/Users/AI/크롤링/chromedriver.exe\",chrome_options= options)\n",
      "C:\\Users\\AI\\AppData\\Local\\Temp\\ipykernel_10128\\1003056959.py:3: DeprecationWarning: use options instead of chrome_options\n",
      "  driver = wb.Chrome(executable_path=\"C:/Users/AI/크롤링/chromedriver.exe\",chrome_options= options)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "더보기 완료~\n",
      "               상품명     가격\n",
      "0       오븐구이 오리도시락  6,900\n",
      "1     열무 감초고추장 비빔밥  4,500\n",
      "2     열무 두부강된장 비빔밥  4,900\n",
      "3      핫 치즈 닭갈비 덮밥  5,900\n",
      "4   오리지널 치즈 닭갈비 덮밥  5,900\n",
      "..             ...    ...\n",
      "88         무말랭이 무침    300\n",
      "89             한솥밥  1,000\n",
      "90             현미밥  1,700\n",
      "91      리얼 티라미수 찰떡  1,500\n",
      "92        리얼꿀 미니호떡  2,200\n",
      "\n",
      "[93 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "options = wb.ChromeOptions()\n",
    "options.add_argument(\"headless\")\n",
    "driver = wb.Chrome(executable_path=\"C:/Users/AI/크롤링/chromedriver.exe\",chrome_options= options)\n",
    "driver.get(\"https://www.hsd.co.kr/menu/menu_list\")\n",
    "try :\n",
    "    while True :\n",
    "        btn = driver.find_element(By.CSS_SELECTOR,\"#btn_more > span > a\")\n",
    "        btn.click()\n",
    "        time.sleep(1)\n",
    "except :\n",
    "    print(\"더보기 완료~\")\n",
    "title = driver.find_elements(By.CLASS_NAME,\"h.fz_03\")\n",
    "price = driver.find_elements(By.CSS_SELECTOR,\".item-price > strong\")\n",
    "titleList = []\n",
    "priceList = []\n",
    "for i in range(len(title)) :\n",
    "    titleList.append(title[i].text)\n",
    "    priceList.append(price[i].text)\n",
    "dic = {\"상품명\":titleList, \"가격\" : priceList}\n",
    "print(pd.DataFrame(dic))\n",
    "driver.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4114a99b",
   "metadata": {},
   "source": [
    "##### "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6e0acbe4",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\AppData\\Local\\Temp\\ipykernel_10128\\744508836.py:9: DeprecationWarning: executable_path has been deprecated, please pass in a Service object\n",
      "  driver = wb.Chrome(executable_path=\"C:/Users/AI/크롤링/chromedriver.exe\", chrome_options = options)\n",
      "C:\\Users\\AI\\AppData\\Local\\Temp\\ipykernel_10128\\744508836.py:9: DeprecationWarning: use options instead of chrome_options\n",
      "  driver = wb.Chrome(executable_path=\"C:/Users/AI/크롤링/chromedriver.exe\", chrome_options = options)\n"
     ]
    },
    {
     "ename": "MoveTargetOutOfBoundsException",
     "evalue": "Message: move target out of bounds\n  (Session info: headless chrome=103.0.5060.114)\nStacktrace:\nBacktrace:\n\tOrdinal0 [0x00FF6463+2188387]\n\tOrdinal0 [0x00F8E461+1762401]\n\tOrdinal0 [0x00EA3C40+801856]\n\tOrdinal0 [0x00F04F4A+1199946]\n\tOrdinal0 [0x00EEC7DC+1099740]\n\tOrdinal0 [0x00EFCC22+1166370]\n\tOrdinal0 [0x00EEC5F6+1099254]\n\tOrdinal0 [0x00EC6BE0+945120]\n\tOrdinal0 [0x00EC7AD6+948950]\n\tGetHandleVerifier [0x012971F2+2712546]\n\tGetHandleVerifier [0x0128886D+2652765]\n\tGetHandleVerifier [0x0108002A+520730]\n\tGetHandleVerifier [0x0107EE06+516086]\n\tOrdinal0 [0x00F9468B+1787531]\n\tOrdinal0 [0x00F98E88+1805960]\n\tOrdinal0 [0x00F98F75+1806197]\n\tOrdinal0 [0x00FA1DF1+1842673]\n\tBaseThreadInitThunk [0x76FE6739+25]\n\tRtlGetFullPathName_UEx [0x77168FEF+1215]\n\tRtlGetFullPathName_UEx [0x77168FBD+1165]\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mMoveTargetOutOfBoundsException\u001b[0m            Traceback (most recent call last)",
      "Input \u001b[1;32mIn [11]\u001b[0m, in \u001b[0;36m<cell line: 14>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     12\u001b[0m menu \u001b[38;5;241m=\u001b[39m driver\u001b[38;5;241m.\u001b[39mfind_element(By\u001b[38;5;241m.\u001b[39mCSS_SELECTOR, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m#gnb > div.gnb_menu > ul > li:nth-child(3) > p > a\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     13\u001b[0m allList \u001b[38;5;241m=\u001b[39m driver\u001b[38;5;241m.\u001b[39mfind_element(By\u001b[38;5;241m.\u001b[39mCSS_SELECTOR, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m#gnb > div.gnb_menu > ul > li:nth-child(3) > div > ul > li:nth-child(1) > a\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m---> 14\u001b[0m \u001b[43mActionChains\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdriver\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmove_to_element\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmenu\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mclick\u001b[49m\u001b[43m(\u001b[49m\u001b[43mallList\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mperform\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m     15\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m     16\u001b[0m     \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\common\\action_chains.py:78\u001b[0m, in \u001b[0;36mActionChains.perform\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     74\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mperform\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[0;32m     75\u001b[0m     \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m     76\u001b[0m \u001b[38;5;124;03m    Performs all stored actions.\u001b[39;00m\n\u001b[0;32m     77\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m---> 78\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mw3c_actions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mperform\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\common\\actions\\action_builder.py:88\u001b[0m, in \u001b[0;36mActionBuilder.perform\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     86\u001b[0m         enc[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mactions\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mappend(encoded)\n\u001b[0;32m     87\u001b[0m         device\u001b[38;5;241m.\u001b[39mactions \u001b[38;5;241m=\u001b[39m []\n\u001b[1;32m---> 88\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdriver\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[43mCommand\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mW3C_ACTIONS\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43menc\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:435\u001b[0m, in \u001b[0;36mWebDriver.execute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    433\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcommand_executor\u001b[38;5;241m.\u001b[39mexecute(driver_command, params)\n\u001b[0;32m    434\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m response:\n\u001b[1;32m--> 435\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43merror_handler\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcheck_response\u001b[49m\u001b[43m(\u001b[49m\u001b[43mresponse\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    436\u001b[0m     response[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_unwrap_value(\n\u001b[0;32m    437\u001b[0m         response\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    438\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m response\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py:247\u001b[0m, in \u001b[0;36mErrorHandler.check_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    245\u001b[0m         alert_text \u001b[38;5;241m=\u001b[39m value[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124malert\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m    246\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace, alert_text)  \u001b[38;5;66;03m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[39;00m\n\u001b[1;32m--> 247\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace)\n",
      "\u001b[1;31mMoveTargetOutOfBoundsException\u001b[0m: Message: move target out of bounds\n  (Session info: headless chrome=103.0.5060.114)\nStacktrace:\nBacktrace:\n\tOrdinal0 [0x00FF6463+2188387]\n\tOrdinal0 [0x00F8E461+1762401]\n\tOrdinal0 [0x00EA3C40+801856]\n\tOrdinal0 [0x00F04F4A+1199946]\n\tOrdinal0 [0x00EEC7DC+1099740]\n\tOrdinal0 [0x00EFCC22+1166370]\n\tOrdinal0 [0x00EEC5F6+1099254]\n\tOrdinal0 [0x00EC6BE0+945120]\n\tOrdinal0 [0x00EC7AD6+948950]\n\tGetHandleVerifier [0x012971F2+2712546]\n\tGetHandleVerifier [0x0128886D+2652765]\n\tGetHandleVerifier [0x0108002A+520730]\n\tGetHandleVerifier [0x0107EE06+516086]\n\tOrdinal0 [0x00F9468B+1787531]\n\tOrdinal0 [0x00F98E88+1805960]\n\tOrdinal0 [0x00F98F75+1806197]\n\tOrdinal0 [0x00FA1DF1+1842673]\n\tBaseThreadInitThunk [0x76FE6739+25]\n\tRtlGetFullPathName_UEx [0x77168FEF+1215]\n\tRtlGetFullPathName_UEx [0x77168FBD+1165]\n"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver as wb\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "import time\n",
    "from selenium.webdriver import ActionChains\n",
    "import pandas as pd\n",
    "options = wb.ChromeOptions()\n",
    "options.add_argument(\"headless\")\n",
    "driver = wb.Chrome(executable_path=\"C:/Users/AI/크롤링/chromedriver.exe\", chrome_options = options)\n",
    "driver.get(\"https://www.hsd.co.kr/\")\n",
    "driver.maximize_window()\n",
    "menu = driver.find_element(By.CSS_SELECTOR, \"#gnb > div.gnb_menu > ul > li:nth-child(3) > p > a\")\n",
    "allList = driver.find_element(By.CSS_SELECTOR, \"#gnb > div.gnb_menu > ul > li:nth-child(3) > div > ul > li:nth-child(1) > a\")\n",
    "ActionChains(driver).move_to_element(menu).click(allList).perform()\n",
    "try:\n",
    "    while True:\n",
    "        btn = driver.find_element(By.CSS_SELECTOR, \"#btn_more > span > a\")\n",
    "        btn.click()\n",
    "        time.sleep(1)\n",
    "except:\n",
    "    print(\"더보기 완료~\")\n",
    "menu = driver.find_elements(By.CLASS_NAME, \"h.fz_03\")\n",
    "price = driver.find_elements(By.CSS_SELECTOR, \".item-price>strong\")\n",
    "menuList = []\n",
    "priceList = []\n",
    "for i in range(0, len(menu)):\n",
    "    menuList.append(menu[i].text)\n",
    "    priceList.append(price[i].text)   \n",
    "dic = {\"메뉴\" : menuList, \"가격\":priceList}\n",
    "pd.DataFrame(dic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e0baad4",
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
