
=====
Usage
=====

This section contains information, including examples, about how to use
*django-oembed-works* in your existing Django projects or applications.


Template Tag
============

In order to use the ``oembed`` template tag, you have to insert the following
statement in your template::

    {% load oembed_works_tags %}

The template tag can be used like::

    {% oembed %}
    {{ entry.body }}
    {% endoembed %}

Optionally, a width and height for the embedded object can be forced::

    {% oembed 560x420 %}
    {{ entry.body }}
    {% endoembed %}

