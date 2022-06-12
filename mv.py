import json
a = []
with open ("SarcasmNLI.json") as f:
	data = json.load(f)


for line in open("sarcasm_test.jsonl"):
	line = json.loads(line)
	if line["id"] not in a and line["id"]<=834:
		a.append(line["id"])

f = open("sarcasm_test.jsonl","w")
for d in data:
	if d["id"] in a:
		f.write(json.dumps(d)+'\n')

f = open("sarcasm_train.jsonl","w")
for d in data:
	if d["id"] not in a:
		f.write(json.dumps(d)+'\n')