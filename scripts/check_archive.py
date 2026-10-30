import os

p = 'archive/unintegrated_staging'
print(f"Contents of {p}:")
for sub in os.listdir(p):
    subpath = os.path.join(p, sub)
    if os.path.isdir(subpath):
        print(f"  [DIR] {sub}: {len(os.listdir(subpath))} items")
    else:
        print(f"  [FILE] {sub}")
