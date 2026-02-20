class cmp242Coders:
    def __init__(self):
        self .__grade = None

    def set_grade(self, score):
        self.__grade = score

    def __getattr__(name):
        return (self.__grade)