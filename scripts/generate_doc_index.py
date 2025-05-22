import os

index_lines = ["# Document Index", "", "This index lists the Markdown files in the `documents` folder.", ""]

for root, _, files in os.walk('documents'):
    files.sort()
    for fname in files:
        if not fname.lower().endswith('.md'):
            continue
        path = os.path.join(root, fname)
        rel = os.path.relpath(path, 'documents')
        description = ''
        with open(path, 'r', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line:
                    description = line.lstrip('#').strip()
                    break
        index_lines.append(f"- [{rel}]({rel}) - {description}")

with open('documents/INDEX.md', 'w') as f:
    f.write('\n'.join(index_lines) + '\n')
print(f"Wrote {len(index_lines)-4} entries to documents/INDEX.md")
