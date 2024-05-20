class Employee:
    def __init__(self, salary, employment_type, organization_type, sum_assured):
        self.salary = salary
        self.employment_type = employment_type
        self.organization_type = organization_type
        self.sum_assured = sum_assured

class TaxCalculator:
    def __init__(self, employee, num_children, children_in_school):
        self.employee = employee
        self.num_children = num_children
        self.children_in_school = children_in_school
        self.taxable_income = employee.salary
        self.total_deductions = self.calculate_total_deductions()
        self.final_tax = self.calculate_final_tax()
        
    def calculate_total_deductions(self):
        total_deductions = 0
        if self.employee.employment_type in ["Regular", "Gov"]:
            total_deductions += self.employee.salary * 0.11  # 11% Employee 
            total_deductions += self.employee.salary * 0.16  # 16% Pension
            total_deductions += self.employee.salary * 0.10  # 10% Provident Fund

        if self.employee.organization_type == "Pvt":
            total_deductions += min(0.05 * self.employee.salary, 0.1 * self.employee.salary)

        for child in self.children_in_school:
            if child.lower() == "y":
                total_deductions += 350000  # Education allowance for each child in school
        return total_deductions
    
    def calculate_final_tax(self):
        taxable_income_after_deductions = self.taxable_income - self.total_deductions #it calculates the taxable income after subtracting the total deductions from the total taxable income.
        if taxable_income_after_deductions <= 300000:
            return 0 #If the taxable income after deductions is less than or equal to 300,000, the tax is 0
        elif 300000 < taxable_income_after_deductions <= 400000:
            return taxable_income_after_deductions * 0.10 #If the taxable income after deductions is greater than 300,000 but less than or equal to 400,000, the tax is calculated by multiplying the taxable income after deductions by 0.10 (10% tax rate).
        elif 400000 < taxable_income_after_deductions <= 650000:
            return taxable_income_after_deductions * 0.15 #If the taxable income after deductions is greater than 400,000 but less than or equal to 650,000, the tax is calculated by multiplying the taxable income after deductions by 0.15 (15% tax rate).
        elif 650000 < taxable_income_after_deductions <= 1000000:
            return taxable_income_after_deductions * 0.20 #If the taxable income after deductions is greater than 650,000 but less than or equal to 1,000,000, the tax is calculated by multiplying the taxable income after deductions by 0.20 (20% tax rate).
        elif 1000000 < taxable_income_after_deductions <= 1500000:
            return taxable_income_after_deductions * 0.25 #If the taxable income after deductions is greater than 1,000,000 but less than or equal to 1,500,000, the tax is calculated by multiplying the taxable income after deductions by 0.25 (25% tax rate).

        else:
            return taxable_income_after_deductions * 0.30 #If the taxable income after deductions is greater than 1,500,000, the tax is calculated by multiplying the taxable income after deductions by 0.30 (30% tax rate).

class GISCalculator:#defines a class named "GISCalculator".
    def __init__(self, employee): # Initialize a GISCalculator object with an Employee
        self.employee = employee

    def calculate_monthly_payment(self):
        return self.employee.sum_assured / 12 #calculates the monthly payment by dividing the sum_assured attribute of the employee object by 12

def get_user_input():#defines a function named "get_user_input"
    name = input("What is your Name: ")# prompts the user to input their name using the input() function. 
    position = input("What is your Occupation: ") # prompts the user to input their occupation using the input() function.
    salary = float(input("Enter your salary(atleast 300,000): ")) # prompts the user to input their salary as a floating-point number using the input() function.

    if salary < 300000: #checks if the value stored in the variable salary is less than 300,000.
        print("Your salary must be at least 300,000.") #If the condition salary < 300000 is true, this line will execute and print the message "Your salary must be at least 300,000." to the console.
        return None

    employment_type = input("Enter your employment type (Contract/Regular): ")
    organization_type = input("Enter your organization type (Gov/Pvt/Corp): ")

    sum_assured = float(input("Enter the sum assured for GIS: "))
    num_children = int(input("Enter the number of children: "))

    children_in_school = [] #initializes an empty list named children_in_school. 
    for i in range(num_children): # starts a loop that iterates over a range of numbers from 0 to num_children
        children_in_school.append(input(f"Is child {i+1} in school? (Y/N): ")) # prompts the user with a question using the input() function.

    return Employee(salary, employment_type, organization_type, sum_assured), num_children, children_in_school

def main():#defines a function named main
    user_input = get_user_input()
    if user_input:
        employee, num_children, children_in_school = user_input
        tax_calculator = TaxCalculator(employee, num_children, children_in_school)
        gis_calculator = GISCalculator(employee)

        print(f"Your final tax amount is: {tax_calculator.final_tax}")#prints a message indicating the final tax amount calculated by the TaxCalculator instance.
        print(f"Your monthly GIS payment is: {gis_calculator.calculate_monthly_payment()}") #prints a message indicating the monthly GIS payment calculated by the GISCalculator instance.

if __name__ == "__main__":#checks if the special built-in variable __name__ is equal to "__main__"
    main() # ensures that the main() function is executed only when the script is run directly, not when it's imported as a module.
 