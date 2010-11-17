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

import re

from django import template

from oembed_works import oembed
from oembed_works.exceptions import OEmbedSizeError
from oembed_works.utils import get_dimensions_from_string
from oembed_works import settings


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
    
    def _process_output(self, output):
        consumer = self._get_oembed_consumer()
        for endpoint, regex_list in settings.OEMBED_PROVIDERS.values():
            for regex in regex_list:
                #print "Doing regex: %s" % regex
                for m in re.finditer(regex, output):
                    #print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))
                    oembed_html = self._get_oembed_html(consumer, m.group(0))
                    output = '%s%s%s' % (output[:m.start()], oembed_html, output[m.end():])
        return output
    
    def _get_oembed_consumer(self):
        consumer = oembed.OEmbedConsumer()
        for format, endpoint_api, regex_list in settings.OEMBED_PROVIDERS.values():
            endpoint = oembed.OEmbedEndpoint(endpoint_api, regex_list)
            consumer.addEndpoint(endpoint)
        return consumer
    
    def _get_oembed_html(self, consumer, link):
        response = consumer.embed(link)
        if isinstance(response, oembed.OEmbedPhotoResponse):
            return '<img src="%(url)s" width="%(width)s" height="%(height)s" />' % response
        else:
            return link



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


