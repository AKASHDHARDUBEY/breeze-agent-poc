import json

def extract():
    skills = {}
    current = {}
    inside = False

    with open("docs.txt") as f:
        for line in f:
            line = line.strip()

            if line == "[SKILL]":
                inside = True
                current = {}

            elif line == "[/SKILL]":
                inside = False
                skills[current["id"]] = current

            elif inside and "=" in line:
                key, value = line.split("=")
                current[key] = value

    return skills


def save(skills):
    with open("skills.json", "w") as f:
        json.dump(skills, f, indent=2)

    print("skills.json created")


def check():
    new = extract()

    try:
        with open("skills.json") as f:
            old = json.load(f)
    except:
        print("skills.json missing")
        return

    if new != old:
        print("Drift detected ⚠️")
    else:
        print("No drift ✅")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        check()
    else:
        save(extract())
