#!/usr/bin/env python3
import zonefile_parser
import argparse
from requests import Session
from urllib.parse import urljoin

_xc_supported_types = {
    'A': 'a_record',
    'AAAA': 'aaaa_record',
    'ALIAS': 'alias_record',
    'CAA': 'caa_record',
    'CNAME': 'cname_record',
    'MX': 'mx_record',
    'NS': 'ns_record',
    'PTR': 'ptr_record',
    'SRV': 'srv_record',
    'TXT': 'txt_record'
}

class Error(Exception):
    """Base class for other exceptions"""
    pass

class XCerror(Error):
    """Raised when XC rest operation fails"""
    pass

class Perror(Error):
    """Raised when parsing operation fails"""
    pass

class Processed:
    def __init__(self, recs, unproc):
        self.recs = recs
        self.unproc = unproc

class XCrr_set_group:
    def __init__(self):
        self.records = []
        self.unprocessed_records = []
        self._xc_supported_types = {
            'A': 'a_record',
            'AAAA': 'aaaa_record',
            'ALIAS': 'alias_record',
            'CAA': 'caa_record',
            'CNAME': 'cname_record',
            'MX': 'mx_record',
            'NS': 'ns_record',
            'PTR': 'ptr_record',
            'SRV': 'srv_record',
            'TXT': 'txt_record'
        }

    def add_a(self, rec):
        record = {
            'a_record': {
                'name': rec['name'],
                'values': [
                    rec['rdata']['value']
                ]
            }
        }
        self.records.append(self._add_ttl(rec, record))

    def add_aaaa(self, rec):
        record = {
           'aaaa_record': {
                'name': rec['name'],
                'values': [
                    rec['rdata']['value']
                ]
            }
        }
        self.records.append(self._add_ttl(rec, record))

    def add_alias(self, rec):
        record = {
           'alias_record': {
                'value': rec['rdata']['value']
            }  
        }
        self.records.append(self._add_ttl(rec, record))

    def add_caa(self, rec):
        record = {
            'caa_record': {
                'name': rec['name'],
                'values': [
                    {
                        'flags': rec['rdata']['flag'],
                        'tag': rec['rdata']['tag'],
                        'value': rec['rdata']['value']
                    }
                ]
            }            
        }
        self.records.append(self._add_ttl(rec, record))

    def add_cname(self, rec):
        record = {
          'cname_record': {
                'name': rec['name'],
                'value': rec['rdata']['value']
            }            
        }
        self.records.append(self._add_ttl(rec, record))

    def add_mx(self, rec):
        record = {
            'mx_record': {
                'name': rec['name'],
                'values': [
                    {
                        'domain': rec['rdata']['host'],
                        'priority': rec['rdata']['priority']
                    }
                ]
            } 
        }
        self.records.append(self._add_ttl(rec, record))

    def add_ns(self, rec):
        record = {
            'ns_record': {
                'name': rec['name'],
                'values': [
                    rec['rdata']['value']
                ]
            }
        }
        self.records.append(self._add_ttl(rec, record))

    def add_ptr(self, rec):
        record = {
            'ptr_record': {
                'name': rec['name'],
                'values': [
                    rec['rdata']['value']
                ]
            }            
        }
        self.records.append(self._add_ttl(rec, record))

    def add_srv(self, rec):
        record = {
            'srv_record': {
                'name': rec['name'],
                'values': [
                    {
                        'port': rec['rdata']['port'],
                        'priority': rec['rdata']['priority'],
                        'target': rec['rdata']['host'],
                        'weight': rec['rdata']['weight']
                    }
                ]
            }            
        }
        self.records.append(self._add_ttl(rec, record))

    def add_txt(self, rec):
        record = {
            'txt_record': {
                'name': rec['name'],
                'values': {
                    rec['rdata']['value']
                }
            }            
        }
        self.records.append(self._add_ttl(record))

    def _add_ttl(rec, record):
        record['ttl'] = rec['ttl']
        return record


class F5xcSession(Session):
    def __init__(self, token, prefix_url=None, *args, **kwargs):
        super(F5xcSession, self).__init__(*args, **kwargs)
        self.prefix_url = prefix_url
        self.headers.update({'Authorization': "APIToken {0}".format(token)})

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.prefix_url, url)
        return super(F5xcSession, self).request(method, url, *args, **kwargs)

    def create_zone(self, desc: str ='ephemeral NS'):
        payload = {
            'metadata':
                {
                    'annotations': {},
                    'description': desc,
                    'disable': False,
                    'labels': {},
                    'name': nsName,
                    'namespace': ''
                },
            'spec': {}
        }
        try:
            resp = self.post('/api/web/namespaces', json=payload)
            resp.raise_for_status()
        except Exception as e:
            raise XCerror(e)

    def replace_zone(self, desc: str ='ephemeral NS'):
        payload = {
            'metadata':
                {
                    'annotations': {},
                    'description': desc,
                    'disable': False,
                    'labels': {},
                    'name': nsName,
                    'namespace': ''
                },
            'spec': {}
        }
        try:
            resp = self.put('/api/web/namespaces', json=payload)
            resp.raise_for_status()
        except Exception as e:
            raise XCerror(e)

def parse_zonefile(zone_file) -> list:
    try:
        with open(zone_file, 'r') as stream:
            content = stream.read()
            records = zonefile_parser.parse(content)
        return records
    except Exception as e:
        raise Perror('Unable to parse zone file content.')

def process_records(records: list):
    json_recs = []
    unprocessed_recs = []
    for record in records:
        try:
            rec = proc_record(record.__dict__)
            json_recs.append(rec)
        except Exception as e:
            unprocessed_recs.append(record)
            continue
    return Processed(json_recs, unprocessed_recs)

def proc_record(rec) -> dict:
    '''Function to represent XC supported record types and their schema'''
    #TBD: Do we need to account for same records with diff values or will the XC API handle that for us?
    switch={
        'A': {
            'a_record': {
                'name': rec['name'],
                'values': [
                    rec['rdata']['value']
                ]
            }
        },
        'AAAA': {
            'aaaa_record': {
                'name': rec['name'],
                'values': [
                    rec['rdata']['value']
                ]
            }
        },
        'ALIAS': {
            'alias_record': {
                'value': rec['rdata']['value']
            }
        },
        'CAA': {
            'caa_record': {
                'name': rec['name'],
                'values': [
                    {
                        'flags': rec['rdata']['flag'],
                        'tag': rec['rdata']['tag'],
                        'value': rec['rdata']['value']
                    }
                ]
            }
        },
        'CNAME': {
            'cname_record': {
                'name': rec['name'],
                'value': rec['rdata']['value']
            }
        },
        'MX': {
            'mx_record': {
                'name': rec['name'],
                'values': [
                    {
                        'domain': rec['rdata']['host'],
                        'priority': rec['rdata']['priority']
                    }
                ]
            }
        },
        'NS': {
            'ns_record': {
                'name': rec['name'],
                'values': [
                    rec['rdata']['value']
                ]
            }
        },
        'PTR': {
            'ptr_record': {
                'name': rec['name'],
                'values': [
                    rec['rdata']['value']
                ]
            }
        },
        'SRV': {
            'srv_record': {
                'name': rec['name'],
                'values': [
                    {
                        'port': rec['rdata']['port'],
                        'priority': rec['rdata']['priority'],
                        'target': rec['rdata']['host'],
                        'weight': rec['rdata']['weight']
                    }
                ]
            }
        },
        'TXT': {
            'txt_record': {
                'name': rec['name'],
                'values': {
                    rec['rdata']['value']
                }
            }
        }
    }
    this_rec = switch.get(rec['rtype'], None)
    if this_rec:
        this_rec['ttl'] = rec['ttl']
        return this_rec
    else:
        raise Perror('record type not supported')



def create_payload(zone_name: str, records: list)->dict:
    payload = {
        'metadata': {
            'name': zone_name,
            'namespace': 'system',
        },
        'spec': {
            'primary': {
                'default_rr_set_group': records
            }
        }
    }
    return payload

def main():
    ap = argparse.ArgumentParser(
        prog='f5xc_dns_from_bind',
        usage='%(prog)s.py [options]',
        description='parse a BIND zone file and populate an f5xc zone.'
    )
    ap.add_argument(
        '--zonefile',
        help='specify the BIND zone file to be parsed',
        required=True
    )
    """
    ap.add_argument(
        '--token',
        help='token used for API access',
        required=True
    )
    ap.add_argument(
        '--tenant_url',
        help='URL for zone API endpoint',
        required=True
    )
    ap.add_argument(
        '--zone_name',
        help='Zone name to be updated',
        required=True
    )
    """
    args = ap.parse_args()
    bind_rec_list = parse_zonefile(args.zonefile)
    proc_recs = process_records(bind_rec_list)
    print(proc_recs.recs)
    print(proc_recs.unproc)
    #xcSession = F5xcSession(args.token, args.tenant_url)

