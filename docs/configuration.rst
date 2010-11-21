
=============
Configuration
=============

This section contains information about how to configure your Django projects
to use *django-oembed-works* and also contains a quick reference of the available
*settings* that can be used in order to customize the functionality of this
application.


Configuring your project
========================

In the Django project's ``settings`` module, add ``oembed_works`` to the
``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'oembed_works',
    )


Reference of the application settings
=====================================

The following settings can be specified in the Django project's ``settings``
module to customize the functionality of *django-oembed-works*.

``OEMBED_PROVIDERS``
    A dictionary of the format::
    
        <provider_name>: (<endpoint_api_url>, [<regex1>, <regex2>, ...])
    
    ``provider_name``
        The oEmbed provider's name.
    ``endpoint_api_url``
        The endpoint's API URL.
    ``[<regex1>, <regex2>, ...]``
        A list of URL schemes. Each *URL scheme* is a regular expression.
    
    By default, the supported oEmbed providers are::
    
        {
        'YouTube': ('http://oohembed.com/oohembed/',
            [r'http://(?:www\.)?youtube\.com/watch\?v=[A-Za-z0-9\-=_]{11}']),
        'Vimeo': ('http://vimeo.com/api/oembed.json',
            [r'http://(?:www\.)?vimeo\.com/\d+']),
        'Dailymotion': ('http://oohembed.com/oohembed/',
            [r'http://(?:www\.)?dailymotion\.com/video/[^<\S]+']),
        'Flickr': ('http://www.flickr.com/services/oembed',
            [r'http://(?:www\.)?flickr\.com/photos/\S+?/(?:sets/)?\d+/?']),
        }


Synchronize the project database
================================

Finally, synchronize the project's database using the following command::

    python manage.py syncdb

