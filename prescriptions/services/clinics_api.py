import requests
from iclinic.settings import ENV as env_var
from prescriptions.utils.httpadapter import RetryTimeoutHTTPAdapter


class ClinicsApiService():
    _config = env_var['clinics_api']

    def get_clinic_by_id(self, id):
        headers = {'Authorization': self._config['key']}
        timeout = int(self._config['timeout'])
        retry = int(self._config['retry'])
        try:
            adapter = RetryTimeoutHTTPAdapter(
                timeout=timeout, max_retries=retry)
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
            return None
