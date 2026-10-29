import json

risks = [
    {"name": "Data leak", "severity": 5, "owner": "IT"},
    {"name": "Budget overrun", "severity": 3, "owner": "Finance"},
    {"name": "Server outage", "severity": 4, "owner": " it "},
    {"name": "Staff turnover", "severity": 2, "owner": "HR"},
]


def word_count(text: str) -> dict:
    list_of_words = text.split()
    seen_words = {}
    for word in list_of_words:
        word = word.strip().lower()
        if word in seen_words:
            seen_words[word] += 1
        else:
            seen_words[word] = 1

    return seen_words


def high_risks(risks: list) -> list:
    filtered_risks = sorted(risks, key=lambda x: x["severity"], reverse=True)
    return [risk["name"] for risk in filtered_risks if risk["severity"] >= 4]


def group_by_owner(risks: list) -> dict:
    grouped_owners = {}
    for risk in risks:
        owner = risk["owner"].strip().lower()
        if owner not in grouped_owners:
            grouped_owners[owner] = []
        grouped_owners[owner].append(risk["name"])

    return grouped_owners


class Risk:
    def __init__(self, name, severity):
        self._name = name
        self._severity = severity

    def is_critical(self):
        return self._severity >= 4


def save_risks(risks: list, path):
    with open(path, "w") as f:
        json.dump(risks, f)


def load_risks(path):
    with open(path) as f:
        text = json.load(f)
    return text


def test_high_risk():
    risks = [
        {"name": "Data leak", "severity": 5, "owner": "IT"},
        {"name": "Budget overrun", "severity": 3, "owner": "Finance"},
        {"name": "Server outage", "severity": 4, "owner": " it "},
        {"name": "Staff turnover", "severity": 2, "owner": "HR"},
    ]

    assert high_risks(risks) == ["Data leak", "Server outage"]
