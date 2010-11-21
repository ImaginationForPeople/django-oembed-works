# -*- coding: utf-8 -*-
#
#  This file is part of django-oembed-works.
#
#  django-oembed-works is a Django app that provides support for the oEmbed format.
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

from django.conf import settings


_OEMBED_PROVIDERS = {
    # Format:
    #     <provider_name>: (<endpoint_api_url>, [<regex1>, <regex2>, ...])
    'YouTube': ('http://oohembed.com/oohembed/',
        [r'http://(?:www\.)?youtube\.com/watch\?v=[A-Za-z0-9\-=_]{11}']),
    'Vimeo': ('http://vimeo.com/api/oembed.json',
        [r'http://(?:www\.)?vimeo\.com/\d+']),
    'Dailymotion': ('http://oohembed.com/oohembed/',
        [r'http://(?:www\.)?dailymotion\.com/video/[^<\S]+']),
    'Flickr': ('http://www.flickr.com/services/oembed',
        [r'http://(?:www\.)?flickr\.com/photos/\S+?/(?:sets/)?\d+/?']),
    #'Google Video': ('http://oohembed.com/oohembed/',
    #    [r'http://video\.google\.com/videoplay?\S*']),
    #'Metacafe': ('http://oohembed.com/oohembed/',
    #    [r'http://\S*.metacafe.com/watch/\S*']),
    #'Scribd': ('http://www.scribd.com/services/oembed',
    #    [r'http://(?:www\.)?scribd\.com/.*']),
    #'Amazon Product Image': ('http://oohembed.com/oohembed/',
    #    [r'http://\S*\.amazon\.(com|co\.uk|de|ca|jp)/\S*/(gp/product|o/ASIN|obidos/ASIN|dp)/\S*']),
    #'Wikipedia': ('http://oohembed.com/oohembed/',
    #    [r'http://\S*.wikipedia.org/wiki/\S*']),
    #'Twitter Status': ('http://oohembed.com/oohembed/',
    #    [r'http://(?:www\.)?twitter\.com/(?:\w{1,20})/statuses/\d+/?']),
    #'': ('',
    #    [r'']),
}

OEMBED_PROVIDERS = getattr(settings, 'OEMBED_PROVIDERS', _OEMBED_PROVIDERS)


