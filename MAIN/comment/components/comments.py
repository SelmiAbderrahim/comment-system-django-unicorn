from django_unicorn.components import UnicornView
from ..models import Author, Comment

class CommentsView(UnicornView):
    author: Author = None
    comments: Comment = None
    content: str = ""

    def mount(self):
        self.author = Author.objects.get(user=self.request.user)
        self.comments = Comment.objects.all()
        return super().mount()

    def submit(self):
        Comment.objects.create(
            author=self.author,
            content=self.content
        )
        #reset
        self.content = ""
        self.comments = Comment.objects.all()
