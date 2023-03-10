from odoo import api, fields, models
from datetime import date


class Patient(models.Model):

    # this will create a table in postgres named "Hospital_Patient"

    _name = "hospital.patient"  # small case is the convention don't change it
    _inherit = ['mail.thread', 'mail.activity.mixin']


    _description = "This python data class is related to the Hospital Patient"

    # this will create columns in the table "Hospital_Patient"
    # there will be some magic fields in the table provided by the odoo

    name = fields.Char(string="Name", default="ABC", tracking=True)
    date_of_birth = fields.Date (string = "Date of Birth",tracking=True)
    age = fields.Integer(string="Age", compute = "age_calculator")


    # Always make sure tuple are separated properly.
    # will have to follow the convention

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    room = fields.Selection([("room_a", "A Class"), ("room_b", "B Class")], string="Room", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)\

    @api.depends("date_of_birth")
    def age_calculator(self):
        today = date.today()
        # print("This is the data for self: --->  ",self)
        for i in (self):
            if i.date_of_birth:
               # print("This is the data for i.date_of_birth: --->  ",i.date_of_birth)
                i .age = today.year - i.date_of_birth.year
            else:
                i.age = 0


