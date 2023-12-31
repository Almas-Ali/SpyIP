from pydantic import BaseModel, Field, field_validator


class IPResponse(BaseModel):
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

    status: str = Field(..., description='Status of the request.')
    continent: str = Field(..., description='Continent name.')
    continentCode: str = Field(..., description='Continent code.')
    country: str = Field(..., description='Country name.')
    countryCode: str = Field(..., description='Country code.')
    region: str = Field(..., description='Region code.')
    regionName: str = Field(..., description='Region name.')
    city: str = Field(..., description='City name.')
    district: str = Field(..., description='District name.')
    zip_: str = Field(..., description='Zip code.')
    lat: float = Field(..., description='Latitude.')
    lon: float = Field(..., description='Longitude.')
    timezone: str = Field(..., description='Timezone.')
    offset: int = Field(..., description='Offset.')
    currency: str = Field(..., description='Currency.')
    isp: str = Field(..., description='ISP name.')
    org: str = Field(..., description='Organization name.')
    as_: str = Field(..., description='AS number and name.')
    asname: str = Field(..., description='AS name.')
    mobile: bool = Field(..., description='Mobile status.')
    proxy: bool = Field(..., description='Proxy status.')
    hosting: bool = Field(..., description='Hosting status.')
    query: str = Field(..., description='IP address.')

    class Config:
        def alias_generator(x):
            return x.replace('_', '')

        populate_by_name = True
        # fields = {  # Alias for reserved keywords
        #     "as_": "as",
        #     "zip_": "zip",
        # }

    @field_validator('status')
    def check_status(cls, v):
        if v != 'success':
            raise ValueError('Invalid IP address.')
        return v

    def json(self, **kwargs) -> str:
        return self.model_dump_json(**kwargs)


class DNSResponse(BaseModel):
    """
    Example response from API:
    "dns": {
        "ip": "74.125.73.83",
        "geo": "United States - Google"
    }
    """

    ip: str = Field(..., description='IP address.')
    geo: str = Field(..., description='Geo location.')

    def json(self, **kwargs) -> str:
        return self.model_dump_json(**kwargs)
