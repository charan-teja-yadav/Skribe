import scrapy

class EconomicsSpider(scrapy.Spider):
    name = "economics"
    start_urls = ['https://economictimes.indiatimes.com/']

    def parse(self, response):
        # Extract links to individual articles from the main page
        for article in response.css('a[href*="/news/"]'):
            article_url = article.css('::attr(href)').get()
            if article_url:
                # Follow the article URL and parse the article's content
                yield response.follow(article_url, self.parse_article)

        # Pagination: Find the link to the next page and follow it
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        # Extract article details
        title = response.css('h1::text').get()
        author_name = response.css('span.author a::text').get()
        author_url = response.css('span.author a::attr(href)').get()
        article_content = ' '.join(response.css('div.articleContent p::text').getall())
        published_date = response.css('span.date::text').get()

        # Output the scraped data
        yield {
            'Article URL': response.url,
            'Title': title,
            'Author Name': author_name,
            'Author URL': author_url,
            'Article Content': article_content,
            'Published Date': published_date,
        }
