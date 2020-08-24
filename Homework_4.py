import requests


URI = 'http://0.0.0.0:5002/'


def make_request(method):
    if method.upper() == 'GET':
        r = requests.get(URI)
        print('Request GET response = {}'.format(r))

    elif method.upper() == 'POST':
        r = requests.post(URI)
        print('Request POST response = {}'.format(r))

    elif method.upper() == 'PUT':
        r = requests.put(URI, 'test')
        print('Request PUT response = {}'.format(r))

    elif method.upper() == 'HEADERS':
        req = requests.post(URI)
        r = req.headers
        print('Request HEADERS response = {}'.format(r))

    elif method.upper() == 'BODY':
        req = requests.get(URI)
        r = req.content
        print('Request BODY response = {}'.format(r))


def make_session_request(user, password, method, data=None):
    s = requests.Session()
    s.auth = (user, password)
    r = s.request(method.upper(), URI, data=data)
    print('Request {} response = {}'.format(method.upper(), r))


if __name__ == '__main__':
    make_request('GET')
    make_request('POST')
    make_request('PUT')
    make_request('headers')
    make_request('body')
    make_session_request('sergii', 'hello', 'GET')
    make_session_request('sergii', 'hello', 'POST', 'test111')
    make_session_request('sergii', 'hello', 'PUT', 'test222')
