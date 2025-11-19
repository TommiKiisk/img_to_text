import re

file = input("Mistä haluat etsiä? ")

with open(file, "r") as f:
    text = f.read()
    
search = input("Mitä haluat etsiä? ")

matches = list(re.finditer(search, text, flags=re.IGNORECASE))

if not matches:
    print("ei löytynyt")
else:
    print(f"Löytyi {len(matches)} osumaa:\n")
    
    for m in matches:
        start_idx = max(0, m.start() -60)
        end_idx = min(len(text), m.end() +60)
        
        context = text[start_idx:end_idx]
        
        highlight = re.sub(search,
                           lambda x: f"[{x.group(0)}]",
                           context,
                           flags=re.IGNORECASE)
        
        print(highlight)