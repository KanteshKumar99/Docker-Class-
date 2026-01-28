from pathlib import Path

current_dir = Path.cwd() #get current darictry respect with path
current_file = Path(__file__).name # get all files names

print(f"Files in {current_dir}:") # what current darictry 

for filepath in current_dir.iterdir():
    if filepath.name == current_file: # check whole files name if match
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content: {content}") #print file content