
#python3 api_user_requestpay.py
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

token = "4c4884a9-6338-4f7f-83e5-fb32f7c6b1e4"#paste token here

headers = {
    # Request headers
    'Authorization': 'Bearer '+token,
    #'X-Callback-Url': '<your domain name>',
    'X-Reference-Id': '26064d61-26fa-4016-afc2-30ad72338c16',#add your api user ID
    'X-Target-Environment': 'sandbox',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'cdfc45d3ac0647488cb639adf7701c80',#add product primary key
}

params = urllib.parse.urlencode({
})


body = json.dumps({

        "amount": "10",

        #use EUR when working in sandbox
        "currency": "EUR",
        "externalId": "1234",

        "payer": {"partyIdType": "MSISDN","partyId": "233543787887"}, #phone should start by 250

        "payerMessage": "You have made payment to me, thank you.",

        "payeeNote": "Payment received thank you."

    })

try:
    conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
    conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print('Response status :',response.status)
    print('Response reason :',response.reason)
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
