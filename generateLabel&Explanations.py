import os
import json
os.environ["CUDA_VISIBLE_DEVICES"]="0"
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import numpy as np
import random
import torch
torch.manual_seed(0)
random.seed(0)
np.random.seed(0)


data = []
for line in open("test.jsonl"):
    line = json.loads(line)
    data.append(line)

model_dir = "./output/"
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
model.cuda()


for i in range(len(data)):
    sentence_A = data[i]["premise"]
    sentence_B = data[i]["hypothesis"]
    instruction = "Does the sentence "+'"'+sentence_A+'" entail or contradict the sentence "'+sentence_B+'"? Please answer between '+'"Entails" or "Contradicts" and explain your decision in a sentence.'
    inputs = tokenizer.encode(instruction, return_tensors="pt")
    outputs = model.generate(input_ids=inputs.cuda(), no_repeat_ngram_size=2, min_length=10, do_sample=True, max_length=128, top_k=5,temperature=0.7,eos_token_id=tokenizer.eos_token_id)
    answer = tokenizer.decode(outputs[0],skip_special_tokens=True)
    if "Entails." in answer:
        predictedlabel = "Entailment"
        predictedExpl = answer.split("Entails.")[1].lstrip().capitalize()
    elif "Contradicts." in answer:
        predictedlabel = "Contradiction"
        predictedExpl = answer.split("Contradicts.")[1].lstrip().capitalize()
    data[i]["predicted_label"] = predictedlabel
    data[i]["model_explanation"] = predictedExpl

with open("./output/predictions.json","w") as f:
    f.write(json.dumps(data,indent=4))


