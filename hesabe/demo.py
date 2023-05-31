import json
import requests
import crypt
import webbrowser

key = 'Replace your Secret Key'
iv = 'Replace your IV Key'
accessCode = 'Replace your Access Code' 
base_url = "https://sandbox.hesabe.com"

data = {
    'merchantCode': 'Replace your Merchant code',
    'currency': 'KWD',
    'amount': 'Replace your Amount as float',
    'responseUrl': 'Replace your Success URL',
    'paymentType': 1,
    'version': '2.0',
    'orderReferenceNumber': 'Replace your Order Reference code',
    'failureUrl': 'Replace your Fail retirect page URL',
    'variable1': '',
    'variable2': 'Replace your ammount',
    'variable3': '',
    'variable4': '',
    'variable5': ''
}

requestDataJson = json.dumps(data)


class Hesabe(object):
    def __init__(self, data):
        self.data = data

    def checkout(self):
        print('Original data: ', type(self.data))
        try:
            encrypted = crypt.encrypt(str(json.dumps(self.data)), key, iv)
        except:
            return {'error': 'key or iv is incorrect please check'}
        payload = encrypted
        print('\nencrypted data: ', payload)
        response = requests.request("POST", base_url + "/checkout", headers={'accessCode': accessCode,
                                                                             'Accept': 'application/json'},
                                    data={'data': payload})
        print('\nresponse encrypted data: ', response.text)
        try:
            decrypted = crypt.decrypt(response.text, key, iv)
            decrypted_json = json.loads(decrypted)
            payment_token = decrypted_json["response"]["data"]
            response_data = {"payment_url": base_url + "/payment?data=" + payment_token}
            # return json.dumps(response_data)
            return response_data
        except:
            return {'error': "Authentication failed, please check access code"}


hesabe = Hesabe(data)
response = hesabe.checkout()
print(response)

if 'payment_url' in response:
    payment_url = response['payment_url']
    webbrowser.open(payment_url)
else:
    print("Error: Payment URL not found.")