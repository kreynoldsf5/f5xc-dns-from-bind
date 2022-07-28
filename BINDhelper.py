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

def a_record(rec):
    record = {
        'ttl': rec['ttl'],
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
        'ttl': rec['ttl'],
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
        'ttl': rec['ttl'],
        'alias_record': {
            'value': rec['rdata']['value']
        }  
    }
    return record

def caa_record(rec):
    record = {
        'ttl': rec['ttl'],
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
        'ttl': rec['ttl'],
        'cname_record': {
            'name': rec['name'],
            'value': rec['rdata']['value']
        }            
    }
    return record

def mx_record(rec):
    record = {
        'ttl': rec['ttl'],
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
        'ttl': rec['ttl'],
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
        'ttl': rec['ttl'],
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
        'ttl': rec['ttl'],
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
        'ttl': rec['ttl'],
        'txt_record': {
            'name': rec['name'],
            'values': {
                rec['rdata']['value']
            }
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

