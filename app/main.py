import requests
import pya3rt
import json

def main(argv):

	apikey = {
	"talk":"EQ9oy99wFbKhOPsC72wQf2o8VRAiAcmM",
	"classification":"he8d4f19qXWFISJzo0dgu2XlYShCo2Zy"
	}
	#client1 = pya3rt.TalkClient(apikey["talk"])
	#print(client1.talk("おはよう"))

	#client = pya3rt.TextClassificationClient(apikey["classification"])

	for i, v in enumerate(argv):
		payload = {'apikey': apikey["classification"], 'model_id':"","text":v}
		r = requests.post('https://api.a3rt.recruit-tech.co.jp/text_classification/v1/classify', data=json.dumps(payload))
		print(r.text)

