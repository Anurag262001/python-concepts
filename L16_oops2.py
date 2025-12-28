class L16_oops2:
    
    def __init__(self,name,age,team):
        self.name=name
        self.age=age
        self.team=team
    def run(self):
        print(f"Hi {self.name} as per your age {self.age} your team is {self.team}")
team1 = "a"
team2 = "b"
banda1 = L16_oops2("anurag",13,team1)
print(banda1.team)
banda1.run()
banda2 = L16_oops2("yash",17,team2)
print(banda2.team)
banda2.run()
  