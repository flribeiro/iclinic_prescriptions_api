import requests
from requests.api import request
from iclinic.settings import ENV as env_var
from prescriptions.errors.error_catalog import errors
from prescriptions.utils.httpadapter import RetryTimeoutHTTPAdapter


class MetricsApiService():
    _config = env_var['metrics_api']

    def post_metrics(self, body):
        headers = {'Authorization': self._config['key']}
        timeout = int(self._config['timeout'])
        retry = int(self._config['retry'])
        try:
            adapter = RetryTimeoutHTTPAdapter(
                timeout=timeout,
                max_retries=retry
            )
            adapter.add_headers(headers)
            http_request = requests.Session()
            http_request.mount(
                'https://',
                adapter
            )
            response = http_request.post(
                self._config['url'] +
                self._config['path'],
                data=body
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            return {'error': errors[4]}
