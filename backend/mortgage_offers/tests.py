import requests


def create_mortgage_offers():
    url = "http://localhost:8000/api/offer/"

    payload = {'bank_name': 'Test_bank_name',
               'term_min': '10',
               'term_max': '30',
               'rate_min': '1.8',
               'rate_max': '9.8',
               'payment_min': '1000000',
               'payment_max': '10000000'}

    files = []
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(f'POST -> {response.text}')


def change_mortgage_offers(id_offer):
    url = f"http://localhost:8000/api/offer/{id_offer}/"

    payload = {'bank_name': 'Test_bank_name_change',
               'term_min': '10',
               'term_max': '30',
               'rate_min': '1.8',
               'rate_max': '9.8',
               'payment_min': '1000000',
               'payment_max': '10000000'}
    files = []
    headers = {}

    response = requests.request("PATCH", url, headers=headers, data=payload, files=files)

    print(f'PATCH -> {response.text}')


def get_list_all_mortgage_offers():
    url = "http://localhost:8000/api/offer/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(f'GET -> {response.text}')


def remove_mortgage_offer(id_offer):
    url = f"http://localhost:8000/api/offer/{id_offer}/"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(f'DELETE -> {response.text}')


def filters():
    import requests

    url = "http://localhost:8000/api/offer/?rate_min=&rate_max=&payment_min=1000000&payment_max=10000000&order=-rate&price=10000000&deposit=10&term=20"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(f'FILTERS -> {response.text}')


if __name__ == '__main__':
    print('Test.py')

    create_mortgage_offers()
    print('create_mortgage_offers DONE')

    change_mortgage_offers(29)
    print('change_mortgage_offers DONE')

    get_list_all_mortgage_offers()
    print('get_list_all_mortgage_offers DONE')

    remove_mortgage_offer(29)
    print('remove_mortgage_offer DONE')

    filters()
    print('filters DONE')
