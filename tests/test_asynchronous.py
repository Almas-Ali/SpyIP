import unittest
import asyncio

from spyip.backends.asynchronous import trace_me, trace_dns, trace_ip, trace_ip_batch


class TestSpyIP(unittest.IsolatedAsyncioTestCase):
    async def test_trace_me(self):
        response = await trace_me()
        self.assertEqual(response.status, 'success')

    async def test_trace_dns(self):
        response = await trace_dns()
        self.assertNotEqual(response.ip, '')
        self.assertNotEqual(response.geo, '')

    async def test_trace_ip(self):
        response = await trace_ip(query='31.13.64.35')
        self.assertEqual(response.status, 'success')

    async def test_trace_ip_batch(self):
        """Check all status is success or not"""
        res = await trace_ip_batch(
            query_list=[
                '31.13.64.35',  # facebook.com
                '142.250.193.206',  # google.com
                '20.205.243.166',  # github.com
                '20.236.44.162',  # microsoft.com
            ]
        )
        status_list = [i.status == 'success' for i in res]
        self.assertTrue(all(status_list))

    async def test_ip_response(self):
        """
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

        response = await trace_ip(query='142.250.193.206')

        self.assertEqual(response.status, 'success')
        self.assertEqual(response.continent, 'Asia')
        self.assertEqual(response.continentCode, 'AS')
        self.assertEqual(response.country, 'India')
        self.assertEqual(response.countryCode, 'IN')
        self.assertEqual(response.region, 'DL')
        self.assertEqual(response.regionName, 'National Capital Territory of Delhi')
        self.assertEqual(response.city, 'New Delhi')
        self.assertEqual(response.district, '')
        self.assertEqual(response.zip_, '110001')
        self.assertEqual(response.lat, 28.6139)
        self.assertEqual(response.lon, 77.209)
        self.assertEqual(response.timezone, 'Asia/Kolkata')
        self.assertEqual(response.offset, 19800)
        self.assertEqual(response.currency, 'INR')
        self.assertEqual(response.isp, 'Google LLC')
        self.assertEqual(response.org, 'Google LLC')
        self.assertEqual(response.as_, 'AS15169 Google LLC')
        self.assertEqual(response.asname, 'GOOGLE')
        self.assertEqual(response.mobile, False)
        self.assertEqual(response.proxy, False)
        self.assertEqual(response.hosting, True)
        self.assertEqual(response.query, '142.250.193.206')

    async def test_json_output(self):
        response = await trace_ip(query='31.13.64.35')
        self.assertEqual(
            response.json(),
            '{"status": "success", "continent": "Asia", "continentCode": "AS", "country": "India", "countryCode": "IN", "region": "WB", "regionName": "West Bengal", "city": "Kolkata", "district": "", "zip_": "700059", "lat": 22.518, "lon": 88.3832, "timezone": "Asia/Kolkata", "offset": 19800, "currency": "INR", "isp": "Facebook, Inc.", "org": "Meta Platforms Ireland Limited", "as_": "AS32934 Facebook, Inc.", "asname": "FACEBOOK", "mobile": false, "proxy": false, "hosting": false, "query": "31.13.64.35"}',
        )


if __name__ == '__main__':
    asyncio.run(unittest.main())
