{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cf92c981",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver as wb\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "import time\n",
    "# 파일시스템을 위한 라이브러리(파일, 폴더를 생성, 삭제)\n",
    "import os\n",
    "# 이미지의 url값을 파일로 변형시켜주는 라이브러리\n",
    "from urllib.request import urlretrieve"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f91e806b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 크롬을 통해서 네이버 메인사이트로 이동\n",
    "driver = wb.Chrome()\n",
    "driver.get(\"http://www.naver.com\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "bf09eac3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. 검색창에 원하는 검색어 입력\n",
    "# 2.1 검색까지 진행!\n",
    "search = driver.find_element(By.ID, \"query\")\n",
    "search.send_keys(\"진로두꺼비\")\n",
    "btn = driver.find_element(By.ID, \"search_btn\")\n",
    "btn.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0d0f594e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#3. 이미지 탭 클릭!\n",
    "img_btn = driver.find_element(By.CSS_SELECTOR, \"#lnb > div.lnb_group > div > ul > li:nth-child(2) > a\")\n",
    "img_btn.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40a66e72",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 스크롤 코드! (화면구성 더 많아진다, 로딩받는 데이터 증가)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b922ccd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. 이미지 태그들을 수집\n",
    "# 이유는? 이미지 태그 속에 존재하는 src만 추출하기 위해서!\n",
    "img = driver.find_elements(By.CSS_SELECTOR, \"._image._listImage\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "df45f8f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fdnvefa72aowie.cloudfront.net%2Forigin%2Farticle%2F202204%2Fb44051addc9ed22fac722fd0277af55ba42f638c93c2bffbea07a9fed10c6c2e.webp%3Fq%3D95%26s%3D1440x1440%26t%3Dinside&type=a340'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 나 img리스트의 0번째 데이터에서 src 속성을 가져다줘!\n",
    "# 속성을 수집할 때는 get_attribute(\"속성\")\n",
    "img[0].get_attribute(\"src\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e357d8d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# src만 담아줄 리스트 새로 제작\n",
    "srcList = []\n",
    "for i in img:\n",
    "    srcList.append(i.get_attribute(\"src\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b2f8b901",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://search.pstatic.net/sunny/?src=https%3A%2F%2Fdnvefa72aowie.cloudfront.net%2Forigin%2Farticle%2F202204%2Fb44051addc9ed22fac722fd0277af55ba42f638c93c2bffbea07a9fed10c6c2e.webp%3Fq%3D95%26s%3D1440x1440%26t%3Dinside&type=a340',\n",
       " 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fdnvefa72aowie.cloudfront.net%2Forigin%2Farticle%2F202111%2F1d89366cee8d538a94a6eadbfdd930911d61d63b37e72e6f1f27aeddbe74d941.webp%3Fq%3D95%26s%3D1440x1440%26t%3Dinside&type=a340',\n",
       " 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MTdfMjgw%2FMDAxNjIxMjUzMDUyNjAz.VURB5Ou62mIophiSi8ODMeG9sJnTHZElziaWlYjN150g.0S7q1gmhhQIHDT7rJohO7QOG_tIg12YnFFnI9lf4QX8g.JPEG.macchiato2%2FIMG_5819.jpg&type=a340',\n",
       " 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fdnvefa72aowie.cloudfront.net%2Forigin%2Farticle%2F202109%2Ff57146b17d9576aee187ee19c4122e401fc81edd2651dc90d27746654df7d2b5.webp%3Fq%3D95%26s%3D1440x1440%26t%3Dinside&type=a340',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fdnvefa72aowie.cloudfront.net%2Forigin%2Farticle%2F202201%2Fbf6f03da15bf0b4c54f2bb85f7b072227e9a15338af1f3cfd71fff2cf7e4d2ac.webp%3Fq%3D95%26s%3D1440x1440%26t%3Dinside&type=a340',\n",
       " 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA4MDdfMTE2%2FMDAxNTk2NzcxODkxMjQ3.pmzA6CBGDxQPJYMiIcShbNv2A8zcVgGzbUNrspW6EvAg.T_r3-MRKqwxHm8u8-6sgIf07hNs1HlNESiTue6hjH2Mg.JPEG.vmflxl4331%2F20200807_123331.jpg&type=a340',\n",
       " 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA0MjFfMjg3%2FMDAxNjUwNTIwODU1NTU3._zyIuxvCAGM_3To2qMhw_vp8YFelHr8CUb37OCDBC0og.ydXfWOxtWl8IXtKUhPMusGCneTED7ZfovH6t9f5_iZog.JPEG.mlhyja82%2F1650520852901.jpg&type=a340',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20220625_51%2F1656085510663H8bV0_JPEG%2F57221356280585841_505194359.jpg&type=a340',\n",
       " 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fdnvefa72aowie.cloudfront.net%2Forigin%2Farticle%2F202205%2F8F9D23763B56D0D156854118FE9200112B432FA8CBC1BC4DC7B47FED66B69978.jpg%3Fq%3D95%26s%3D1440x1440%26t%3Dinside&type=a340',\n",
       " 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20210125_187%2F16115052602637IBVb_PNG%2F12641158972539934_278696982.png&type=a340',\n",
       " 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fdnvefa72aowie.cloudfront.net%2Forigin%2Farticle%2F202105%2F88359baaae40ba68da28510a47c02388556d8864bd2ae5c27234269b2f209e28.webp%3Fq%3D95%26s%3D1440x1440%26t%3Dinside&type=a340',\n",
       " 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA2MThfMjI4%2FMDAxNTkyNDM2NTE2OTY2.PQ7IHBLf8ksVlNhK1HpRFRSiOJ6IFsCkesfDp0tm8Psg.obvkZ6dvOGaPh56xU6zgWugzV40M__WnFVXchtWZu9cg.JPEG.mimdesign%2F1592436516329.jpg&type=a340',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7',\n",
       " 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "srcList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "e0550521",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 이미지를 저장!\n",
    "# 바탕화면에 이미지 폴더를 생성\n",
    "# 바탕화면에 이미지라는 폴더가 없다면, 바탕화면에 이미지 폴더 만들어줘~\n",
    "if not os.path.isdir(\"C:/Users/AI/Desktop/이미지\"):\n",
    "    os.mkdir(\"C:/Users/AI/Desktop/이미지\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "fcb4b9af",
   "metadata": {},
   "outputs": [],
   "source": [
    "# url 값을 이미지 폴더에 저장\n",
    "cnt = 0\n",
    "for i in srcList:\n",
    "    urlretrieve(i, f\"C:/Users/AI/Desktop/이미지/img{cnt}.jpg\")\n",
    "    cnt +=1;\n",
    "    time.sleep(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65e6ca2c",
   "metadata": {},
   "source": [
    "### 이미지가 중간에 깨지는 이유는?\n",
    "- 이미지는 텍스트 파일보다 크기가 더 크기 때문에\n",
    "- 화면상에 스크롤을 통해서 더 많이 로딩 받기!\n",
    "- 1. 크롬실행\n",
    "- 2. 스크롤을 충분히 진행 // 화면구성\n",
    "- 3. img태그를 수집 // 태그수집\n",
    "- 4. img태그 속 src만 추출 // 데이터가공\n",
    "- 5. 파일로 저장 // 데이터활용"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b342070f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15b774c1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c2afc3a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a59c4f97",
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
