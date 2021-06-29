# Mission-to-Mars

## Overview of Project 

### Purpose

The purpose of this analysis is to build a web-application that gives information on Mars, which is updated with a click of a button.

### Resources used
- Websites scraped : https://redplanetscience.com, https://spaceimages-mars.com, https://galaxyfacts-mars.com, https://marshemispheres.com
- Software : Python 3.7.9, Jupyter Notebook 6.1.4, Pandas 1.1.3, Anaconda 1.7.2, flask 1.1.2, Bootstrap 3, MongoDB 4.4, Beautiful Soup-4, Splinter 0.14.0


## Results

The web-application displayes news related to Mars along with a photograph the shows a sliced section of Mars's surface. This information is updated by clicking a button that says "Scrape New Data".\
A table comparing facts between Earth and Mars is also given.\
Four hemispheres of Mars were obtained, along with their titles, and stored in a list of dictionaries, as shown below.

On the web-app, their display was changed to four smaller thumbnails side by side, using Bootstrap. Any of the hemispheres pictures may be clicked to view a larger sized photograph in a separate window.

The web-application is responsive to devices of different sizes, like an ipad or iphone or desktop.

Display on a desktop screen:

Display on a ipad screen:




## Summary 

Beautiful Soup 4 was used for scraping the various websites to obtain the information. This process was automated using Splinter.\
The scraped information was first stored in a noSQL database MongoDB named mars_app, in a collection called mars. This was updated each time new informataion was scraped, and the latest update was presented in a web-application using flask. HTML components and Bootstrap were used to design the web-app.

The user may scrape new information by the click of a button in the web-app, and the latest mars news is displayed.

Picture showing updated information in mars document in mars_app mongo db.

