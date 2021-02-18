from django.test import TestCase
from prescriptions.utils.httpadapter import RetryTimeoutHTTPAdapter


class HTTPAdapterTestCase(TestCase):
    def test_adapter_with_default_timeout(self):
        adapter = RetryTimeoutHTTPAdapter()
        self.assertTrue(isinstance(adapter, RetryTimeoutHTTPAdapter))
        self.assertEqual(adapter.timeout, 5)

    def test_adapter_with_custom_timeout(self):
        adapter = RetryTimeoutHTTPAdapter(timeout=10)
        self.assertTrue(isinstance(adapter, RetryTimeoutHTTPAdapter))
        self.assertEqual(adapter.timeout, 10)
