"""
# Old way or procedural programming method
let baseSalary = 30,000;
let overtime = 10;
let rate = 20;

function getWage(baseSalary, overtime, rate) {
    return baseSalary + (overtime * rate);
}
"""

# New way using OOP

class Getwage:
    def __init__(self, base_salary, overtime, rate):
        self.base_salary = base_salary
        self.overtime = overtime
        self.rate = rate

    def calculate_wage(self):
        return self.base_salary + (self.overtime * self.rate)
    
wage1 = Getwage(30000, 10, 20)
print(wage1.calculate_wage())
print()
wage2 = Getwage(40000, 5, 25)
print(wage2.calculate_wage())