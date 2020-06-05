import requests
import json


def get(url, headers=None, cookies=None):
    # Get request
    try:
        response = requests.get(url=url, headers=headers, cookies=cookies)
        return response
    except:
        print("Something went wrong.")


def post(url, headers=None, cookies=None, data=None):
    # Post request
    try:
        response = requests.post(url=url, headers=headers, cookies=cookies, data=data)
        return response
    except:
        print("Something went wrong.")


def put(url, headers=None, cookies=None, data=None):
    # Put request
    try:
        response = requests.put(url=url, headers=headers, cookies=cookies, data=data)
        return response
    except:
        print("Something went wrong.")


def main():
    main_url = 'http://jsonplaceholder.typicode.com'
    payload = {'id': 101,
               'title': 'test',
               'body': 'test_body',
               'userId': 1
               }
    response = get(f'{main_url}/posts/1')
    print(response.text)
    response = post(f'{main_url}/posts', data=json.dumps(payload))
    print(response.text)
    response = put(f'{main_url}/posts/1', data=json.dumps(payload))
    print(response.text)
    # Remove any data from the server using Delete request
    # response =
    # print(response.text)


if __name__ == '__main__':
    main()
