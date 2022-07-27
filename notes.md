#Notes

```shell
{'rtype': 'CNAME', 'name': 'dvwa.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'asm.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'e-app.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'emea-ms.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'e.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'email.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'email.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'email.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'emea-mdm.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '31.221.17.175'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'emea-ms.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '31.221.17.174'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'emea.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns4-02.azure-dns.info.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'emea.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns3-02.azure-dns.org.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'emea.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns2-02.azure-dns.net.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'emea.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns1-02.azure-dns.com.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'emeasp.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'dns-italy.f5se.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'epcheck.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.122'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'etherpad.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.98'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'f5-gsa.volt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns1.volterradns.io.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'f5-gsa.volt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns4.volterradns.io.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'f5-gsa.volt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns3.volterradns.io.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'f5-gsa.volt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns2.volterradns.io.'}, 'ttl': '20'}
```

```json
"default_rr_set_group": [
        {
          "ttl": 3600,
          "a_record": {
            "name": "example",
            "values": [
              "1.2.3.4"
            ]
          }
        },
        {
          "ttl": 86400,
          "ns_record": {
            "name": "",
            "values": [
              "ns1.f5clouddns.com",
              "ns2.f5clouddns.com"
            ]
          }
        },
        {
          "ttl": 3600,
          "a_record": {
            "name": "example2",
            "values": [
              "2.3.4.5"
            ]
          }
        }
      ],
```

```json
"spec": {
"primary": {
"default_rr_set_group": [
{
"a_record": {
"name": "string",
"values": [
"string"
]
},
"aaaa_record": {
"name": "string",
"values": [
"string"
]
},
"alias_record": {
"value": "string"
},
"caa_record": {
"name": "string",
"values": [
{
"flags": 0,
"tag": "string",
"value": "string"
}
]
},
"cname_record": {
"name": "string",
"value": "string"
},
"mx_record": {
"name": "string",
"values": [
{
"domain": "string",
"priority": 0
}
]
},
"ns_record": {
"name": "string",
"values": [
"string"
]
},
"ptr_record": {
"name": "string",
"values": [
"string"
]
},
"srv_record": {
"name": "string",
"values": [
{
"port": 0,
"priority": 0,
"target": "string",
"weight": 0
}
]
},
"ttl": 0,
"txt_record": {
"name": "string",
"values": [
"string"
]
}
}
],
```


 def week(i):
        switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
         return switcher.get(i,"Invalid day of week")



{'rtype': 'CNAME', 'name': '_0197a04015c2dfb11a1f71488b04ca28.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'A02ED68EA436F6CCF20B61311059A711.B3DD41E557B5F7F51C5CDD136BEC8A60.comodoca.com.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': '_0197a04015c2dfb11a1f71488b04ca28.shop.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '02ED68EA436F6CCF20B61311059A711.B3DD41E557B5F7F51C5CDD136BEC8A60.comodoca.com.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': '_224e4497e25664cd536d8a04eb640f8b.hive.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_3ceb02740b3b6d8b4ff480df7896d23c.mzlfeqexyx.acm-validations.aws.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': '_29fd174e9c000bbb92ffb80f8274f974.api.clouddocs.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_d22a717467127a524e8411b870e55204.jfrzftwwjs.acm-validations.aws.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': '_32ad0267137e0c3e567510e4af17d567.www.clouddocs.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_9e6e19d98ee4df6869b76c38be737d17.mzlfeqexyx.acm-validations.aws.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': '_39be946e55a7a0884b9901fc1d786982.github-mgmt-dev.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_965b9be3b86b62fdb8f0ef37a9d31c9b.zdxcnfdgtt.acm-validations.aws.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': '_46bcb0ba3805ffbb51beb6a193da5e92.source.clouddocs.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_d8d5b2cd3b2ef07fc36f537cf2497707.jfrzftwwjs.acm-validations.aws.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': '_46bcb0ba3805ffbb51beb6a193da5e92.source.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_d8d5b2cd3b2ef07fc36f537cf2497707.jfrzftwwjs.acm-validations.aws.'}, 'ttl': '20'}
{'rtype': 'TXT', 'name': '_acme-challenge.letsencrypt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'Yxxawh6fd1acx3w29zS1XZ9bKMKPOt2X1LCPfn3vWos'}, 'ttl': '3600'}
{'rtype': 'TXT', 'name': '_acme-challenge.www.letsencrypt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'wGsSebrR9P9s7F6CsWEHFIn8NPlL5WnnH4g26cPJW5s'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': '_ba1889d380286d16a97bd211484ab1fa.github-mgmt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_7d2848b76398d7bbb5c039587edafeb1.zdxcnfdgtt.acm-validations.aws.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': '_c66d77b93d7d7fd52b1217059db894d5.arc-hive.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_529ce0f6a83a0ca6d737db0402a9f785.mzlfeqexyx.acm-validations.aws.'}, 'ttl': '20'}
{'rtype': 'SRV', 'name': '_citrixreceiver._tcp.f5se.com.', 'rclass': 'IN', 'rdata': {'priority': '1', 'weight': '1', 'port': '443', 'host': 'cloudgateway.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'TXT', 'name': '_dmarc.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'v=DMARC1; p=reject; fo=1; ri=3600; rua=mailto:f5@rua.agari.com; ruf=mailto:f5@ruf.agari.com'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': '_domainconnect.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_domainconnect.gd.domaincontrol.com.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': '_f343f9d0e7a76b60aafd6b3292956496.arc-hive-dev.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_70ad41456ca796d28636684351d45bc1.mzlfeqexyx.acm-validations.aws.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': '_f762993af3f76168374ca9007f449278.clouddocs.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '_5057d1a7744c4caee76d737a63f8e5be.mzlfeqexyx.acm-validations.aws.'}, 'ttl': '20'}
{'rtype': 'TXT', 'name': '_pki-validation.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'A561-795B-31DB-74FE-E284-2E73-7497-3AF9'}, 'ttl': '20'}
{'rtype': 'SRV', 'name': '_sip._tls.f5se.com.', 'rclass': 'IN', 'rdata': {'priority': '100', 'weight': '1', 'port': '443', 'host': 'sipdir.online.lync.com.'}, 'ttl': '3600'}
{'rtype': 'SRV', 'name': '_sipfederationtls._tcp.f5se.com.', 'rclass': 'IN', 'rdata': {'priority': '100', 'weight': '1', 'port': '5061', 'host': 'sipfed.online.lync.com.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'abm.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '50.112.211.206'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'adfs.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '13.91.53.212'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': 'airline-backend.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'airline-alb-1429882411.us-west-1.elb.amazonaws.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'airline.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '184.169.227.227'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'airline2.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '12.222.68.72'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'alertserver.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '54.200.134.68'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'apcjseapps.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '1c831a9fec452bff055e8473b94bcd04-894600865.ap-southeast-1.elb.amazonaws.com.'}, 'ttl': '600'}
{'rtype': 'CNAME', 'name': 'api.arc-hive.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'arc-hive.f5se.com.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': 'api.clouddocs.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'd-rcq0w871pb.execute-api.us-east-1.amazonaws.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'apm-chicago.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '173.15.123.181'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'arc-hive-dev.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'd25q5iht7xlnwt.cloudfront.net.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': 'arc-hive.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'd3tbcazgtp9ekd.cloudfront.net.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'asm.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.112'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'autodiscover.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'autodiscover.outlook.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'aw-mail.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.97'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'backend.webresearch.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '34.68.209.197'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': 'bank.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ghs.googlehosted.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'chi.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '173.15.123.180'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'chicago.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '173.15.123.180'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'citrix-chicago.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '173.15.123.179'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'clouddocs.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'd3slromlcdsxlk.cloudfront.net.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'cloudgateway.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.110'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'connect.chi.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '173.15.123.179'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'connect.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.76'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'demobank.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '54.200.134.68'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'dns-iberia.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '62.23.186.230'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'dns-italy.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '212.31.246.29'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'dns-paris.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '109.7.65.105'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'docs.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.107'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'dvwa.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'asm.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'e-app.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'emea-ms.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'e.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'email.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'email.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'email.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'emea-mdm.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '31.221.17.175'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'emea-ms.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '31.221.17.174'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'emea.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns4-02.azure-dns.info.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'emea.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns3-02.azure-dns.org.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'emea.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns2-02.azure-dns.net.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'emea.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns1-02.azure-dns.com.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'emeasp.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'dns-italy.f5se.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'epcheck.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.122'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'etherpad.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.98'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'f5-gsa.volt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns1.volterradns.io.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'f5-gsa.volt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns4.volterradns.io.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'f5-gsa.volt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns3.volterradns.io.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'f5-gsa.volt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns2.volterradns.io.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.75'}, 'ttl': '3600'}
{'rtype': 'CAA', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'flag': '0', 'tag': 'issue', 'value': 'godaddy.com'}, 'ttl': '20'}
{'rtype': 'CAA', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'flag': '0', 'tag': 'issue', 'value': 'amazon.com'}, 'ttl': '20'}
{'rtype': 'CAA', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'flag': '0', 'tag': 'issue', 'value': 'amazonaws.com'}, 'ttl': '20'}
{'rtype': 'CAA', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'flag': '0', 'tag': 'issue', 'value': 'entrust.net'}, 'ttl': '20'}
{'rtype': 'CAA', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'flag': '0', 'tag': 'issue', 'value': 'amazontrust.com'}, 'ttl': '20'}
{'rtype': 'CAA', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'flag': '0', 'tag': 'issue', 'value': 'letsencrypt.org'}, 'ttl': '20'}
{'rtype': 'CAA', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'flag': '0', 'tag': 'issue', 'value': 'awstrust.com'}, 'ttl': '20'}
{'rtype': 'MX', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'priority': '0', 'host': 'f5se-com.mail.eo.outlook.com.'}, 'ttl': '3600'}
{'rtype': 'MX', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'priority': '10', 'host': 'mailstore1.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns2.f5se.com.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns1.f5se.com.'}, 'ttl': '20'}
{'rtype': 'SOA', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'mname': 'hostmaster.f5se.com.', 'rname': 'ns1.f5se.com.', 'serial': '2022072601', 'refresh': '28800', 'retry': '7200', 'expire': '604800', 'minimum': '600'}, 'ttl': '3600'}
{'rtype': 'TXT', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'google-site-verification=PkiaBBMcL0G5aqbYaOwQyR1pVd4CFEppQIN0DdoYmvU'}, 'ttl': '20'}
{'rtype': 'TXT', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'MS=ms30729094'}, 'ttl': '20'}
{'rtype': 'TXT', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'v=spf1 a ip4:208.85.211.65 include:outlook.com -all'}, 'ttl': '20'}
{'rtype': 'TXT', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'nf2du49bqm7kcncqca88aj33dl.'}, 'ttl': '20'}
{'rtype': 'TXT', 'name': 'f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'h0hsh0s1ts36t3p2idon6plg6c'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'fpsalerts.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '199.204.218.88'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'fraudalerts.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.95'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'ftp.chi.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '173.15.123.179'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'ftp.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.75'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'ga.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ghs.googlehosted.com.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': 'github-mgmt-dev.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'd-c5de03h6mc.execute-api.us-east-1.amazonaws.com.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': 'github-mgmt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'd-v5kd3sibxl.execute-api.us-east-1.amazonaws.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'google.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.107'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'gslb.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns1.f5se.com.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'gslb.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns2.f5se.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'haiku.chi.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '173.15.123.179'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'hive.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'd3tbcazgtp9ekd.cloudfront.net.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'iberia.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'dns-iberia.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'idpdiscover.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.113'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'imap.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'imap.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'intune.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.119'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'isc.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '18.144.181.71'}, 'ttl': '30'}
{'rtype': 'A', 'name': 'issedemo.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.111'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'italy.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'dns-italy.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'login.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.113'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'low.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '63.116.152.90'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'lowell.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '63.116.152.90'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'lyncdiscover.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'webdir.online.lync.com.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'mail.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.114'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'mam.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.118'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'mobile.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.115'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'mobilemail.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'mobilemail-v01.prod.mesa1.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'ms62092986.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ps.microsoftonline.com.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'msoid.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'clientconfig.microsoftonline-p.net.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'msvdi.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '52.8.7.46'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'ns1.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '107.162.140.123'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'ns2.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '107.162.140.162'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'o365proxy.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.123'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'oauth-as.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.113'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'oauth.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.103'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'oc.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns-565.awsdns-06.net.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'oc.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns-1706.awsdns-21.co.uk.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'oc.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns-1137.awsdns-14.org.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'ofba.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '52.32.16.23'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'office365.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.113'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'opennms-skywest.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '199.204.218.16'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'os.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns-51.awsdns-06.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'otp.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.113'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'paris.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'dns-paris.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'paxtest.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '67.42.87.144'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': 'pda.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'mobilemail-v01.prod.mesa1.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'pop.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'pop.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'portal.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.108'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'portalpass.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'portal.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'recipies.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '52.8.117.183'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'salesforce.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.105'}, 'ttl': '3600'}
{'rtype': 'TXT', 'name': 'scjairline.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'h0hsh0s1ts36t3p2idon6plg6c'}, 'ttl': '60'}
{'rtype': 'A', 'name': 'securegit.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.75'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'shapeiapp.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '34.211.14.132'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'sharepoint.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.109'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'shop.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '52.9.104.123'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'silverline-syd.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'peg44.acmesyd.gslb.f5silverline.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'silverline.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '107.162.139.19'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': 'sip.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'sipdir.online.lync.com.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'sjcairline.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '12.222.68.72'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': 'slides.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'modseclambda-711464542.us-east-1.elb.amazonaws.com.'}, 'ttl': '20'}
{'rtype': 'CNAME', 'name': 'smtp.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'smtp.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'source.clouddocs.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'd2ps560w0f4g09.cloudfront.net.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'splunk-skywest.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '199.204.218.16'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'splunk.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.78'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'staging.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'dns4.p07.nsone.net.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'staging.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'dns1.p07.nsone.net.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'staging.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'dns2.p07.nsone.net.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'staging.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'dns3.p07.nsone.net.'}, 'ttl': '20'}
{'rtype': 'TXT', 'name': 'staging.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ves-io-b4c708df-cc19-4dd3-8e3a-bf3e044b544e'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'swg.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.120'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'u2fdemo.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'login.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'vdi-html5.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.106'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'vdi.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'vdi-html5.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'versafe.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.104'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'view.chi.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '173.15.123.181'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'viewgw.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.106'}, 'ttl': '3600'}
{'rtype': 'NS', 'name': 'volt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns2.f5se.com.'}, 'ttl': '20'}
{'rtype': 'NS', 'name': 'volt.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'ns1.f5se.com.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'vpn-skywest.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '199.204.218.16'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'vpntest.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.77'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'wareport.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.75'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'webmail.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'webmail.secureserver.net.'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'webresearch.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'd3ibvfqx7idnjy.cloudfront.net.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'websafe.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.104'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'whitehat.chi.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '173.15.123.179'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'www.clouddocs.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'd3slromlcdsxlk.cloudfront.net.'}, 'ttl': '20'}
{'rtype': 'A', 'name': 'www.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.75'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'xenapp-saml.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.103'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'xendemo.chi.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '173.15.123.178'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'xendemo.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.100'}, 'ttl': '3600'}
{'rtype': 'CNAME', 'name': 'xendesktop.f5se.com.', 'rclass': 'IN', 'rdata': {'value': 'xendemov11.f5se.com.'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'zenith.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.65'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'zenith1.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.66'}, 'ttl': '3600'}
{'rtype': 'A', 'name': 'zenith2.f5se.com.', 'rclass': 'IN', 'rdata': {'value': '208.85.211.67'}, 'ttl': '3600'}