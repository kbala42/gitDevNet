import json

kimlik={"ad":"Kamil","soyAd":"Bala"}

with open("kamil.json","w") as f:
	json.dump(kimlik,f)
