from django.shortcuts import render, redirect
from django.contrib import messages


import requests
import json
import time


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
        if request.method == 'POST':
            amounts = request.POST['amount']
            number = request.POST['number']
            amount = float(amounts)
            json_data = json.loads(response.text)
            access_token = json_data['access']

            url = "https://payments.paypack.rw/api/transactions/cashin"

            payload = json.dumps({
                "amount": amount,
                "number": number
            })
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Bearer {access_token}'
            }

            response = requests.request(
                "POST", url, headers=headers, data=payload)
            reference = json.loads(response.text)
            # ref = reference['ref']
            print(reference)
            messages.info(request, 'Your transaction is being processed')
            return render(request, 'processing.html')
        else:
            return render(request, 'pay.html')
