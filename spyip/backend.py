from typing import List, Union
import asyncio
import random
import string

import httpx

from .exceptions import (
    TooManyRequests,
    ConnectionTimeout,
    StatusError,
)
from .models import (
    IPResponse,
    DNSResponse,
)


def get_random_string(length: int = 32) -> str:
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.sample(letters, length))


# API endpoints for IP address lookup
trace_me_url = 'http://ip-api.com/json/'
trace_ip_url = 'http://ip-api.com/json/%(query)s'
trace_dns_url = f'http://{get_random_string(32)}.edns.ip-api.com/json/'
trace_ip_batch_url = 'http://ip-api.com/batch'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
}


def trace_me(
    timeout: int = 5,
    lang: str = 'en',
) -> Union[IPResponse, None]:
    """Trace your own IP address."""
    try:
        res = httpx.get(
            url=trace_me_url,
            params={'fields': 66842623, 'lang': lang},
            headers=headers,
            timeout=timeout,
        )
        data = res.json()
        data['as_'] = data.pop('as')

        if res.status_code == 200:
            return IPResponse(**data)
        else:
            raise StatusError(f'Invalid status code: {res.status_code}. Expected 200.')

    # 408 Request Timeout
    except httpx._exceptions.ConnectTimeout:
        raise ConnectionTimeout(
            'Connection timeout. The server timed out waiting for the request. According to the HTTP specification, the client is allowed to repeat the request again after some time.'
        )
    # 429 Too Many Requests
    except httpx._exceptions.TooManyRedirects:
        raise TooManyRequests(
            'Too many requests. Our endpoints are limited to 45 HTTP requests per minute from an IP address. If you go over this limit your requests will be throttled (HTTP 429) until your rate limit window is reset.'
        )


def trace_ip(
    query: str,
    timeout: int = 5,
    lang: str = 'en',
) -> IPResponse:
    """Trace IP address"""
    try:
        res = httpx.get(
            url=trace_ip_url % {'query': query},
            params={'fields': 66842623, 'lang': lang},
            headers=headers,
            timeout=timeout,
        )
        data = res.json()
        data['as_'] = data.pop('as')

        if res.status_code == 200:
            return IPResponse(**data)
        else:
            raise StatusError(f'Invalid status code: {res.status_code}. Expected 200.')

    # 408 Request Timeout
    except httpx._exceptions.ConnectTimeout:
        raise ConnectionTimeout('The server timed out waiting for the request.')
    # 429 Too Many Requests
    except httpx._exceptions.TooManyRedirects:
        raise TooManyRequests(
            'Too many requests. Our endpoints are limited to 45 HTTP requests per minute from an IP address. If you go over this limit your requests will be throttled (HTTP 429) until your rate limit window is reset.'
        )


def trace_dns(
    timeout: int = 5,
    lang: str = 'en',
) -> IPResponse:
    """Trace your own DNS address."""
    try:
        res = httpx.get(
            url=trace_dns_url,
            params={'fields': 66842623, 'lang': lang},
            headers=headers,
            timeout=timeout,
        )
        if res.status_code == 200:
            return DNSResponse(**res.json()['dns'])
        else:
            raise StatusError(f'Invalid status code: {res.status_code}. Expected 200.')
    # 408 Request Timeout
    except httpx._exceptions.ConnectTimeout:
        raise ConnectionTimeout(
            'Connection timeout. The server timed out waiting for the request. According to the HTTP specification, the client is allowed to repeat the request again after some time.'
        )

    # 429 Too Many Requests
    except httpx._exceptions.TooManyRedirects:
        raise TooManyRequests(
            """\
This endpoint is limited to 15 requests per minute from an IP address.

If you go over the limit your requests will be throttled (HTTP 429) until your rate limit window is reset. If you constantly go over the limit your IP address will be banned for 1 hour.

The returned HTTP header X-Rl contains the number of requests remaining in the current rate limit window. X-Ttl contains the seconds until the limit is reset.
Your implementation should always check the value of the X-Rl header, and if its is 0 you must not send any more requests for the duration of X-Ttl in seconds."""
        )


def trace_ip_batch(
    query_list: List[str],
    timeout: int = 5,
    lang: str = 'en',
) -> List[IPResponse]:
    """Trace multiple IP addresses"""
    try:
        res = httpx.post(
            url=trace_ip_batch_url,
            params={'fields': 66842623, 'lang': lang},
            headers=headers,
            timeout=timeout,
            json=query_list,
        )
        response = []
        if res.status_code == 200:
            for x in res.json():
                x['as_'] = x.pop('as')
                response.append(IPResponse(**x))
            return response
        else:
            raise StatusError(f'Invalid status code: {res.status_code}. Expected 200.')
    # 408 Request Timeout
    except httpx._exceptions.ConnectTimeout:
        raise ConnectionTimeout(
            'Connection timeout. The server timed out waiting for the request. According to the HTTP specification, the client is allowed to repeat the request again after some time.'
        )

    # 429 Too Many Requests
    except httpx._exceptions.TooManyRedirects:
        raise TooManyRequests(
            """\
This endpoint is limited to 15 requests per minute from an IP address.

If you go over the limit your requests will be throttled (HTTP 429) until your rate limit window is reset. If you constantly go over the limit your IP address will be banned for 1 hour.

The returned HTTP header X-Rl contains the number of requests remaining in the current rate limit window. X-Ttl contains the seconds until the limit is reset.
Your implementation should always check the value of the X-Rl header, and if its is 0 you must not send any more requests for the duration of X-Ttl in seconds."""
        )
