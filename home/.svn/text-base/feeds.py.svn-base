from django.contrib.syndication.feeds import Feed
from stimulustracker.blog.models import Post

class LatestEntries(Feed):
    title = "Edmoney.org blog posts"
    link = "/blog/"
    description = "The latest posts on Edmoney.org"
    def items(self):
        return Post.published_objects.order_by('-publication_date')[:10]