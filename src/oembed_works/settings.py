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

from django.conf import settings



_OEMBED_PROVIDERS = {
    # Format:
    #     <provider_name>: (<format>, <endpoint_api_url>, [<regex1>, <regex2>, ...])
    
    'Flickr': ('1', 'http://www.flickr.com/services/oembed',
        [r'http://(?:www\.)?flickr\.com/photos/\S+?/(?:sets/)?\d+/?']),
    'Amazon Product Image (OohEmbed)': ('1', 'http://oohembed.com/oohembed/',
        [r'http://\S*\.amazon\.(com|co\.uk|de|ca|jp)/\S*/(gp/product|o/ASIN|obidos/ASIN|dp)/\S*']),
    'Google Video (OohEmbed)': ('1', 'http://oohembed.com/oohembed/',
        [r'http://video\.google\.com/videoplay?\S*']),
    'Metacafe (OohEmbed)': ('1', 'http://oohembed.com/oohembed/',
        [r'http://\S*.metacafe.com/watch/\S*']),
    'Twitter Status (OohEmbed)': ('1', 'http://oohembed.com/oohembed/',
        [r'http://(?:www\.)?twitter\.com/(?:\w{1,20})/statuses/\d+/?']),
    'Wikipedia (OohEmbed)': ('1', 'http://oohembed.com/oohembed/',
        [r'http://\S*.wikipedia.org/wiki/\S*']),
    'YouTube (OohEmbed)': ('1', 'http://oohembed.com/oohembed/',
        [r'http://(?:www\.)?youtube\.com/watch\?v=[A-Za-z0-9\-=_]{11}']),
    'Vimeo': ('1', 'http://vimeo.com/api/oembed.json',
        [r'http://(?:www\.)?vimeo\.com/\d+']),
    'Scribd': ('1', 'http://www.scribd.com/services/oembed',
        [r'http://(?:www\.)?scribd\.com/.*']),
    'Dailymotion (OohEmbed)': ('1', 'http://oohembed.com/oohembed/',
        [r'http://(?:www\.)?dailymotion\.com/video/[^<\S]+']),
    #'': ('1', '',
    #    [r'']),
}

OEMBED_PROVIDERS = getattr(settings, 'OEMBED_PROVIDERS', _OEMBED_PROVIDERS)


