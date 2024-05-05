class Vacancy:
    id = 0

    def __init__(self, name, department, salary, snippet, schedule, professional_roles, experience):
        Vacancy.id += 1
        self.id = Vacancy.id
        self.name = name
        self.department = department
        self.salary = salary
        self.snippet = snippet
        self.schedule = schedule
        self.professional_roles = professional_roles
        self.experience = experience

    def __lt__(self, other):
        return
