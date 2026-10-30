import os

print("Directories under data/:")
for item in os.listdir('data'):
    full_path = os.path.join('data', item)
    if os.path.isdir(full_path):
        print(f"  [DIR]  data/{item} ({len(os.listdir(full_path))} items)")
    else:
        print(f"  [FILE] data/{item}")

if os.path.exists('archive'):
    print("\nDirectories under archive/:")
    for item in os.listdir('archive'):
        full_path = os.path.join('archive', item)
        if os.path.isdir(full_path):
            print(f"  [DIR]  archive/{item} ({len(os.listdir(full_path))} items)")
        else:
            print(f"  [FILE] archive/{item}")
