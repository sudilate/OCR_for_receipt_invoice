import json
import requests
url = "https://ocr.aspire.com/api/v1/receipt"
image = "/Users/amitsarang/TextSummarization/receipt-ocr-original.jpg"

res = requests.post(url, 
                    data = {
                        'api_key': 'TEST',
                        'recognizer': 'auto',
                        'ref_no':'oct_python_123'
                    }, 
                    files={
                        'file': open(image, 'rb')
                    })

with open('output.json', 'w') as f:
    json.dump(json.loads(res.text), f)