# create view for homepage and link it to the urls
# separate view for homepage therefore views.py file created inside simplesocial project folder

from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
