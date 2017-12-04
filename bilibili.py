# coding: utf-8
# Go to the bilibili.com and get the URL of top 100 videos

"""
only for testing;
ver 0.01;
2017-12-4;
397174562@qq.com;
"""


from bs4 import BeautifulSoup
import requests
from selenium import webdriver


# LANDING PAGE: fun--鬼畜, 其他的字面意思理解即可
URL_fun = "https://www.bilibili.com/ranking?spm_id_from=333.334.ranking_kichiku.8#!/origin/119/0/3/"
URL_music = "https://www.bilibili.com/ranking?spm_id_from=333.334.ranking_kichiku.8#!/origin/3/0/3/"
URL_game = "https://www.bilibili.com/ranking?spm_id_from=333.334.ranking_kichiku.8#!/origin/4/0/3/"
URL_dance = "https://www.bilibili.com/ranking?spm_id_from=333.334.ranking_kichiku.8#!/origin/129/0/3/"


# define lists to store all URLs for each category top100 page
list_fun = list()
list_music = list()
list_game = list()
list_dance = list()

FILE = 'data.txt'     # all info written to data.txt


def get_target_info(url, target_list):
    driver = webdriver.Chrome()
    cookie = driver.get_cookies()
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')

    # print(soup.div(name='div', attrs={'class': 'num'}))   # Testing

    nums = soup.find_all(name='div', attrs={'class': 'num'})
    titles = soup.find_all(name='div', attrs={'class': 'title'})
    authors = soup.find_all(name='span', attrs={'class': 'data-box author'})
    avs = soup.find_all(name='i', attrs={'class': 'watch-later'})

    for i in range(100):
        num = nums[i].text
        title = titles[i].text
        author = authors[i].text
        av = 'www.bilibili.com/video/av' + str(avs[i])[8:-26]

        target_list.append([num, av, title, author])

    with open(FILE, 'a') as txt_file:
        for data in target_list:
            txt_file.write(str(data) + '\n')


get_target_info(URL_fun, list_fun)
get_target_info(URL_music, list_music)
get_target_info(URL_game, list_game)
get_target_info(URL_dance, list_dance)
