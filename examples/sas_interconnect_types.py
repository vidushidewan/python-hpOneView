# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2016) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from pprint import pprint
from hpOneView.oneview_client import OneViewClient
from config_loader import try_load_from_file

# This resource is only supported for synergy enclosures

config = {
    "ip": "",
    "credentials": {
        "userName": "administrator",
        "password": ""
    }
}

# Try load config from a file (if there is a config file)
config = try_load_from_file(config)

oneview_client = OneViewClient(config)

# Get all
print("Get all SAS Interconnect Types")
sas_interconnect_types = oneview_client.sas_interconnect_types.get_all()
pprint(sas_interconnect_types)

if sas_interconnect_types:
    # Get by URI
    print("Get a SAS Interconnect Type by URI")
    uri = sas_interconnect_types[0]['uri']
    sas_interconnect_type_by_uri = oneview_client.sas_interconnect_types.get(uri)
    pprint(sas_interconnect_type_by_uri)

    # Get by name
    print("Get a SAS Interconnect Type by name")
    name = sas_interconnect_types[0]['name']
    sas_interconnect_type_by_name = oneview_client.sas_interconnect_types.get_by('name', name)
    pprint(sas_interconnect_type_by_name)
