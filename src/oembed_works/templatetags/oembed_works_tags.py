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
from django.template.loader import render_to_string

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
        self.consumer = self._get_oembed_consumer()
    
    def render(self, context):
        output = self.nodelist.render(context)
        # Process output
        output = self._oembed_processor(output, self.width, self.height)
        return output
    
    def _oembed_processor(self, output, width, height):
        for format, endpoint, regex_list in settings.OEMBED_PROVIDERS.values():
            for regex in regex_list:
                for m in re.finditer(regex, output):
                    #print 'MATCH: %02d-%02d: %s' % (m.start(), m.end(), m.group(0))
                    oembed_html = self._get_oembed_html(self.consumer, m.group(0), width, height)
                    pattern = re.escape(m.group(0)) # The found link is used as the pattern
                    output = re.sub(pattern, oembed_html, output)
        return output
    
    def _get_oembed_consumer(self):
        consumer = oembed.OEmbedConsumer()
        for format, endpoint_api, regex_list in settings.OEMBED_PROVIDERS.values():
            endpoint = oembed.OEmbedEndpoint(endpoint_api, regex_list)
            consumer.addEndpoint(endpoint)
        return consumer
    
    def _get_oembed_html(self, consumer, link, width, height):
        response = consumer.embed(link)
        info_dict = {'response': self._set_oembed_dimensions(response, width, height)}
        if response['type'] == 'photo':
            return render_to_string('oembed_works/photo.html', info_dict)
        if response['type'] == 'video':
            return render_to_string('oembed_works/video.html', info_dict)
        if response['type'] == 'link':
            return render_to_string('oembed_works/link.html', info_dict)
        if response['type'] == 'rich':
            return render_to_string('oembed_works/rich.html', info_dict)
        else:
            return link
    
    def _set_oembed_dimensions(self, response, width, height):
        if width is not None:
            response['width'] = width
            if response.has_key('html'):
                response['html'] = re.sub('width="\d+"', 'width="%d"' % width, response['html'])
        if height is not None:
            response['height'] = height
            if response.has_key('html'):
                response['html'] = re.sub('height="\d+"', 'height="%d"' % height, response['html'])
        return response

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


