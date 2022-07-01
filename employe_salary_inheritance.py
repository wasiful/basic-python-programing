from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass()
# abstract base class for employees which holds name id and compute _pay function
class Employee(ABC):
    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        """ """


# create super class
@dataclass
class HourlyEmployee(Employee):  # passing the abc

    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    employe_cost: float = 1000

    def compute_pay(self) -> float:
        return(
            self.pay_rate * self.hours_worked
            +self.employe_cost
            +self.commission * self.contracts_landed
        )


@dataclass
class SalariedEmployee(Employee):
    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        return(
            self.monthly_salary * self.percentage
        )


@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):  # a subclass of salaried Employee
    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return(super().compute_pay()  # calling the super compute method and adding rest of it
            +self.commission * self.contracts_landed
        )


@dataclass
class Freelancer(Employee):
    pay_rate: float = 0
    hours_worked: int = 0
    vatnumber: str = ""

    def compute_pay(self) -> float:
        return(
            self.pay_rate * self.hours_worked
        )


@dataclass
class FreelancerWithCommission(Freelancer):  # subclass of Freelancer
    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return(
            super().compute_pay()  # super receives the previous return from  main class
            +self.commission * self.contracts_landed
        )


def main() -> None:
    henry = HourlyEmployee(name="henry", id=123, pay_rate=50, hours_worked=100)
    print(f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}")
    sarah = SalariedEmployeeWithCommission(
        name="Sarah", id=12345, monthly_salary=5000, contracts_landed=10
    )
    print(f"{sarah.name} landed {sarah. contracts_landed} contracts and earned ${sarah.compute_pay()}")


if __name__ == "__main__":
    main()