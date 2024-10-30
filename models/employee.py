"""
Model for employee
"""
from configuration import db
import uuid

class Employee(db.Model):
    __tablename__ = "employee"

    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50), nullable=True)
    schedule_id = db.Column(db.UUID(), db.ForeignKey('schedule.id'))

    schedules = db.relationship("Schedule", uselist=True, back_populates="employee")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'schedule_id': self.schedule_id,
        }
