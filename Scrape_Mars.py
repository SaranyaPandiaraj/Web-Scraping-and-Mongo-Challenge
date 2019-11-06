from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Users/Saranya/Downloads/chromedriver_win32/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)
    
def scrape_info():
    browser = init_browser()
     
    #NASA Mars News 
    #Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
    NASA_Mars_url ="https://mars.nasa.gov/news/"
    browser.visit(NASA_Mars_url)

    NASA_Mars_html = browser.html
    NASA_Mars_soup = BeautifulSoup(NASA_Mars_html, 'html.parser')

    NASA_Mars_News_Title = NASA_Mars_soup.find('div', class_='content_title').text
    NASA_Mars_News_Para = NASA_Mars_soup.find('div', class_='article_teaser_body').text

    #Checking/Displaying the Title Content
    print(NASA_Mars_News_Title)

    #Checking/Displaying the Para Content
    print(NASA_Mars_News_Para)

    ###  JPL Mars Space Images - Featured Image </ins>

    
    # Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

    # Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

    # Make sure to find the image url to the full size `.jpg` image.

    # Make sure to save a complete url string for this image.
    

    JPL_Mars_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(JPL_Mars_url)

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)
    browser.click_link_by_partial_text('more info')
    time.sleep(1)
    JPL_Mars_html = browser.html
    JPL_Mars_soup = BeautifulSoup(JPL_Mars_html, 'html.parser')
    time.sleep(1)
    Full_Image_Url = JPL_Mars_soup.find('figure', class_='lede').a['href']
    print(Full_Image_Url)

    Base_Url = "https://www.jpl.nasa.gov"
    Featured_Image_url = Base_Url + Full_Image_Url
    print(Featured_Image_url)

    ###  Mars Weather </ins>

    # Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.
    

    Mars_Weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(Mars_Weather_url)

    Mars_Weather_html = browser.html
    Mars_Weather_soup = BeautifulSoup(Mars_Weather_html, 'html.parser')

    Mars_Weather = Mars_Weather_soup.find('p', class_='TweetTextSize').text
    print(Mars_Weather)

    ###  Mars Facts </ins>

    # Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

    # Use Pandas to convert the data to a HTML table string.

    Mars_Facts_url = "http://space-facts.com/mars/"

    Mars_Facts_table = pd.read_html(Mars_Facts_url)
    Mars_Facts_table

    Mars_Facts_table_df = Mars_Facts_table[0]
    Mars_Facts_table_df.columns = ["Properties", "Value"]
    Mars_Facts_table_df

    Mars_Facts_table_html = Mars_Facts_table_df.to_html(index=False)

    Mars_Facts_table_html

    ###  Mars Hemispheres </ins>

    # Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

    # You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

    # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

    # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

    Mars_Hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(Mars_Hemispheres_url)

    Mars_Hemispheres_html = browser.html
    Mars_Hemispheres_soup = BeautifulSoup(Mars_Hemispheres_html, 'html.parser')

    Products = Mars_Hemispheres_soup.find_all('div', class_='item')
    print(Products)

    #Creating Empty list to store the Image Title & Image URL
    Prod_Title_Img_Url = []

    #Creating a loop for retrieving the title and img urls'
    for prod in Products:
        
        Title = prod.find("h3").text
        
        Prod_Img_Url = prod.find('a', class_='itemLink product-item')["href"]
        
        Base_Url = "https://astrogeology.usgs.gov"
        
        browser.visit(Base_Url + Prod_Img_Url)
        
        Prod_Img_Url_html = browser.html
        
        Prod_Img_Url_soup = BeautifulSoup(Prod_Img_Url_html,"html.parser")
        
        Full_Resolution_Image_Url = Base_Url + Prod_Img_Url_soup.find("img",class_="wide-image")["src"]
        
        Prod_Title_Img_Url.append({"Title":Title,"Img_url":Full_Resolution_Image_Url})

    #Displaying Prod_Title_Img_Url
    Prod_Title_Img_Url
    
    
    #Storing all the Scrapped Data's into Dictionary
    
    Mars_Data = {
        "NASA_Mars_News_Title": NASA_Mars_News_Title,
        "NASA_Mars_News_Para": NASA_Mars_News_Para,
        "Featured_Image_url": Featured_Image_url,
        "Mars_Weather": Mars_Weather,
        "Mars_Facts_table_html": Mars_Facts_table_html,
        "Prod_Title_Img_Url": Prod_Title_Img_Url
                }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return Mars_Data    