import os

def replace_in_file(filepath):
    print(f"Processing {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    replacements = {
        "Marjo Ballabani": "Aniket Maharana",
        "MARJO BALLABANI": "ANIKET MAHARANA",
        "Marjo": "Aniket",
        "marjoballabani": "aniketmaharana",
        "marjo-ballabani": "aniket-maharana",
        "marjo@ballabani": "aniket@maharana"
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

def main():
    directory = r"c:\Users\anike\Downloads\marjoballabani.me-master\marjoballabani.me-master"
    for root, dirs, files in os.walk(directory):
        if '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith(('.html', '.js', '.css', '.md', '.txt', '.xml', 'CNAME', 'LICENSE')):
                filepath = os.path.join(root, file)
                replace_in_file(filepath)

if __name__ == "__main__":
    main()
