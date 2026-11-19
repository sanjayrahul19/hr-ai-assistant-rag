
from typing import TypedDict


class EmployeeRecord(TypedDict):
    employee_id: int
    name: str
    department: str
    designation: str
    employment_status: str
    joining_date: str
    annual_salary_inr: int
    leave_entitlements: dict[str, int]
    leave_used: dict[str, int]


EMPLOYEES: dict[int, EmployeeRecord] = {
    101: {
        "employee_id": 101,
        "name": "Rahul",
        "department": "Engineering",
        "designation": "Software Engineer",
        "employment_status": "Active",
        "joining_date": "2024-01-15",
        "annual_salary_inr": 1200000,
        "leave_entitlements": {
            "casual": 12,
            "sick": 10,
            "earned": 15
        },
        "leave_used": {
            "casual": 4,
            "sick": 2,
            "earned": 5
        }
    },

    102: {
        "employee_id": 102,
        "name": "Priya",
        "department": "HR",
        "designation": "HR Executive",
        "employment_status": "Active",
        "joining_date": "2023-06-10",
        "annual_salary_inr": 900000,
        "leave_entitlements": {
            "casual": 12,
            "sick": 10,
            "earned": 15
        },
        "leave_used": {
            "casual": 7,
            "sick": 3,
            "earned": 8
        }
    },

    103: {
        "employee_id": 103,
        "name": "Arjun",
        "department": "Finance",
        "designation": "Financial Analyst",
        "employment_status": "Active",
        "joining_date": "2022-09-20",
        "annual_salary_inr": 1100000,
        "leave_entitlements": {
            "casual": 12,
            "sick": 10,
            "earned": 15
        },
        "leave_used": {
            "casual": 2,
            "sick": 4,
            "earned": 3
        }
    }
}
