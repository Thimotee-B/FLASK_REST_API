"""
Schemas for Employee meta data
"""
from configuration import ma

class EmployeeSchema(ma.Schema):

    class Meta:
        fields = (
            "id",
            "name",
            "schedule_id",
        )
