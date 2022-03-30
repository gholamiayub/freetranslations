import re

from django import template


register = template.Library()

@register.filter
def url_to_domain(value):
    """Remove scheme and domain extension from the given string"""
    url = re.compile(r"https?://(www\.)?")
    url = url.sub('', value).strip().strip('/')

    return url
