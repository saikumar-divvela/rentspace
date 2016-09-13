from userprofile.models import User
import userprofile.error_codes as message

import traceback

def createuser(username,password,first_name,last_name,phone_number):
	response = {}
	response["status"] = message.SUCCESS
	try:
		if username is None or password is None or first_name is None or last_name is None or phone_number is None:
			raise Exception(message.MISSING_INPUT_FIELD)

		if is_user_exists(username):
			raise Exception(message.DUP_USER)

		if is_phone_exists(phone_number):
			raise Exception(message.DUP_PHONE_NUMBER)

		# Only pass the required fields defined in models.py

		user = User.objects.create_user(email=username,password=password,phone_number=phone_number)
		print (user,user.password)
		user.first_name = first_name
		user.last_name = last_name
		user.save()

		response["message"] = message.REGISTER_USER_SUCCESS

	except Exception as exp:
		print (exp)
		traceback.print_exc()
		response["status"] = message.ERROR
		response["message"]= str(exp)

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

