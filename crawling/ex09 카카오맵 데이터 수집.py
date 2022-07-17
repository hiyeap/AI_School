{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ac8d79ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver as wb\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b5105873",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = wb.Chrome()\n",
    "driver.get(\"https://map.kakao.com/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e2f6ca8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 검색창에 광주맛집 검색\n",
    "# 지도 설정 레이어를 클릭!\n",
    "layer = driver.find_element(By.ID, \"dimmedLayer\")\n",
    "layer.click()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c3fa3de8",
   "metadata": {},
   "source": [
    "### id나 클래스에(선택자에) .이나 # 기호가 들어가 있는 경우\n",
    "- 컴퓨터가 해석할 때 #(아이디), .(클래스)로 인식하기 때문에\n",
    "- 문자로 인식시키기 위해서 \\# or \\.으로 사용!\n",
    "- 문자로 \".\" , \"#\"으로 인식"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b32296a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 검색창 찾기\n",
    "search = driver.find_element(By.CSS_SELECTOR, \"#search\\.keyword\\.query\")\n",
    "search.send_keys(\"광주맛집\")\n",
    "search.send_keys(Keys.ENTER)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ff141421",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"1c70485d-9fab-43ed-88c9-807387120dc3\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"4e40e930-da08-4fdf-8ac1-6202a389a7da\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"d719dfff-0845-498c-9c55-808f19749d49\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"1ae6986b-2146-47f8-b0b8-a04faa410ee9\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"0e6b9d78-ec44-4eb4-b9f3-84420e577ce2\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"e5c6f830-d435-4629-9f9b-b37280c8cbc3\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"406c0840-699a-40b5-b16e-f17c5532e8da\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"e35f4481-284b-4907-a371-71ead52711a0\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"3043c60a-0d56-4a11-af07-d06d0bbc05a2\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"d9190300-4302-4d2d-83c0-125ae3d3a534\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"962dad44-fe88-4e6b-b63a-7be44a8d08e5\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"bb96e41c-8456-4a33-8281-ae4498000245\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"5f762f44-8418-40a3-9660-875112b6ea5c\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"d54d2dc8-2a22-4272-ba4e-9043b9599b90\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"1f90bb36-0f9b-436d-9152-4ef934e6a20a\")>,\n",
       " <selenium.webdriver.remote.webelement.WebElement (session=\"64eb1c3b57546b5c5bb4504ab0d98db6\", element=\"a9bc7112-fdc9-404b-9f16-b574111e8a3b\")>]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1페이지 가게이름 수집\n",
    "res = driver.find_elements(By.CSS_SELECTOR, \"a.link_name\")\n",
    "res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "0bd3c0cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'군자대한곱창 수완점'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "res[0].get_attribute(\"title\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ab83d8f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['군자대한곱창 수완점',\n",
       " '상무초밥 상무점',\n",
       " '영미오리탕',\n",
       " '송정떡갈비 1호점',\n",
       " '궁전제과 충장본점',\n",
       " '명화식육식당',\n",
       " '초돈',\n",
       " '나주식당',\n",
       " '황솔촌 상무점',\n",
       " '라라브레드 송정점',\n",
       " '미미원',\n",
       " '맥문동레스토랑',\n",
       " '마천루',\n",
       " '스트럭트',\n",
       " '황솔촌 수완점',\n",
       " '서울곱창']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 가게이름 리스트\n",
    "res_list = []\n",
    "for i in range(len(res)):\n",
    "    res_list.append(res[i].get_attribute(\"title\"))\n",
    "res_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "9c159d00",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 더보기버튼 클릭\n",
    "more = driver.find_element(By.CSS_SELECTOR, \"#info\\.search\\.place\\.more\")\n",
    "more.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "598f1672",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2페이지 가게이름 수집 & 다음페이지로 이동\n",
    "res = driver.find_elements(By.CSS_SELECTOR, \"a.link_name\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e063aee",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f47dacee",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c383ea58",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "322d55d1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da5f2024",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e99a7873",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "875ef586",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9204c601",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0486dee7",
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
