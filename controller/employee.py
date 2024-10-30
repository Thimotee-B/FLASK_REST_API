"""
Controller for employee
"""
from flask import request
from models.employee import Employee
from schemas.employee import EmployeeSchema
from configuration import db
import uuid


def read_all():
    employees = Employee.query.all()
    return EmployeeSchema(many=True).dump(employees), 202


def create():
    data = request.get_json()
    try:
        print(f"#### {data}")

        employee = Employee(
            name=data.get("name"),
            schedule_id=uuid.UUID(data.get("schedule_id"))
        )
        employee_schema = EmployeeSchema()
        db.session.add(employee)
        db.session.commit()
        return employee_schema.jsonify(employee), 200
    except Exception as err:
        print(f"#### ERROR = {err}")
        return ["ERROR"], 400