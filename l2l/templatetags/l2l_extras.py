from django import template
from datetime import datetime

register = template.Library()


@register.filter
def l2l_dt(value):

    """
    Detects if value is a datetime object. If it is, object is converted to a string that is formatted '%Y-%m-%d %H:%M:%S'.
    If value is a string,  we convert it to a datetime object and then perform the step mentioned above.
    """

    format = "%Y-%m-%d %H:%M:%S"

    if isinstance(value, datetime):
        return value.strftime(format)

    elif isinstance(value, str):
        dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        return dt.strftime(format)

    else:
        return "Hmm, seems something went wrong. We'll take a look at this ASAP"
        # Implement some sort of notifier here so devs know that a customer broke it :D
