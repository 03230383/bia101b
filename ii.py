class Person:
    def __init__(self, name, income_source='Salary', organization_type='Private'):
        self.name = name
        self.income_source = income_source
        self.organization_type = organization_type
        self.deductions = {
            'education_allowance': 0,
            'life_insurance_premium': 0,
            'self_education_allowance': 0,
            'donations': 0,
            'sponsored_child_education': 0,
            'NPPF': 0,
            'children_tax_deduction': 0,
            'GIS': 0
        }

    def calculate_general_deductions(self, total_gross_income):
        general_deductions = (
            min(self.deductions['education_allowance'], 350000) +
            self.deductions['life_insurance_premium'] +
            min(self.deductions['self_education_allowance'], 350000) +
            min(self.deductions['donations'], total_gross_income * 0.05) +
            min(self.deductions['sponsored_child_education'], 350000) +
            self.deductions['NPPF'] +
            self.deductions['children_tax_deduction'] +
            self.deductions['GIS']
        )
        return general_deductions

    def calculate_tax(self, total_income):
        if total_income < 300000:
            return 0  # Exempt from taxation if gross income is below 300,000

        tax_payable = 0
        previous_limit = 0

        for limit, rate in tax_brackets:
            if total_income > limit:
                taxable_income = limit - previous_limit
                tax_payable += taxable_income * rate
                previous_limit = limit
            else:
                taxable_income = total_income - previous_limit
                tax_payable += taxable_income * rate
                break

        if tax_payable >= 1000000:
            tax_payable *= 1.1

        return tax_payable

class Employee(Person):
    def __init__(self, name, employment_income, pf_contribution, gis_contribution, position_type='Regular', **deductions):
        super().__init__(name, income_source='Salary')
        self.employment_income = employment_income
        self.pf_contribution = pf_contribution
        self.gis_contribution = gis_contribution
        self.position_type = position_type
        self.deductions.update(deductions)

    def calculate_income(self):
        total_gross_income = self.employment_income - self.pf_contribution - self.gis_contribution
        general_deductions = self.calculate_general_deductions(total_gross_income)
        return total_gross_income - general_deductions

class Landlord(Person):
    def __init__(self, name, rental_income):
        super().__init__(name, income_source='Rental')
        self.rental_income = rental_income

    def calculate_income(self):
        return self.rental_income * 0.8

class Investor(Person):
    def __init__(self, name, dividend_income, **deductions):
        super().__init__(name, income_source='Dividend')
        self.dividend_income = dividend_income
        self.deductions.update(deductions)

    def calculate_income(self):
        total_gross_income = self.dividend_income
        general_deductions = self.calculate_general_deductions(total_gross_income)
        return total_gross_income - general_deductions

class Consultant(Person):
    def __init__(self, name, other_income, **deductions):
        super().__init__(name, income_source='Consulting')
        self.other_income = other_income
        self.deductions.update(deductions)

    def calculate_income(self):
        total_gross_income = self.other_income
        general_deductions = self.calculate_general_deductions(total_gross_income)
        return total_gross_income - general_deductions

# Define the tax brackets and rates for Bhutan
tax_brackets = [
    (300000, 0.0),  
    (400000, 0.1),  
    (650000, 0.15), 
    (1000000, 0.2), 
    (1500000, 0.25), 
    (float('inf'), 0.3)  
]

# Example usage
employee = Employee("Karma", 250000, 50000, 10000, position_type='Regular', education_allowance=200000, life_insurance_premium=30000, donations=20000)
landlord = Landlord("Tshering", 400000)
investor = Investor("Wangmo", 100000, donations=15000)
consultant = Consultant("Jatsho", 700000, life_insurance_premium=25000, self_education_allowance=40000)

# Calculate and print taxes including general deductions
for person in [employee, landlord, investor, consultant]:
    income = person.calculate_income()
    tax = person.calculate_tax(income)
    print(f"\n{person.name}'s total income: Nu. {income:.2f}")
    print(f"{person.name}'s total tax payable: Nu. {tax:.2f}")

# Print exemption for individuals with gross income below 300,000
exempted = [person.name for person in [employee, landlord, investor, consultant] if person.calculate_income() < 300000]
if exempted:
    print("\nExempted from taxation (Gross income below 300,000):")
    for name in exempted:
        print(name)
