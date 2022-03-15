from postcodevalidate.func import postcode_validator


postcode=str(input('Enter UK post code to validate'))
if postcode_validator(postcode):
    print('VALID POSTCODE')
else:
    print('INVALID POSTCODE')   