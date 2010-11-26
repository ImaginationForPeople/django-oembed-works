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

from django.db import models
from django.utils import simplejson

from oembed_works import oembed


class StoredOEmbedResponse(models.Model):
    link_hash = models.CharField(max_length=32, unique=True, db_index=True)
    response_data = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Stored OEmbed Response'
        verbose_name_plural = 'Stored OEmbed Responses'
    
    def __unicode__(self):
        return self.link_hash
    
    def get_response_object(self):
        """Returns an OEmbedResponse object according to the response type."""
        data = simplejson.loads(self.response_data)
        if not data.has_key('type'):
            raise oembed.OEmbedError('Missing required field `type` in stored OEmbed response.')
        response = oembed.OEmbedResponse.create(data['type'])
        response.loadData(data)
        return response

