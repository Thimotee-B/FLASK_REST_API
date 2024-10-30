"""
Model for Schedule
"""
from datetime import datetime
import uuid
from configuration import db


class Schedule(db.Model):
    __tablename__ = "schedule"

    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    start_datetime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    end_datetime = db.Column(db.DateTime, nullable=True)
    employee_number = db.Column(db.UUID, nullable=True)

    employee = db.relationship("Employee", uselist=False, back_populates="schedules")

    def to_dict(self):
        return {
            'id': self.id,
            'start_datetime': self.start_datetime,
            'end_datetime': self.end_datetime,
            'employee_number': self.employee_number,
        }
