# Skribe
=========

Livemint Scraping Task
======================
Approach:
--------
For Livemint, we used Scrapy to extract article information such as the URL, title, author name, author URL, content, and published date. Initially, we inspected the website’s structure to locate the required elements, using browser developer tools to identify the tags and classes containing the necessary data. After carefully mapping the article data to their respective HTML elements, we set up Scrapy spiders to navigate through multiple pages and retrieve articles in bulk.

Challenges Faced:
----------------
The primary challenge with Livemint was dealing with dynamic content loading. Some elements were not immediately available in the HTML source, which caused missing data in our initial attempts. We had to refine our XPath selectors and CSS queries to ensure consistent data extraction. Additionally, we struggled with pagination, as the website’s pagination system was slightly complex. Debugging this part required trial and error, modifying the crawler several times before successfully fetching article data across pages. Despite the setbacks, we managed to extract clean and structured data.

=============================================================================================================================================================================

Economic Times Scraping Task
============================
Approach:
--------
For the Economic Times, the process was somewhat similar but posed additional complexities. The site had multiple types of articles (e.g., news, opinions) with different page structures, so we customized our Scrapy spider to handle variations in HTML layout. We built logic to distinguish between article types and extract data accordingly. This involved implementing conditional scraping based on the presence of certain tags or attributes that indicated the type of page we were dealing with.

Challenges Faced:
----------------
The biggest challenge here was the inconsistency in HTML structures between different sections of the site. Articles would sometimes have missing author information or differently structured content. We had to write extra conditions in the code to handle these inconsistencies. There were also problems with timeouts and response failures, which led us to adjust the download delay and retry mechanisms in Scrapy. These adjustments greatly improved the stability of our scraper, but it took significant effort to debug the issues, and several rounds of code refinement were needed to get reliable results.

=============================================================================================================================================================================

Telegraf Scraping Task
=====================
Approach:
--------
For Telegraf, we initially followed the same method of using Scrapy to crawl and extract article data. This included setting up a spider to target articles across multiple sections, identifying the HTML tags for the title, author, content, and date, and handling pagination to access articles across multiple pages.

Challenges Faced:
----------------
Telegraf presented some unexpected challenges. In the initial attempts, our scraper returned empty entries for several articles despite correctly locating the relevant HTML tags in our inspection phase. After extensive debugging, we realized that some pages were being served with content protection measures, such as anti-scraping scripts, that prevented data extraction. To overcome this, we made minor adjustments in request handling and tweaked Scrapy’s settings to minimize detection as a bot. Another issue was inconsistent data formats for published dates, which required custom date parsing logic.

Overall, debugging and refining the spider for Telegraf took considerable time and effort. Several iterations were needed, but in the end, we were able to extract valid data without any significant loss.

==============================================================================================================================================================================
