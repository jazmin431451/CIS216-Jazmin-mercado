
class Employee:
    """This class supports the employee's name and their ID."""

    def __init__(self, name, employee_id):
        """Creates an employee with a name and an ID.

        Args:
            name (str): The employee's name.
            employee_id (int): The employee's ID.
        """
        self.name = name
        self.employee_id = employee_id

    @property
    def calculate_pay(self):
        """Gets the employee's calculated payment.

        Returns:
            float: The employee's calculated payment.
        """
        pass

class Manager(Employee):
    """This class supports the manager's salary claims in their payment."""

    def __init__(self, name, employee_id, salary):
        """Creates a manager with a name, ID, and salary.

        Args:
            name (str): The manager's name.
            employee_id (int): The manager's ID.
            salary (float): The manager's salary.

        Raises:
            ValueError: Salary cannot be negative.
        """
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        super().__init__(name, employee_id)
        self.salary = salary

    @property
    def calculate_pay(self):
        """Gets the manager's salary.

        Returns:
            float: The manager's salary.
        """
        return self.salary

class Salesperson(Employee):
    """This class supports the salesperson's claims in their sales commission rate."""

    def __init__(self, name, employee_id, commission_rate):
        """Creates a salesperson with a name, ID, and commission rate.

        Args:
            name (str): The salesperson's name.
            employee_id (int): The salesperson's ID.
            commission_rate (float): The salesperson's commission rate.

        Raises:
            ValueError: Commission rate should be less than 1.0.
        """
        if commission_rate >= 1.0:
            raise ValueError("Commission rate should be less than 1.0")
        super().__init__(name, employee_id)
        self.commission_rate = commission_rate

    @property
    def calculate_pay(self):
        """Calculates the salesperson's payment based on assumed total sales.

        Returns:
            float: The calculated payment for the salesperson.
        """
        total_sales = 10000
        return total_sales * self.commission_rate

class HourlyEmployee(Employee):
    """This class supports the employee's hourly rate and hours worked."""

    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        """Creates an hourly employee with a name, ID, hourly rate, and hours worked.

        Args:
            name (str): The employee's name.
            employee_id (int): The employee's ID.
            hourly_rate (float): The hourly rate.
            hours_worked (float): The hours worked.

        Raises:
            ValueError: Hourly rate and hours worked should be non-negative.
        """
        if hourly_rate < 0 or hours_worked < 0:
            raise ValueError("Hourly rate and hours worked should be non-negative")
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def calculate_pay(self):
        """Calculates the hourly employee's payment.

        Returns:
            float: The calculated payment for the hourly employee.
        """
        return self.hourly_rate * self.hours_worked

# Unit tests
if __name__ == "__main__":
    manager = Manager("John Doe", 101, 60000.0)
    salesperson = Salesperson("Jane Smith", 102, 0.1)
    hourly_employee = HourlyEmployee("Bob Johnson", 103, 15.0, 40.0)

    print(f"Manager Salary: ${manager.calculate_pay}")
    print(f"Salesperson Commission: ${salesperson.calculate_pay}")
    print(f"Hourly Employee Payment for 40 hours: ${hourly_employee.calculate_pay}")
