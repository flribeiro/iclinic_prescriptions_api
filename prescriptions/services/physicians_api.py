import requests
import json
from django.core.cache import cache
from iclinic.settings import ENV as env_var
from prescriptions.errors.error_catalog import errors
from prescriptions.utils.httpadapter import RetryTimeoutHTTPAdapter


class PhysiciansApiService():
    _config = env_var['physicians_api']

    def get_physician_by_id(self, id):
        headers = {'Authorization': self._config['key']}
        timeout = float(self._config['timeout'])
        retry = int(self._config['retry'])
        cache_ttl = int(self._config['cache_ttl']) * 3600
        physician = cache.get(f'physician_{id}')
        if physician is not None:
            return json.loads(physician)
        else:
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
                physician = response.json()
                cache.set(f'physician_{physician["id"]}', json.dumps(
                    physician), timeout=cache_ttl)
                return physician
            except requests.exceptions.HTTPError:
                if response.status_code == 404:
                    return {'error': errors[2]}
                else:
                    return {'error': errors[5]}
            except requests.exceptions.ConnectionError:
                return {'error': errors[5]}
