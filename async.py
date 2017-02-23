from requests_futures.sessions import FuturesSession

def bg_cb(sess, resp):
    print(resp.status_code)

session = FuturesSession()
future_one = session.get('http://httpbin.org/get', background_callback=bg_cb)
future_two = session.get('http://httpbin.org/get?foo=bar', background_callback=bg_cb)

print(future_one.done())
print(future_one.done())

#response_one = future_one.result()
#print('response one status: {0}'.format(response_one.status_code))
#print(response_one.content)
# wait for the second request to complete, if it hasn't already
#response_two = future_two.result()
#print('response two status: {0}'.format(response_two.status_code))
#print(response_two.content)

