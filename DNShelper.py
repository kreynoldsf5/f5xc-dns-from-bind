import zonefile_parser

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ParseErr(Error):
    """Raised when XC rest operation fails"""
    pass

def parse_zonefile(zone_file) -> list:
    try:
        with open(zone_file, 'r') as stream:
            content = stream.read()
            records = zonefile_parser.parse(content)
        return records
    except Exception as e:
        raise ParseErr('Unable to parse zone file content.')

def normalize_ttl(rec) -> int:
    '''XC API requires all ttls to be >=60'''
    if rec['ttl'] < 60:
        return 60
    return rec['ttl']

def a_record(rec):
    record = {
        'ttl': normalize_ttl(rec),
        'a_record': {
            'name': rec['name'],
            'values': [
                rec['rdata']['value']
            ]
        }
    }
    return record

def aaaa_record(rec):
    record = {
        'ttl': normalize_ttl(rec),
        'aaaa_record': {
            'name': rec['name'],
            'values': [
                rec['rdata']['value']
            ]
        }
    }
    return record

def alias_record(rec):
    record = {
        'ttl': normalize_ttl(rec),
        'alias_record': {
            'name': None,
            'value': rec['rdata']['value']
        }  
    }
    return record

def caa_record(rec):
    record = {
        'ttl': normalize_ttl(rec),
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
    return record

def cname_record(rec):
    record = {
        'ttl': normalize_ttl(rec),
        'cname_record': {
            'name': rec['name'],
            'value': rec['rdata']['value']
        }            
    }
    return record

def mx_record(rec):
    record = {
        'ttl': normalize_ttl(rec),
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
    return record

def ns_record(rec):
    record = {
        'ttl': normalize_ttl(rec),
        'ns_record': {
            'name': rec['name'],
            'values': [
                rec['rdata']['value']
            ]
        }
    }
    return record

def ptr_record(rec):
    record = {
        'ttl': normalize_ttl(rec),
        'ptr_record': {
            'name': rec['name'],
            'values': [
                rec['rdata']['value']
            ]
        }            
    }
    return record

def srv_record(rec):
    record = {
        'ttl': normalize_ttl(rec),
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
    return record

def txt_record(rec):
    record = {
        'ttl': normalize_ttl(rec),
        'txt_record': {
            'name': rec['name'],
            'values': [
                rec['rdata']['value']
            ]
        }            
    }
    return record

type2func = {
    'A': a_record,
    'AAAA': aaaa_record,
    'ALIAS': alias_record,
    'CAA': caa_record,
    'CNAME': cname_record,
    'MX': mx_record,
    'NS': ns_record,
    'PTR': ptr_record,
    'SRV': srv_record,
    'TXT': txt_record 
}

