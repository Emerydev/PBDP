import server
import json


def test_fct_search_contact():

    req_payload = {
        "search_in_dirs": [1, 2],
        "filters": [
            {
                "field_name": "firstname",
                "field_value": "test"
            }
        ]
    }
    result = server.search_contact(req_payload)
    print("Fetch results: ")
    print(json.dumps(result, indent=4, sort_keys=True))


def test_fct_add_user():
    req_payload = {
        "pseudo": "test",
        "password": "test", 
        "admin": "true"

    }
    result = server.add_user(req_payload)
    print(result)


def test_fct_add_contact():
    req_payload = {
        "dir_id": 2,
        "contact": {
            "firstname": "test",
            "lastname": "test", 
            "email": "test@test.test",
            "phone": "0000000000", 
            "address": {
                "street": "street test", 
                "street_number": "number test",
                "country": "country test", 
                "city": "city test"
            }
        }
    }
    result = server.add_contact(req_payload)
    print(result)


# test_fct_add_user()
# test_fct_add_contact()
# test_fct_search_contact()
