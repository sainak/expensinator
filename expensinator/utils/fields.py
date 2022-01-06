from django.db import models


class LCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()
