from odoo import api, fields, models

class Patient(models.Model):
    # this will create a table in postgres named "Hospital_Patient"
   _name = "hospital.patient"  #small case is the convention donot change it
   _description = "This python data class is related to the Hospital Patient"


    # this will create columns in the table "Hospital_Patient"
    # there will be some magic fields in the table provided by the odoo
   name = fields.Char(string = "Name")
   age = fields.Integer(string = "Age")

   #Always make sure tuple are seprated properly.
   # will have to follow the convention
   gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")