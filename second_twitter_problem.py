 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'vacate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING service
#  2. INTEGER replacement_count
#  3. STRING_ARRAY hostname_service_list
#

def vacate(service, replacement_count, hostname_service_list):
    # Write your code here
    # racks = set()

    # for each rack
    # racks with smallest numbers of instances of services at front of some structure
    # this guarantees that if we start removing replacement_count instances of service
    #   the racks with the smallest number of instances AND greatest of empty are at the front, so we get the
    #   "most" number of cleared racks possible up to replacement_count

    # return racks with only empty as the service on the host
    service_hosts_count = 1
    empty_hosts_count = []
    racks_and_counts = {}

    for host_line in hostname_service_list:
        host_name, host_service = host_line.split(" ")
        rack_name = host_name.split("-")[0]
        racks_and_counts[rack_name] = {service: 0, "empty_count": 0}


    for host_line in hostname_service_list:
        for rack, count_tracker in racks_and_counts:
            if service in host_line:
                racks_and_counts[rack][service] += 1
            elif ("empty" in host_line):
                racks_and_counts[rack]["empty_count"] += 1

    print(racks_and_counts)
    return []

if __name__ == '__main__':

    service = "timelines"

    replacement_count = 2

    hostname_service_list_count = 12

    hostname_service_list = ["aaa-01.prod.twttr.net timelines", "aaa-02.prod.twttr.net empty", "aaa-03.prod.twttr.net empty", "aab-01.prod.twttr.net timelines", "aab-02.prod.twttr.net timelines", "aab-03.prod.twttr.net empty", "aac-01.prod.twttr.net timelines", "aac-02.prod.twttr.net empty", "aac-03.prod.twttr.net tweets", "aad-01.prod.twttr.net timelines", "aad-02.prod.twttr.net empty", "aad-03.prod.twttr.net empty"]

    result = vacate(service, replacement_count, hostname_service_list)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
