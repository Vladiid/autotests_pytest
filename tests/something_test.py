import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User

# resp = requests.get(SERVICE_URL)
# print(resp.json())


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_abject = Response(response)
    test_abject.assert_status_code(200).validate(User)

# z = {
#   'meta': {
#     'pagination': {
#       'total': 2488,
#       'pages': 249,
#       'page': 1,
#       'limit': 10,
#       'links': {
#         'previous': None,
#         'current': 'https://gorest.co.in/public/v1/users?page=1',
#         'next': 'https://gorest.co.in/public/v1/users?page=2'
#       }
#     }
#   },
#   'data': [
#     {
#       'id': 2541,
#       'name': 'Mrs. Avadhesh Pillai',
#       'email': 'pillai_mrs_avadhesh@goldner-stamm.net',
#       'gender': 'male',
#       'status': 'inactive'
#     },
#     {
#       'id': 2540,
#       'name': 'Kannen Desai',
#       'email': 'kannen_desai@bosco.net',
#       'gender': 'female',
#       'status': 'active'
#     },
#     {
#       'id': 2539,
#       'name': 'Shankar Patel',
#       'email': 'patel_shankar@runte.co',
#       'gender': 'female',
#       'status': 'active'
#     },
#     {
#       'id': 2538,
#       'name': 'Rep. Suma Dutta',
#       'email': 'dutta_rep_suma@mayer.co',
#       'gender': 'female',
#       'status': 'inactive'
#     },
#     {
#       'id': 2537,
#       'name': 'Bhushit Somayaji DO',
#       'email': 'do_bhushit_somayaji@harvey-emmerich.io',
#       'gender': 'male',
#       'status': 'inactive'
#     },
#     {
#       'id': 2536,
#       'name': 'Akula Dhawan',
#       'email': 'dhawan_akula@harris.info',
#       'gender': 'male',
#       'status': 'active'
#     },
#     {
#       'id': 2535,
#       'name': 'Ambar Namboothiri Jr.',
#       'email': 'jr_ambar_namboothiri@treutel.io',
#       'gender': 'male',
#       'status': 'active'
#     },
#     {
#       'id': 2534,
#       'name': 'Charuchandra Desai IV',
#       'email': 'iv_charuchandra_desai@marquardt.com',
#       'gender': 'female',
#       'status': 'active'
#     },
#     {
#       'id': 2533,
#       'name': 'Deeptimayee Butt',
#       'email': 'deeptimayee_butt@brown.org',
#       'gender': 'male',
#       'status': 'inactive'
#     },
#     {
#       'id': 2532,
#       'name': 'Divakar Panicker',
#       'email': 'panicker_divakar@koepp.net',
#       'gender': 'female',
#       'status': 'active'
#     }
#   ]
# }
