from atlant_framework.templator import render


class Home:
    def __call__(self, request):
        return '200 ok', render('home.html', data=request.get('data', None))


class About:
    def __call__(self, request):
        return '200 ok', render('about.html')