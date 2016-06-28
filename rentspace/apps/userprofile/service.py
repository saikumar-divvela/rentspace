from userprofile.models import User
from userprofile.error_codes import *



def createuser(username,password,first_name,last_name,phone_number):
	response = {}
	response["status"] = ERROR
	try: 

		if username is None or password is None or first_name is None or last_name is None or phone_number is None:
			response["code"] =	MISSING_CONTENT_CODE
			response["msg"] = MISSING_CONTENT_MSG
			return response

		if is_user_exists(username):
			response["code"] = DUP_USER_CODE
			response["msg"] =  DUP_USER_MSG
			return response

		if is_phone_exists(phone_number):
			response["code"] = DUPL_PHONE_NUMBER_CODE
			response["msg"] =  DUPL_PHONE_NUMBER_MSG
			return response	

		# Only pass the required fields defined in models.py
		
		user = User.objects.create_user(email=username,password=password,phone_number=phone_number)
		print (user,user.password)
		user.first_name = first_name
		user.last_name = last_name
		user.save()
		
		response["status"] = SUCCESS
		response["code"] = 0
		response["msg"] = "User created successfully "

	except:
		response["code"] =ERROR_CODE		
		response["msg"]= ERROR_MSG

	return response		


def validate_email_format():
	print ('validating email format')


def is_user_exists(username):
	print ('validating user')
	try:
		User.objects.get(email=username)
	except User.DoesNotExist:
		return False
	return True

def is_phone_exists(phone_number):
	print ('validating phone')
	try:
		User.objects.get(phone_number=phone_number)
	except User.DoesNotExist:
		return False
	return True

