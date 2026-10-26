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
    return risks_list.sort(reverse=True)

#3 Task

def group_by_owner(risks: list) -> dict:
    seen_owners = []
    # seyi anlamadim nasil yapiyim, yani kac tane suan owner var farkli farkli bilmiyoruz, o yuzden oyle yapmaliyim ki eger owner ayniysa direkt once varsa o dicte ilave etsin yoks ayenisini yaratsin amma bu yenisini yaratma kismini cozemedim. bir de owner isimlerini aynilastirmak da lazim.
    for risk in risks:
        risk["owner"].lower()
        # tam bilemedim ya

#4 Task

class Risk:
    def __init__(name, severity):
        self._name = name,
        self._severity = severity # mentorumun onceden yazdigi kodlardan aklimda kaldigi kadariyla yazmaya calistim, tam dogru mu bilmiyorum.


    def is_critical(severity):
        if severity >= 4:
            return "severity is critical"

        return "severity is not critical"

#5 Task

# bu json yazilimi okumasi falan tam hatirlamiyorum ya, bit tek json_load() boyle bir sey aklimda o kadar.

#6 Task

# test yazmayi da bilmiyorum :(