import requests

def make_request(url):
    r = requests.get(url=url)
    body = r.json()
    return body


def get_ngrok_url():
    try:
        ngrok_body = make_request('http://localhost:4040/api/tunnels')
        public_url = ngrok_body['tunnels'][0]['public_url']
        return public_url
    except:
        return ''

if __name__ == '__main__':
    print(get_ngrok_url())