from django.db.models import Model, CharField
from django.core.validators import RegexValidator
import hashlib
import hmac
from django.utils.encoding import force_bytes
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class AuthenticatedMessage(Model):
    message = CharField(max_length=100)
    hash_value = CharField(max_length=64, validators=[RegexValidator('[0-9a-f]{64}')])

    def clean(self):
        hmac_function = hmac.new(
            b'frown canteen mounted carve',
            msg=force_bytes(self.message),
            digestmod=hashlib.sha256)
        hash_value = hmac_function.hexdigest()
        if not hmac.compare_digest(hash_value, self.hash_value):
            raise ValidationError(_('Message not authenticated'),
                                  code='msg_not_auth')

    class Meta:
        permissions = [
            ('send_authenticatedmessage', 'Can send msgs'),
            ('receive_authenticatedmessage', 'Can receive msgs'),
        ]
