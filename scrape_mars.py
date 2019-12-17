#!/usr/bin/env python
# coding: utf-8



from bs4 import BeautifulSoup
import requests
import pandas as pd
from splinter import Browser
import time



def scrape_info():

    mars = {}
    url = "https://mars.nasa.gov/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_="content_title")
    results 



    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome')
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)




    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    slide_elem = news_soup.select_one('ul.item_list li.slide')




    slide_elem




    slide_elem.find("div", class_='content_title')




    news_title = slide_elem.find("div", class_='content_title').get_text()
    news_title
    mars["news_title"] = news_title




    news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
    news_p
    mars["news_paragraph"] = news_title




    browser = Browser('chrome')
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)
    # Optional delay for loading the page
    image = browser.find_by_id("full_image")
    image.click()
    time.sleep(5)
    newimage =  browser.find_link_by_partial_text('more info')
    newimage.click()
    time.sleep(5)



    soup = BeautifulSoup(browser.html, 'html.parser')
    result=soup.find('figure',class_="lede")
    featured_image_url="https://www.jpl.nasa.gov"+result.a.img["src"]
    featured_image_url
    mars["featured_image_url"] = featured_image_url




    url = "https://twitter.com/marswxreport?lang=en"
    browser = Browser('chrome')
    browser.visit(url)
    soup = BeautifulSoup(browser.html, 'html.parser')
    result=soup.find('div',class_="js-tweet-text-container")
    result.p.text
    mars_weather = result.p.text
    mars["weather"] = mars_weather




    df = pd.read_html('https://space-facts.com/mars/')[0]
    df.columns=['description', 'value']
    df.set_index('description', inplace=True)
    df




    mars_facts = df.to_html()
    mars["facts"] = mars_facts




    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser = Browser('chrome')
    browser.visit(url)
    hemisphere_image_urls = []
    links = browser.find_by_css("a.product-item h3")
    links
    for i in range(len(links)):
        hemisphere = {}
        # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css("a.product-item h3")[i].click()
        # Next, we find the Sample image anchor tag and extract the href
        sample_elem = browser.find_link_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
        # Get Hemisphere title
        hemisphere['title'] = browser.find_by_css("h2.title").text
        # Append hemisphere object to list
        hemisphere_image_urls.append(hemisphere)
        # Finally, we navigate backwards
        browser.back()




    hemisphere_image_urls




    mars["hemisphere"] = hemisphere_image_urls


    
    return mars
if __name__ == "__main__":
    print(scrape_info())



