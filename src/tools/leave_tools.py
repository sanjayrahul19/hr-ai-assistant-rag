
from datetime import date, timedelta
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field
from langchain.tools import tool

from src.data.mock_employee_data import EMPLOYEES


LeaveType = Literal["casual", "sick", "earned"]


# -----------------------------
# Input schemas
# -----------------------------

class LeaveBalanceInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    employee_id: int = Field(gt=0, strict=True)


class LeaveEligibilityInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    employee_id: int = Field(gt=0, strict=True)
    leave_type: LeaveType
    start_date: date
    end_date: date


# -----------------------------
# Internal helper functions
# -----------------------------

def calculate_working_days(
    start_date: date,
    end_date: date
) -> int:
    """Calculate weekdays between two dates, inclusive."""

    working_days = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:
            working_days += 1

        current_date += timedelta(days=1)

    return working_days


# -----------------------------
# LangChain tools
# -----------------------------

@tool(args_schema=LeaveBalanceInput)
def calculate_leave_balance(employee_id: int) -> dict:
    """
    Get the remaining casual, sick and earned leave
    balance of an employee.
    """

    employee = EMPLOYEES.get(employee_id)

    if employee is None:
        return {
            "success": False,
            "error": "Employee not found."
        }

    balances = {}

    for leave_type, entitlement in employee["leave_entitlements"].items():
        used = employee["leave_used"][leave_type]

        balances[leave_type] = entitlement - used

    return {
        "success": True,
        "employee_id": employee_id,
        "leave_balances": balances
    }


@tool(args_schema=LeaveEligibilityInput)
def check_leave_eligibility(
    employee_id: int,
    leave_type: LeaveType,
    start_date: date,
    end_date: date
) -> dict:
    """
    Check whether an employee has sufficient leave
    balance for the requested dates.
    """

    employee = EMPLOYEES.get(employee_id)

    if employee is None:
        return {
            "eligible": False,
            "reason": "Employee not found."
        }

    if employee["employment_status"] != "Active":
        return {
            "eligible": False,
            "reason": "Employee is not active."
        }

    if start_date < date.today():
        return {
            "eligible": False,
            "reason": "Start date cannot be in the past."
        }

    if end_date < start_date:
        return {
            "eligible": False,
            "reason": "End date cannot be before start date."
        }

    requested_days = calculate_working_days(
        start_date,
        end_date
    )

    if requested_days == 0:
        return {
            "eligible": False,
            "reason": "No working days in the selected date range."
        }

    entitlement = employee["leave_entitlements"][leave_type]
    used = employee["leave_used"][leave_type]
    remaining = entitlement - used

    if requested_days > remaining:
        return {
            "eligible": False,
            "reason": "Insufficient leave balance."
        }

    return {
        "eligible": True,
        "employee_id": employee_id,
        "leave_type": leave_type,
        "requested_days": requested_days,
        "remaining_balance": remaining,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat()
    }
