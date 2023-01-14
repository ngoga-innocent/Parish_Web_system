from django.shortcuts import render, redirect


import requests
import json


def Authorization(request):
    url = "https://payments.paypack.rw/api/auth/agents/authorize"

    payload = json.dumps({
        "client_id": "6ac5ba12-9281-11ed-9030-dead986dd4f7",
        "client_secret": "b664f4cee485d97801ae0c5e4938954eda39a3ee5e6b4b0d3255bfef95601890afd80709"
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer {access_token}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.ok:

        json_data = json.loads(response.text)
        access_token = json_data['access']

        url = "https://payments.paypack.rw/api/transactions/cashin"

        payload = json.dumps({
            "amount": 1000,
            "number": '0726584581'
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        reference = json.loads(response.text)
        # ref = reference['ref']
        print(reference)

        # if response.ok:
        #     url = "https://payments.paypack.rw/api/transactions/find/"
        #     # url = url+f'Bearer{referencekey}'
        #     payload = {}
        #     headers = {'Authorization': f'Bearer {access_token}'}

        #     response = requests.request(
        #         "GET", url, headers=headers, data=payload)

        #     print(response.text)
        # # access = json_data['access']
        return render(request, 'payed.html')


# def Pay(request):
#     if request.method == 'POST':
#         amount = request.POST['amount']
#         number = request.POST['number']
#         access = request.POST['access_token']
#         accesses = json.loads(access)
#         access_token = accesses['access_token']
#         url = "https://payments.paypack.rw/api/transactions/cashin"

#         data = json.dumps({
#             "amount": amount,
#             "number": number
#         })
#         headers = {
#             'Content-Type': 'application/json',
#             'Accept': 'application/json',
#             'Authorization': 'Bearer{access_token}'
#         }

#         response = requests.request("POST", url, headers=headers, json=data)

#         print(response.text)
#         return render(request, 'home.html')
#     else:
#         return render(request, 'pay.html')
