"""
Schemas for Schedule meta data
"""
from configuration import ma

class ScheduleSchema(ma.Schema):
    """
    Schema for schedule
    """
    class Meta:
        fields = (
        'id', 
        'start_datetime', 
        'end_datetime', 
        'employee_number',
        )