# Static Web Crawler

The static web crawler intelligently crawls through the google play store home page to fetch the app details in CSV format.

The app details consists following key parameters:
-Publisher
-Category 
-Size 
-Rating
-Reviews
-Total downloads

The project is built using python 3.6. 
The BeautifulSoup library is used to parse the web page.
Multiprocessing and multi threading is used to parser the each applink on the web page which improved the performance by 200%.

With some tuning and tweaks, the same project can be used as non static web crawler.



