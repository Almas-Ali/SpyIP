import unittest

from spyip import trace_me, trace_dns, trace_ip, trace_ip_batch


class TestSpyIP(unittest.TestCase):
    def test_trace_me(self):
        self.assertEqual(trace_me().status, 'success')

    def test_trace_dns(self):
        self.assertNotEqual(trace_dns().ip, '')
        self.assertNotEqual(trace_dns().geo, '')

    def test_trace_ip(self):
        self.assertEqual(trace_ip(query='31.13.64.35').status, 'success')

    def test_trace_ip_batch(self):
        """Check all status is success or not"""
        res = trace_ip_batch(
            query_list=[
                '31.13.64.35',  # facebook.com
                '142.250.193.206',  # google.com
                '20.205.243.166',  # github.com
                '20.236.44.162',  # microsoft.com
            ]
        )
        status_list = [i.status == 'success' for i in res]
        self.assertTrue(all(status_list))

    def test_ip_response(self):
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

        res = trace_ip(query='142.250.193.206')

        self.assertEqual(res.status, 'success')
        self.assertEqual(res.continent, 'Asia')
        self.assertEqual(res.continentCode, 'AS')
        self.assertEqual(res.country, 'India')
        self.assertEqual(res.countryCode, 'IN')
        self.assertEqual(res.region, 'DL')
        self.assertEqual(res.regionName, 'National Capital Territory of Delhi')
        self.assertEqual(res.city, 'New Delhi')
        self.assertEqual(res.district, '')
        self.assertEqual(res.zip_, '110001')
        self.assertEqual(res.lat, 28.6139)
        self.assertEqual(res.lon, 77.209)
        self.assertEqual(res.timezone, 'Asia/Kolkata')
        self.assertEqual(res.offset, 19800)
        self.assertEqual(res.currency, 'INR')
        self.assertEqual(res.isp, 'Google LLC')
        self.assertEqual(res.org, 'Google LLC')
        self.assertEqual(res.as_, 'AS15169 Google LLC')
        self.assertEqual(res.asname, 'GOOGLE')
        self.assertEqual(res.mobile, False)
        self.assertEqual(res.proxy, False)
        self.assertEqual(res.hosting, True)
        self.assertEqual(res.query, '142.250.193.206')

    def test_json_output(self):
        res = trace_ip(query='31.13.64.35')
        self.assertEqual(
            res.json(),
            '{"status": "success", "continent": "Asia", "continentCode": "AS", "country": "India", "countryCode": "IN", "region": "WB", "regionName": "West Bengal", "city": "Kolkata", "district": "", "zip_": "700059", "lat": 22.518, "lon": 88.3832, "timezone": "Asia/Kolkata", "offset": 19800, "currency": "INR", "isp": "Facebook, Inc.", "org": "Meta Platforms Ireland Limited", "as_": "AS32934 Facebook, Inc.", "asname": "FACEBOOK", "mobile": false, "proxy": false, "hosting": false, "query": "31.13.64.35"}',
        )
