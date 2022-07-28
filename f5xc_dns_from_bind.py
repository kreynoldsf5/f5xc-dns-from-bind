#!/usr/bin/env python3
import argparse
import XChelper, BINDhelper

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
    bind_rec_list = BINDhelper.parse_zonefile(args.zonefile)
    proc_recs = process_records(bind_rec_list)
    print(proc_recs.recs)
    print(proc_recs.unproc)
    #xcSession = F5xcSession(args.token, args.tenant_url)

