print("Temp.Converter")
try:
 celsius = float(input("Enter temperature in Celsius: "))
 fahrenheit = (celsius * 9/5) + 32
 print(f"{fahrenheit}F")
 if fahrenheit >= 90:
  print("Its Hot")
 elif fahrenheit <= 50:
  print ("Its Cold")
 else:
  print("Its Normal")
except:
 print("Error.Please put NUMBER.")
 


 
