import json

risks = [
    {"name": "Data leak", "severity": 5, "owner": "IT"},
    {"name": "Budget overrun", "severity": 3, "owner": "Finance"},
    {"name": "Server outage", "severity": 4, "owner": " it "},
    {"name": "Staff turnover", "severity": 2, "owner": "HR"},
]

def word_count(text: str) -> dict:
    seen_words = {}
    for word in text:
        word = word.strip().lower()
        if word in seen_words:
            seen_words[word] += 1
        else:
            seen_words = 1

    return seen_words

def high_risks(risks: list) -> list:
    high_risks = [risk for risk in risks if risk["severity"] >= 4]
    return sorted(high_risks, key=lambda x: x["severity"], reverse=True)

def group_by_owner(risks: list) -> dict:
    grouped_risks = {}
    for risk in risks:
        owner = risk["owner"].strip().lower()
        grouped_risks[owner].append(risk["name"])

    return grouped_risks

class Risk:
    def __init__(self, name, severity):
        self._name = name,
        self._severity = severity

    def is_critical(self):
        return self._severity >= 4


def save_risks(risks: list, ):
    with open(risks, "w") as f:
        json.dumps(f)

def load_risks(path):
    with open(path) as f:
        json.loads(f)

def test_high_risk():
    risks = [
        {"name": "Data leak", "severity": 5, "owner": "IT"},
        {"name": "Budget overrun", "severity": 3, "owner": "Finance"},
        {"name": "Server outage", "severity": 4, "owner": " it "},
        {"name": "Staff turnover", "severity": 2, "owner": "HR"},
    ]

    assert high_risks(risks) == [{"name": "Data leak", "severity": 5, "owner": "IT"}, 
                                {"name": "Server outage", "severity": 4, "owner": " it "},]