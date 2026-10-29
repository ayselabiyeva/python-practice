from basics.rewrite import high_risks 

def test_high_risk():
    risks = [
        {"name": "Data leak", "severity": 5, "owner": "IT"},
        {"name": "Budget overrun", "severity": 3, "owner": "Finance"},
        {"name": "Server outage", "severity": 4, "owner": " it "},
        {"name": "Staff turnover", "severity": 2, "owner": "HR"},
    ]

    assert high_risks(risks) == ["Data leak", "Server outage"]
