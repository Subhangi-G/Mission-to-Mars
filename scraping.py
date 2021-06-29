# Import Splinter and BeautifulSoup
from splinter import Browser 
from bs4 import BeautifulSoup as soup 
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager 

def scrape_all():
    # Initiate headless driver for deployment.
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary.
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": mars_hemispheres(browser),
    }
    print(data)
    # Stop webdriver and return data. 
    browser.quit()
    return data

# Article and Summary about Mars (latest)

def mars_news(browser):
    # Scrape Mars News
    # Visit the Mars Nasa News site 
    #url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser. 
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        
        # Use the parent element to find the paragraph text. 
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None
    
    return news_title, news_p

# JPL Space Image Featured Image

def featured_image(browser):
    # Visit URL
    #url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Find and click the full image button. 
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup.
    html = browser.html 
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url. 
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL.
    #img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}' 
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

# Mars Facts
def mars_facts():
    # Add try/except for error handling
    try:
        # use 'read_html' to scrape the facts table into a dataframe.
        #df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0] 
        df = pd.read_html('https://galaxyfacts-mars.com/')[0]
       
    except BaseException:
        return None

    # Assign columns and set index of dataframe.
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap. 
    return df.to_html(classes="table table-striped")

# Mars Hemispheres
def mars_hemispheres(browser):
    
    # 1. Use browser to visit the URL
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    # Create a for loop to iterate through the tags.
    for i in range (3,7):
        # Create an empty dictionary to store the current image url and title.
        hemisphere = {}

        # Finding and clicking a hemisphere link.
        img_thumb = browser.find_by_tag('img')[i]
        img_thumb.click()

        # Parse the resulting html with soup.
        html = browser.html
        hemisphere_soup = soup(html, 'html.parser')

        # Find the relative url for the image
        img_rel_url = hemisphere_soup.find('div', class_="downloads").ul.li.a.get('href')

        # Create the absolute url for the image
        img_url = f'https://marshemispheres.com/{img_rel_url}'

        # Retrieve the title.
        title = hemisphere_soup.find('div', class_="cover").h2.text

        # Save the hemisphere url and the title to the dictionary.
        hemisphere['img_url']= img_url
        hemisphere['title'] = title
        
        # Append the hemisphere dictionary to the list.
        hemisphere_image_urls.append(hemisphere)

        # Navigate back to the beginning.
        browser.back()

    return hemisphere_image_urls

      
if __name__ == "__main__" :
    
    # If running as script print scraped data
    print(scrape_all())

