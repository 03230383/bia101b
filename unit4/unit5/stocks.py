class Employee:
    def __init__(self, pf_contribution=True, gis_contribution=True, children=0):
        self.pf_contribution = pf_contribution
        self.gis_contribution = gis_contribution
        self.children = children


class IncomeTaxCalculator:
    def __init__(self, income, employee=None, employment_type="Regular", organization_type="Private"):
        self.income = income
        self.employee = employee
        self.employment_type = employment_type
        self.organization_type = organization_type

    def calculate_tax(self):
        # Consider PF and GIS contributions
        if self.employee:
            if not self.employee.pf_contribution:
                self.income += 0  # Modify as per actual PF deduction rules
            if not self.employee.gis_contribution:
                self.income += 0  # Modify as per actual GIS deduction rules

        # Calculate Gross Total Income
        gross_total_income = self.income

        # Deductions
        deductions = 0
        if self.employee:
            # Education allowance
            deductions += min(350000, self.income)
            # Life insurance premium
            deductions += 0  # Placeholder for actual deduction calculation
            # Self-education allowance
            deductions += min(350000, self.income)
            # Donations
            deductions += min(0.05 * gross_total_income, self.income)
            # Sponsored children education expenses
            deductions += min(350000, self.income) * self.employee.children

        adjusted_gross_income = gross_total_income - deductions

        # Tax calculation based on adjusted gross income
        if adjusted_gross_income <= 300000:
            tax = 0
        elif 300001 <= adjusted_gross_income <= 400000:
            tax = (adjusted_gross_income - 300000) * 0.1
        elif 400001 <= adjusted_gross_income <= 650000:
            tax = 10000 + (adjusted_gross_income - 400000) * 0.15
        elif 650001 <= adjusted_gross_income <= 1000000:
            tax = 35500 + (adjusted_gross_income - 650000) * 0.20
        elif 1000001 <= adjusted_gross_income <= 1500000:
            tax = 80500 + (adjusted_gross_income - 1000000) * 0.25
        else:
            tax = 180500 + (adjusted_gross_income - 1500000) * 0.30

        # Apply surcharge for private sector employees
        if self.organization_type == "Private":
            tax = self.apply_surcharge(tax)

        return tax

    def apply_surcharge(self, tax):
        if tax >= 1000000:
            surcharge = 0.1 * tax
            tax += surcharge
        return tax

    def calculate_net_income(self):
        tax = self.calculate_tax()
        net_income = self.income - tax
        return net_income


# Example usage:
employee1 = Employee(pf_contribution=True, gis_contribution=True, children=2)  # Example employee characteristics
income = 800000  # Example income
calculator = IncomeTaxCalculator(income, employee=employee1)
tax = calculator.calculate_tax()
net_income = calculator.calculate_net_income()

print(f"Total Tax Payable: Nu. {tax}")
print(f"Net Income: Nu. {net_income}")
