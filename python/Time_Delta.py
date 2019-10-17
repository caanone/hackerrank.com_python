#!/bin/python3

import math
import os
import random
import re
import sys
from time import strptime
from datetime import datetime

# Sun 10 May 2015 13:54:36 -0700
def time_delta(t1, t2):
    return 100

if __name__ == '__main__':
    date_inputs = {}
    for x in range(3):
        for y in range(1):
            dt = input().split(" ")
            print(dt[4].split(":")[2])
            date_inputs.update({
                str(x) + "-" + str(y) : {
                    "day":int(dt[1]),
                    "month":strptime(dt[2],'%b').tm_mon,
                    "year":int(dt[3]),
                    "hour":int(dt[4].split(":")[0]), "minute":int(dt[4].split(":")[1]), "second":int(dt[4].split(":")[2]),
                    "tztype":dt[5][0], "tz_secs":int(dt[5][1:3]) * 60 * 60 + int(dt[5][3:5]) * 60
                    }})
    
    # Development purposes..
    import json
    print(json.dumps(date_inputs, sort_keys=True,
                 indent=4, separators=(',', ': ')))
    

"""

Sun 10 May 2015 13:54:36 -0730
Sun 10 May 2015 13:54:36 -1010
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000


"""





"""
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains , the number of testcases.
Each testcase contains  lines, representing time  and time .

Constraints

Input contains only valid timestamps
.
Output Format

Print the absolute difference  in seconds.

Sample Input 0

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sample Output 0

25200
88200
Explanation 0

In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is  seconds or  seconds.

Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 
"""