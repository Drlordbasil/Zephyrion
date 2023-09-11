Here's the refactored version of the Python script with the optimizations applied:

```python
from bs4 import BeautifulSoup
import requests

class ContentGenerator:
    def __init__(self):
        self.trending_topics = {"technology", "sports", "health"}

    def generate_content(self):
        html = requests.get("https://example.com").content
        soup = BeautifulSoup(html, 'lxml')

        trending_articles = self.scrape_articles(soup, "h2", "p")

        all_articles = api_call()  # Combined API call for all articles
        news_articles = [article for article in all_articles if article.source == "news"]
        blog_posts = [article for article in all_articles if article.source == "blog"]
        social_media_discussions = [article for article in all_articles if article.source == "social_media"]
        
        article = api_call()
        blog_post = api_call()
        social_media_post = api_call()

        for topic in self.trending_topics:
            if topic in trending_articles:
                optimized_article, optimized_blog_post = self.optimize_content(article, blog_post)

                self.publish_content(optimized_article, optimized_blog_post, social_media_post)

    def scrape_articles(self, soup, title_tag, content_tag):
        articles = soup.find_all("article")
        return [{"title": article.find(title_tag).text.strip(), "content": article.find(content_tag).text.strip()} for article in articles]

    def optimize_content(self, article, blog_post):
        # Content optimization logic
        return optimized_article, optimized_blog_post

    def publish_content(self, optimized_article, optimized_blog_post, social_media_post):
        platform = get_platform()

        if platform == "website":
            # Publish on website logic
            pass
        elif platform == "mobile_app":
            # Publish on mobile app logic
            pass
        elif platform == "social_media":
            # Publish on social media logic
            pass
        else:
            # Handle unsupported platform
            pass

content_generator = ContentGenerator()
content_generator.generate_content()
```

In the refactored version, the optimizations mentioned earlier are applied to improve the script's performance, readability, and maintainability.