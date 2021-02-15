import requests
from iclinic.settings import ENV as env_var
from prescriptions.errors.error_catalog import errors
from prescriptions.utils.httpadapter import RetryTimeoutHTTPAdapter


class PhysiciansApiService():
    _config = env_var['physicians_api']

    def get_physician_by_id(self, id):
        headers = {'Authorization': self._config['key']}
        timeout = float(self._config['timeout'])
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
            response = http_request.get(
                self._config['url'] +
                self._config['path'].replace('{id}', str(id))
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            if response.status_code == 404:
                return {'error': errors[2]}
            else:
                return {'error': errors[5]}
        except requests.exceptions.ConnectionError:
            return {'error': errors[5]}
