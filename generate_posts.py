import os
import openai
import datetime

# Configuration
openai.api_key = os.getenv("OPENAI_API_KEY")
amazon_tag = os.getenv("AMAZON_TAG")

# Generate a post using GPT
prompt = f"""Génère un article de blog en français pour 'Objets Malins du Quotidien' listant 5 gadgets utiles du quotidien avec leurs descriptifs et liens Amazon. Utilise ce tag affilié: {amazon_tag}."""
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=500
)

content = response.choices[0].text.strip()
date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
filename = f"_posts/{date}-gadgets-quotidien.md"
with open(filename, "w") as f:
    f.write(f"---
layout: default
title: Gadgets utiles du quotidien - {date}
date: {date}
---

")
    f.write(content)
