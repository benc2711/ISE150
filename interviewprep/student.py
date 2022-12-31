

class Student(object):
    def __init__(self, skill, id, level):
        self.skill = skill
        self.id = id
        self.level = level
    def getSkill(self):
        return self.skill
    def getId(self):
        return self.id
    def getLevel(self):
        return self.level
    def getChosenSkill(self, chosenSkill):
        return self.level[chosenSkill]



