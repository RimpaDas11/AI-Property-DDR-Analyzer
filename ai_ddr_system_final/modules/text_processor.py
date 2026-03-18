def extract_observations(text_data):
    observations = []
    for page in text_data:
        text = page["text"]
        if not text:
            continue
        t = text.lower()
        if "dampness" in t:
            observations.append({"type": "dampness", "page": page["page"], "text": text})
        if "leakage" in t:
            observations.append({"type": "leakage", "page": page["page"], "text": text})
        if "crack" in t:
            observations.append({"type": "crack", "page": page["page"], "text": text})
    return observations
