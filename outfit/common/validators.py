from django.core.exceptions import ValidationError
import re

VALIDATE_ONLY_EXCEPTION_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'


def validator_only_letters(value):
    if not re.match("[A-Za-z]", value):
        raise ValidationError(VALIDATE_ONLY_EXCEPTION_MESSAGE)
