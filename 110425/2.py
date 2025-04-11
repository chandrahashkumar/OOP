# # How to print, which type of error generate
# try:
#     n = int(input())
#     print(n)
# except:
#     print("Error")
#
# finally:
#     print("OK")

try:
   with open('data.csv') as file:
       read_data = file.read()
except FileNotFoundError as fnf_error:
   print(fnf_error)
   print("Explanation: We cannot load the 'data.csv' file")
