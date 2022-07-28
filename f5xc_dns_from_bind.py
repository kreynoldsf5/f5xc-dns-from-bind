#!/usr/bin/env python3
import argparse
import XChelper, DNShelper

class XCresults():
    def __init__(self):
        self.records = []
        self.unprocessed = []
    def add_rec(self, XCrec):
        self.records.append(XCrec)
    def rm_rec(self, XCrec):
        self.records.remove(XCrec)
    def add_up(self, rec):
        self.unprocessed.append(rec)
    def rm_up(self, rec):
        self.unprocessed.remove(rec)

def process_records(records: list, results: XCresults):
    for record in records:
        rec = record.__dict__
        try:
            XCrec = DNShelper.type2func[rec['rtype']](rec)
            results.add_rec(XCrec)
        except Exception as e:
            results.add_up(rec)
            continue
    return results

def main():
    ap = argparse.ArgumentParser(
        prog='f5xc_dns_from_bind',
        usage='%(prog)s.py [options]',
        description='parse a BIND zone file and populate an f5xc zone.'
    )
    ap.add_argument(
        '--zone_file',
        help='specify the BIND zone file to be parsed',
        required=True
    )
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
        help='zone name to be created',
        required=True
    )
    ap.add_argument(
        '--update',
        help='update an existing zone (as opposed to creating a new zone)',
        action='store_true',
        default=False,
        required=False
    )
    args = ap.parse_args()
    bind_rec_list = DNShelper.parse_zonefile(args.zone_file)
    results = XCresults()
    process_records(bind_rec_list, results)
    xcSession = XChelper.F5xcSession(args.token, args.tenant_url)
    if args.update:
        xcSession.update_zone(args.zone_name, results.records)
    else:
        xcSession.create_zone(args.zone_name, results.records)

    """
    1. zone name is valid
    2. there are recrods to add
    3. REST call succeeded
    4. pretty output/report containing count of records added and records not supported
    """

if __name__ == "__main__":
    main()

