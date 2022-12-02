import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime

# source_link
#source_link = "https://kun.uz/uz/news/2022/12/01/uch-tomonlama-ittifoq-tashqi-kuchlar-qolidagi-ozbek-gazi-va-volodinning-hurmatsizligi-siyosatshunoslar-bilan-suhbat"
source_link = 'https://kun.uz/uz/news/2022/12/02/yei-davlatlari-rossiya-nefti-narxining-yuqori-chegarasi-60-dollar-bolishini-kelishib-olishdi'
#source_link = 'https://kun.uz/uz/news/2022/12/03/turkiyalik-sharhlovchi-jch-2022-oyini-tanaffusida-efirdan-chetlatildi'

access_datetime = datetime.datetime.now()


def get_data(link):

    # -----step 1

    # get the html text
    request = requests.get(source_link).text

    # soup
    soup = BeautifulSoup(request, 'html5lib')

    # main article
    article = soup.find('div', class_='single-layout__center slc')

    article.script.decompose()

    # article parts: get data
    article_body = article.find_all('p')

    content = ''

    for part in article_body:
        content = content + part.text

    # -----step 2: split p tags data
    word = content.split(' ')

    word_df = pd.Series(word)

    # -----step 3: most appearing words
    print(word_df.str.split(expand=True).stack().value_counts())

    # -----create csv file
    df = pd.DataFrame([link, access_datetime,
                       content, word], index=["source_link", "access_datetime", "content", "word"])

    df.to_csv('kunuz/kunuz.csv')


get_data(source_link)
