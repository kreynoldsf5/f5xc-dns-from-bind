from requests import Session
from urllib.parse import urljoin

class Error(Exception):
    """Base class for other exceptions"""
    pass

class XCerr(Error):
    """Raised when XC rest operation fails"""
    pass

class F5xcSession(Session):
    def __init__(self, token, prefix_url=None, *args, **kwargs):
        super(F5xcSession, self).__init__(*args, **kwargs)
        self.prefix_url = prefix_url
        self.headers.update({'Authorization': "APIToken {0}".format(token)})

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.prefix_url, url)
        return super(F5xcSession, self).request(method, url, *args, **kwargs)

    def create_zone(self, zoneName, xcRecords):
        payload = {
            'metadata': {
                'name': zoneName,
                'namespace': 'system',
            },
            'spec': {
                'primary': {
                    'default_rr_set_group': xcRecords
                }
            }
        }
        try:
            resp = self.post('/api/web/namespaces', json=payload)
            resp.raise_for_status()
        except Exception as e:
            raise XCerr(e)

    def replace_zone(self, zoneName, xcRecords):
        payload = {
            'metadata': {
                'name': zoneName,
                'namespace': 'system',
            },
            'spec': {
                'primary': {
                    'default_rr_set_group': xcRecords
                }
            }
        }
        try:
            resp = self.put('/api/web/namespaces', json=payload)
            resp.raise_for_status()
        except Exception as e:
            raise XCerr(e)