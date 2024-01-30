"""
SpyIP - A simple IP lookup tool written in Python.

Dependent on:
-------------
    httpx
    pydantic
    https://ip-api.com/
    

Supported fields:
-----------------
    status
    continent
    continentCode
    country
    countryCode
    region
    regionName
    city
    district
    zip
    lat
    lon
    timezone
    offset
    currency
    isp
    org
    as
    asname
    mobile
    proxy
    hosting
    query

    
Supported languages:
--------------------

| lang (ISO 639) | description                     |
| -------------- | ------------------------------- |
| en             | English (default)               |
| de             | Deutsch (German)                |
| es             | Español (Spanish)               |
| pt-BR          | Português - Brasil (Portuguese) |
| fr             | Français (French)               |
| ja             | 日本語 (Japanese)               |
| zh-CN          | 中国 (Chinese)                  |
| ru             | Русский (Russian)               |

"""

from .backend import trace_me, trace_ip, trace_dns, trace_ip_batch


__version__ = '0.2.0'
__author__ = 'Md. Almas Ali'
__all__ = [
    'trace_me',
    'trace_ip',
    'trace_dns',
    'trace_ip_batch',
]
