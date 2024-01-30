from attr import define, field, asdict
import json


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

    @status.validator
    def validate_status(self, attribute, value):
        if value != 'success':
            raise ValueError('Invalid IP address.')
        return value

    def json(self, **kwargs):
        return json.dumps(asdict(self), **kwargs)


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

    def json(self, **kwargs):
        return json.dumps(asdict(self), **kwargs)
