from django.forms import ModelForm
from .models import *
from django import forms
class DateInput(forms.DateInput):
	input_type = 'date'
class MissingChild(ModelForm):
	class Meta:
		model = MissingChildren 
		fields = ['name', 'age','height','sex','complexion', 'face', 'hair', 'eye', 'state', 'missing_date']
		widgets = {
			'missing_date' : DateInput(),
		}
class StolenVehicle(ModelForm):
	class Meta:
		model  = StolenVehicles
		fields = ['vehicle_type', 'reg_num', 'eng_num', 'chassis_num']

# class DateInput(forms.DateInput):
# 	input_type = 'date'
# class TimeInput(forms.TimeInput):
# 	input_type = 'time'
# class AddCustomer(ModelForm):
# 	class Meta:
# 		model = Customer
# 		fields = ['name', 'room_type', 'contact_number', 'Dob' ,'address', 'Payment_mode', 'Rating', 'Review']
# 		widgets = {
# 			'Dob' : DateInput(),
# 		}

# class AddRoom(ModelForm):
# 	class Meta:
# 		model = Room 
# 		fields = '__all__'


# class AddEmployee(ModelForm):
# 	class Meta:
# 		model = Employee
# 		fields = ['name', 'dep_id', 'contact_number', 'dob', 'address', 'join_date', 'working_hours', ]
# 		widgets = {
# 			'dob' : DateInput(),
# 			'join_date' : DateInput(),
# 		}

# class AddSupplier(ModelForm):
# 	class Meta:
# 		model = Supplier
# 		fields = ['name', 'contact_number', 'address', 'email',]

# class AddItems(ModelForm):
# 	class Meta:
# 		model = Logistics
# 		fields = ['name', 'price', 'quantity', 'supp_id',]

# class AddOrder(ModelForm):
# 	class Meta:
# 		model = Orders
# 		fields = ['cus_id', 'service_id', 'item_id', 'bill_amount', 'item_quantity', 'service_quantity']
# 		widgets = {
# 			'bill_amount' : forms.HiddenInput(),
# 		}

# class AddService(ModelForm):
# 	class Meta:
# 		model = Services
# 		fields = ['start_time', 'end_time', 'age_restriction', 'price', 'name', 'availibility', ]
# 		widgets = {
# 			'start_time' : TimeInput(),
# 			'end_time'	: TimeInput(),
# 		}

# class AddVisitor(ModelForm):
# 	class Meta:
# 		model = Visitor
# 		fields = ['name', 'contact_number', 'cus_id', ]


# # class AddSupply(ModelForm):
# # 	class Meta:
# # 		model = Supply
# # 		fields = ['item_id', 'supplier_id', ]

# class SelectRoom(forms.Form):
# 	room_type = forms.ChoiceField(choices=Room_Types)