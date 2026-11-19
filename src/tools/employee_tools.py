
from pydantic import BaseModel, Field
from langchain.tools import tool

from src.data.mock_employee_data import EMPLOYEES


class EmployeeLookupInput(BaseModel):
    employee_id: int = Field(
        gt=0,
        description="Employee ID"
    )


@tool(args_schema=EmployeeLookupInput)
def get_employee(employee_id: int) -> dict:
    """
    Get basic employee details using employee ID.
    Use this tool when someone asks about an employee.
    """

    employee = EMPLOYEES.get(employee_id)

    if employee is None:
        return {
            "success": False,
            "error": "Employee not found."
        }

    return {
        "success": True,
        "data": {
            "employee_id": employee_id,
            "name": employee["name"],
            "department": employee["department"],
            "designation": employee["designation"],
            "employment_status": employee["employment_status"],
            "joining_date": employee["joining_date"]
        }
    }
