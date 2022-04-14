from django.core.exceptions import ValidationError
import re

VALIDATE_ONLY_EXCEPTION_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'


def validator_only_letters(value):
    if not re.match("[A-Za-z]", value):
        raise ValidationError(VALIDATE_ONLY_EXCEPTION_MESSAGE)

#
# def max_size_file(max_size):
#     def validate(value):
#         filesize = value.file.size
#         if filesize > max_size * 1024 * 1024:
#             raise ValidationError(f"Max file size is {max_size}")
#
#     return validate
