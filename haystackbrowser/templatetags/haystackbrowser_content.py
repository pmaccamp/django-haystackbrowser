# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.simple_tag
def get_content_for_field(model, field):
    return model.get_content_for_field(field)