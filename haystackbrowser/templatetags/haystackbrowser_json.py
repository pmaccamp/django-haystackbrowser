# -*- coding: utf-8 -*-
from django import template
from json2html import json2html

register = template.Library()


@register.simple_tag
def format_json_to_html(json):
    print json
    return json2html.convert(json=json, table_attributes="class=\"table table-bordered table-hover\"")
