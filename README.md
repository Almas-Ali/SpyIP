<h1 align="center">SpyIP</h1>

<p align="center">
<a href="https://pepy.tech/project/spyip"><img src="https://static.pepy.tech/personalized-badge/spyip?period=total&units=none&left_color=grey&right_color=blue&left_text=Total%20Downloads"></a>
<a href="https://github.com/Almas-Ali/SpyIP/"><img src="https://img.shields.io/github/license/Almas-Ali/SpyIP?style=flat-square"></a>
<a href="https://wakatime.com/badge/user/168edf9f-71dc-49cc-bf77-592d9c9d4eed/project/018cbf9a-cecf-4ae8-ad59-a34b9eefb754"><img src="https://wakatime.com/badge/user/168edf9f-71dc-49cc-bf77-592d9c9d4eed/project/018cbf9a-cecf-4ae8-ad59-a34b9eefb754.svg" alt="wakatime"></a>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAlmas-Ali%2FSpyIP&count_bg=%2352B308&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
</p>

<p align="center">A simple IP lookup tool written in Python.
</p>

SpyIP uses <a href="https://ip-api.com/" target="_blank" title="IP-API">ip-api</a> API to trace IP addresses. SpyIP is type annotated, unit tested, PEP8 compliant, documented and optimized for performance.

## Features

- [x] Trace your own IP address

- [x] Trace your own DNS

- [x] Trace IP address by query

- [x] Trace batch IP address


- [x] Type annotated

- [x] Unit tested

- [x] PEP8 compliant

- [x] Documented

- [x] Optimized


## Installation

```bash
pip install spyip
```

## Usage

```python
from spyip import trace_me, trace_dns, trace_ip, trace_ip_batch


me = trace_me() # trace your own IP
print(me.json(indent=4)) # print as JSON with indent


dns = trace_dns() # trace your own DNS
print(dns.json()) # print as JSON


# trace by IP address (facebook.com)
ip = trace_ip(query="31.13.64.35")
print(ip.json()) # print as JSON

# set timeout
print(
    trace_ip(
        query="31.13.64.35",
        timeout=5,
    ).json()
)


# batch trace by IP address (facebook.com, google.com, github.com, microsoft.com, ...)
batch = trace_ip_batch(
    query_list=[
        '31.13.64.35', # facebook.com
        '142.250.193.206', # google.com
        '20.205.243.166', # github.com
        '20.236.44.162', # microsoft.com
    ],
)
print(batch) # print a list of IPResponse objects. (see below)
```

## Localization

Localized `city`, `regionName` and `country` can be translated to the following languages by passing `lang` argument to `trace_me`, `trace_ip` and `trace_ip_batch` functions. Default language is `en` (English). Here is the list of supported languages:

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

## Response objects

Response objects are `pydantic` base models. In `SpyIP` we have 2 response objects respectively:

<ol type="1">
<li>
<details>
<summary>
<code>IPResponse</code>: for single IP address query
</summary>

```python
@define
class IPResponse:
    """
    Example response from API:

    {
        "status": "success",
        "continent": "Asia",
        "continentCode": "AS",
        "country": "India",
        "countryCode": "IN",
        "region": "DL",
        "regionName": "National Capital Territory of Delhi",
        "city": "New Delhi",
        "district": "",
        "zip": "110001",
        "lat": 28.6139,
        "lon": 77.209,
        "timezone": "Asia/Kolkata",
        "offset": 19800,
        "currency": "INR",
        "isp": "Google LLC",
        "org": "Google LLC",
        "as": "AS15169 Google LLC",
        "asname": "GOOGLE",
        "mobile": false,
        "proxy": false,
        "hosting": true,
        "query": "142.250.193.206",
    }
    """

    status: str = field(metadata={'description': 'Status of the request.'})
    continent: str = field(metadata={'description': 'Continent name.'})
    continentCode: str = field(metadata={'description': 'Continent code.'})
    country: str = field(metadata={'description': 'Country name.'})
    countryCode: str = field(metadata={'description': 'Country code.'})
    region: str = field(metadata={'description': 'Region code.'})
    regionName: str = field(metadata={'description': 'Region name.'})
    city: str = field(metadata={'description': 'City name.'})
    district: str = field(metadata={'description': 'District name.'})
    zip_: str = field(metadata={'description': 'Zip code.'}, alias='zip')
    lat: float = field(metadata={'description': 'Latitude.'})
    lon: float = field(metadata={'description': 'Longitude.'})
    timezone: str = field(metadata={'description': 'Timezone.'})
    offset: int = field(metadata={'description': 'Offset.'})
    currency: str = field(metadata={'description': 'Currency.'})
    isp: str = field(metadata={'description': 'ISP name.'})
    org: str = field(metadata={'description': 'Organization name.'})
    as_: str = field(metadata={'description': 'AS number and name.'}, alias='as_')
    asname: str = field(metadata={'description': 'AS name.'})
    mobile: bool = field(metadata={'description': 'Mobile status.'})
    proxy: bool = field(metadata={'description': 'Proxy status.'})
    hosting: bool = field(metadata={'description': 'Hosting status.'})
    query: str = field(metadata={'description': 'IP address.'})
```

</details>
</li>
<li>
<details>
<summary>
<code>DNSResponse</code>: for DNS query
</summary>

```python
@define
class DNSResponse:
    """
    Example response from API:
    "dns": {
        "ip": "74.125.73.83",
        "geo": "United States - Google"
    }
    """

    ip: str = field(metadata={'description': 'IP address.'})
    geo: str = field(metadata={'description': 'Geo location.'})
```

</details>
</li>
</ol>

In batch query, `trace_ip_batch` returns a list of `IPResponse` objects. You can just iterate over the list and use as you need.

## Exceptions

`SpyIP` has 3 custom exceptions:

- `TooManyRequests` - raised when you exceed the API rate limit.
- `ConnectionTimeout` - raised when connection times out.
- `StatusError` - raised when API returns an error status.

## Tests

Test cases are located in `tests` directory. You can run tests with the following command:

```bash
python -m unittest discover -s tests
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. If you have any idea, suggestion or question, feel free to open an issue. Please make sure to update tests as appropriate.

## License

This project is licensed under the terms of the [MIT](LICENSE) license.
