"""
Controller for schedule API
"""
from flask import request
from models.schedule import Schedule
from schemas.schedule import ScheduleSchema
from flask import request
from configuration import db
from utils.date_utils import convert_str_to_datetime
import uuid

def read_all():
    schedules = Schedule.query.all()
    return ScheduleSchema(many=True).dump(schedules), 202

def create():
    data = request.get_json()
    try:
        print(f"#### {data}")

        start_datetime = convert_str_to_datetime(data.get('start_datetime'))
        end_datetime = convert_str_to_datetime(data.get('end_datetime'))

        schedule = Schedule(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            employee_number=uuid.UUID(data.get('employee_number'))
        )
        schedule_schema = ScheduleSchema()
        db.session.add(schedule)
        db.session.commit()
        return schedule_schema.jsonify(schedule), 200
    except Exception as err:
        print(f"#### ERROR = {err}")
        return ["ERROR"], 400
