import os, json

metadata = []
base_dir = os.path.join(os.path.dirname(__file__), '..', 'prompts')
for category in ['gpts', 'prompt_injections']:
    dir_path = os.path.join(base_dir, category)
    for fname in sorted(os.listdir(dir_path)):
        fpath = os.path.join(dir_path, fname)
        if not os.path.isfile(fpath):
            continue
        name = os.path.splitext(fname)[0]
        description = ''
        with open(fpath, 'r', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line:
                    description = line.lstrip('#').strip()
                    break
        metadata.append({'file': os.path.join(category, fname), 'name': name, 'description': description, 'category': category})

out_path = os.path.join(base_dir, 'metadata.json')
with open(out_path, 'w') as f:
    json.dump(metadata, f, indent=2)
print(f"Wrote {len(metadata)} entries to {out_path}")
