from datetime import date
from views import Home, About


def secret_front(request):
    request['data'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Home(),
    '/about/': About(),
}
