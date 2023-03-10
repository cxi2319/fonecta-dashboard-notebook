import requests

API_KEY = "b2d6e0a848c3acb2df576557304c20ff"
V = "20230223"
PARENT_ACCOUNT_ID = "8181751292082973749"

ACCOUNT_LIST_URL = f"https://api.yext.com/v2/accounts?api_key={API_KEY}&v={V}&limit=1000&offset=1"
RESOURCE_APPLY_URL = (
    f"https://api.yext.com/v2/accounts/me/resourcesapplyrequests?api_key={API_KEY}&v={V}"
)


def jsonify_response(account_list_url):
    response = requests.get(account_list_url)

    account_json = response.json()

    json_response = account_json["response"]["accounts"]
    return json_response


json_response = jsonify_response(ACCOUNT_LIST_URL)

input_list = json_response
account_list = []

# Loop through the accounts list and print the accountId for each item
def get_accounts(input_list, account_list):
    for obj in input_list:
        # print(obj)
        if obj["parentAccountId"] == PARENT_ACCOUNT_ID and ["accountId"] != PARENT_ACCOUNT_ID:
            # print((obj["parentAccountId"]))
            account_list.append(obj["accountId"])
    # list of accountIDs
    return account_list


account_list = get_accounts(json_response, account_list)
# print(len(account_list))
print(account_list)

RESOURCE_APPLY_URL = (
    f"https://api.yext.com/v2/accounts/me/resourcesapplyrequests?api_key={API_KEY}&v={V}"
)
for account in range(len(account_list)):
    ky_request_body = {
        "targetAccountId": f"{account}",
        "source": {"type": "GitHub", "url": "https://github.com/cxi2319/fonecta-ky-dashboard"},
    }

    ya_request_body = {
        "targetAccountId": f"{account}",
        "source": {"type": "GitHub", "url": "https://github.com/alexyang528/fonecta-ya-dashboard"},
    }

    hs_request_body = {
        "targetAccountId": f"{account}",
        "source": {"type": "GitHub", "url": "https://github.com/alexyang528/fonecta-hs-dashboard"},
    }
    requests.post(RESOURCE_APPLY_URL, json=ky_request_body)
    requests.post(RESOURCE_APPLY_URL, json=ya_request_body)
    requests.post(RESOURCE_APPLY_URL, json=hs_request_body)
