from rest_framework.routers import SimpleRouter

from . views import BooksView, CategoryView

router = SimpleRouter()
router.register('books', BooksView, base_name='all_books')
router.register('categories', CategoryView, base_name='all_categories')

urlpatterns = router.urls
