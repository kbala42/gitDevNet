import json

with open("kamil.json") as f:
	data=json.load(f)
	print(data)
	print(data["ad"])
	print(data["soyAd"])

kimlikDictDumps=json.dumps(data, indent=4,sort_keys= True)
print(kimlikDictDumps)
