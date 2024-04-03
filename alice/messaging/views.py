from django.views.generic.edit import CreateView
from models import AuthenticatedMessage


class CreateAuthenticatedMessageView(CreateView):
    model = AuthenticatedMessage
    fields = ['message', 'hash_value']
    success_url = '/'
