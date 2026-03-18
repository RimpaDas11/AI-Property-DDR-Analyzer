def merge_data(obs1, obs2):
    merged = []
    seen = set()
    for obs in obs1 + obs2:
        key = obs["type"] + str(obs["page"])
        if key not in seen:
            merged.append(obs)
            seen.add(key)
    return merged
