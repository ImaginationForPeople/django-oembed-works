# -*- coding: utf-8 -*-
#
#  This file is part of django-oembed-works.
#
#  DESCRIPTION_DESCRIPTION_DESCRIPTION
#
#  Development Web Site:
#    - http://www.codetrax.org/projects/django-oembed-works
#  Public Source Code Repository:
#    - https://source.codetrax.org/hgroot/django-oembed-works
#
#  Copyright 2010 George Notaras <gnot [at] g-loaded.eu>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from django import template

from oembed_works.exceptions import OEmbedSizeError
from oembed_works.utils import get_dimensions_from_string


register = template.Library()


class OEmbedNode(template.Node):
    def __init__(self, nodelist, width, height):
        self.nodelist = nodelist
        self.width = width
        self.height = height
    def render(self, context):
        output = self.nodelist.render(context)
        # Processing
        # TODO:
        return output

def do_oembed(parser, token):
    """
    - 
    {% oembed [WIDTHxHEIGHT] %}
    
    {% endoembed %}
    
    """
    # split_contents() knows not to split quoted strings.
    args = token.split_contents()
    width, height = None, None
    if len(args) not in (2, 3):
        raise template.TemplateSyntaxError('%s tag requires one or two arguments' % args[0])
    elif len(args) == 3:
        try:
            width, height = get_dimensions_from_string(args[1])
        except OEmbedSizeError:
            raise template.TemplateSyntaxError("second argument to %s tag must be a string of the format 'WIDTHxHEIGHT'" % args[0])
    
    nodelist = parser.parse(('endoembed',))
    parser.delete_first_token()
    return OEmbedNode(nodelist, width, height)

register.tag('oembed', do_oembed)


