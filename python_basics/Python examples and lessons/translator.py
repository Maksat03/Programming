import requests 
import json

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
key = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97' 
lang = 'en-ru' 
enter = "[log] Enter the word: "
while True:
	text = input(enter)
	if len(str(text).split()) == 0:
		continue
	if text != "exit":
		r =	requests.post(url, data={'key': key, 'text': text, 'lang': lang}) 
		print(f"[log] Typed text: {text}")
		print(f"[log] Translated word: {json.loads(r.text)['text'][0]}")
		enter = "[log] Enter the following word: "
		continue
	break
print("[log] Good bye, see you soon!")