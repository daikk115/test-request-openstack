import json

import env
from graceful_exit import *

url_list_meter = 'http://{}:8777/v2/meters'.format(env.IP)
url_get_statistics = 'http://{}:8777/v2/meters/image.size/statistics'.format(env.IP)
url_create_alarm = 'http://{}:8042/v2/alarms'.format(env.IP)

headers = {
    'User-Agent': 'ceilometerclient.apiclient',
    'X-Auth-Token': env.TOKEN
}

create_body = {
    "threshold_rule": {
        "threshold": 8.0,
        "query": [{
            "field": "resource_id",
            "type": "",
            "value": "5341d781-692d-4c67-acc2-c1ebe0e99ce7",
            "op": "eq"
        }],
        "meter_name": "image.size",
        "comparison_operator": "gt",
        "statistic": "count"
    },
    "alarm_actions": ["log://"],
    "type": "threshold",
    "name": "image_size_count"
}

if __name__ == '__main__':
    while True:
        time.sleep(0.1)
        # Get list metering
        send_request(url_list_meter, 'GET', headers=headers)

        # Statistic of image.size
        send_request(url_get_statistics, 'GET', headers=headers)

        # Create new alarm
        try:
            post_future = send_request(url_create_alarm, 'POST',
                              headers=headers, data=json.JSONEncoder().encode(create_body))
            post_content = post_future.result().content
        except Exception as e:
            print e
            # In case, not graceful shutdown --> Connection Errorr
            continue
        alarm_id = json.loads(post_content).get('alarm_id')
        url_alarm = 'http://{}:8042/v2/alarms/{}'.format(env.IP, alarm_id)

        # Get special alarm
        try:
            get_future = send_request(url_alarm, 'GET', headers=headers)
            get_content = get_future.result().content
        except:
            # In case, not graceful shutdown --> Connection Error
            continue

        # Update alarm with threshold increasing
        update_body = json.loads(get_content)
        update_body["threshold_rule"]["threshold"] = 10.0
        send_request(url_alarm, "PUT",
                     headers=headers, data=json.JSONEncoder.encode(update_body))

        # Delete above alarm
        url_delete_alarm = 'http://{}:8042/v2/alarms/{}'.format(env.IP, alarm_id)
        send_request(url_alarm, 'DELETE', headers=headers)

"""
GET alarm resp:
{"alarm_actions": ["log://"],
"ok_actions": [],
"name": "image_count2",
"severity": "low",
"timestamp": "2017-03-22T07:01:47.072404",
"enabled": true,
"state": "insufficient data",
"state_timestamp": "2017-03-22T07:01:33.191512",
"threshold_rule": {
    "meter_name": "image.size",
    "evaluation_periods": 1,
    "period": 60, "statistic": "count",
    "threshold": 10.0,
    "query": [{
        "field": "resource_id",
        "type": "",
        "value": "5341d781-692d-4c67-acc2-c1ebe0e99ce7",
        "op": "eq"
    }],
    "comparison_operator": "gt",
    "exclude_outliers": false
},
"alarm_id": "9e4a202c-662c-4888-abd0-7a8d926a57e1",
"time_constraints": [],
"insufficient_data_actions": [],
"repeat_actions": false,
"user_id":
"383934eac7cc40cfa6bd32a21c18a2f6",
"project_id": "239238e54ed14524a753241e8a577d54",
"type": "threshold",
"description": "Alarm when image.size is gt a count of 8.0 over 60 seconds"}
"""
