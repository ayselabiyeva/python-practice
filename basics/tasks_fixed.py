import json

#1 Task

def word_count(text: str) -> dict:
    list_of_words = text.split()
    seen = {}
    for word in list_of_words:
        if word in seen:
            seen[word] += 1
        else:
            seen[word] = 1

    return seen

#2 Task

risks = [{"name": "Data leak", "severity": 5, "owner": "IT"}, ...]

def high_risks(risks: list) -> list:
    risks_list = [ risk for risk in risks if risk["severity"] >= 4 ]
    return sorted(risks_list, key = lambda x: x["severity"], reverse=True)

#3 Task

def group_by_owner(risks: list) -> dict:
    seen_owners = {}
    # seyi anlamadim nasil yapiyim, yani kac tane suan owner var farkli farkli bilmiyoruz, o yuzden oyle yapmaliyim ki eger owner ayniysa direkt once varsa o dicte ilave etsin yoks ayenisini yaratsin amma bu yenisini yaratma kismini cozemedim. bir de owner isimlerini aynilastirmak da lazim.
    for risk in risks:
        owner = risk["owner"].strip().lower()
        if owner not in seen_owners:
            seen_owners[owner] = []
        seen_owners[owner].append(risk["name"])
    return seen_owners
#4 Task

class Risk:
    def __init__(self, name, severity):
        self._name = name
        self._severity = severity # mentorumun onceden yazdigi kodlardan aklimda kaldigi kadariyla yazmaya calistim, tam dogru mu bilmiyorum.


    def is_critical(self):
        return self._severity >= 4

#5 Task

def load_risks_from_json(json_string: str) -> list:
    return json.loads(json_string)

def save_risks_to_json(risks: list) -> str:
    with open("risks", "w") as f:
        return json.dump(risks, f)

def load_risks_from_json_file(file_path: str) -> list:
    with open(file_path) as f:
        return json.load(f)
#6 Task

def test_high_risk_owners(risks):
    risks = [{"name": "A", "severity": 5, "owner": "IT"}, 
             {"name": "B", "severity": 3, "owner": "IT"}, 
             {"name": "C", "severity": 4, "owner": "IT"}, 
             {"name": "A", "severity": 5, "owner": "HR"}, 
             {"name": "A", "severity": 2, "owner": "HR"}]

    assert high_risks(risks) == [{"name": "A", "severity": 5, "owner": "IT"}, 
                                 {"name": "C", "severity": 4, "owner": "IT"}, 
                                 {"name": "A", "severity": 5, "owner": "HR"}] 