#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[5]:


#grab titles and bodies
titles = soup.find('div', class_='content_title').text
bodies = soup.find('div', class_='article_teaser_body').text




# In[6]:


#featured image url
featured_image_url1 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(featured_image_url1)


# In[7]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[8]:


image_url = soup.find('article', class_='carousel_item')['style']
image_url


# In[9]:


split_url = image_url.split("'")
print(split_url[1])


# In[10]:


featured_image_url = 'https://www.jpl.nasa.gov' + split_url[1]
featured_image_url


# In[11]:


#mars facts
facts_url = "https://space-facts.com/mars/"
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[12]:


tables = pd.read_html(facts_url)
tables[1]


# In[13]:


df = tables[1]
df.set_index('Mars - Earth Comparison')


# In[14]:


html_table = df.to_html()
html_table


# In[16]:


#mars hemispheres
hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[17]:


browser.visit(hemisphere_url)


# In[18]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[19]:


hemisphere_image_urls = []

hemisphere_titles = soup.find_all('div', class_='item')

#loop through pulled data and append to empty list
for junk in hemisphere_titles:
    title = junk.find('h3').text
    
    half_image_url = junk.find('a', class_='itemLink product-item')['href']
    
    browser.visit('https://astrogeology.usgs.gov/' + half_image_url)
    
    half_img_html = browser.html
    
    soup = BeautifulSoup(half_img_html,'html.parser')
    
    img_url = 'https://astrogeology.usgs.gov/' + soup.find('img', class_='wide-image')['src']
    
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    
hemisphere_image_urls


# In[20]:
empty = []
def scrape():
    empty.append(titles)
    empty.append(bodies)
    empty.append(featured_image_url)
    empty.append(html_table)
    empty.append(hemisphere_image_urls)
scrape()
empty
