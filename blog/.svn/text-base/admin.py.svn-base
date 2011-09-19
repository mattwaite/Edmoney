from django.contrib import admin
from stimulustracker.blog.models import Post
 
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    prepopulated_fields = {'title_slug': ('title',)}
    raw_id_fields = ['schools_in_post', 'districts_in_post', 'states_in_post']
    list_display = ['title', 'author', 'active']
    list_filter = ['publication_date']
    list_editable = ['active']
    date_hierarchy = 'publication_date'
    fieldsets = (
        ('The Post', {
            'fields': ('title', 'title_slug', 'author', 'body')
        }),
        ('Post administration', {
            'fields': ('publication_date', 'active', 'enable_comments')        
        }),
        ('Tagging', {
            'fields': ('schools_in_post', 'districts_in_post', 'states_in_post')        
        }),
    ) 
    class Media:
       js = ('/media/js/tiny_mce/tiny_mce.js',
             '/media/js/tiny_mce/textareas.js',)

admin.site.register(Post, PostAdmin)

from django.contrib.comments.moderation import CommentModerator, moderator
from django.contrib.sites.models import Site
from django.conf import settings

class PostModerator(CommentModerator):
    email_notification = True
    enable_field = 'enable_comments'
    def check_spam(self, request, comment, key, blog_url=None, base_url=None):
        try:
            from akismet import Akismet
        except:
            return False

        if blog_url is None:
            blog_url = 'http://%s/' % Site.objects.get_current().domain

        ak = Akismet(
            key=settings.AKISMET_API_KEY,
            blog_url=blog_url
        )

        if base_url is not None:
            ak.baseurl = base_url

        if ak.verify_key():
            data = {
                'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
                'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                'referrer': request.META.get('HTTP_REFERER', ''),
                'comment_type': 'comment',
                'comment_author': comment.user_name.encode('utf-8'),
            }

            if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
                return True

        return False

    def allow(self, comment, content_object, request):
        allow = super(PostModerator, self).allow(comment, content_object, request)

        # change this depending on which spam provider you want to use
        spam = self.check_spam(request, comment,
            key=settings.AKISMET_API_KEY,
        ) or self.check_spam(request, comment,
            key=settings.TYPEPAD_ANTISPAM_API_KEY,
            base_url='api.antispam.typepad.com/1.1/'
        )

        return not spam and allow

moderator.register(Post, PostModerator)
