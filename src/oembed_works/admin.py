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

from django.contrib import admin
from django.db.models.loading import cache


#class StoredOEmbedResponseAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(cache.get_model('oembed_works', 'StoredOEmbedResponse'), StoredOEmbedResponseAdmin)
