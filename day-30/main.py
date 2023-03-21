# #FileNotFound
#
# try:  # check to see if the following codes fails or not
#         file = open("a_file.txt")
#         print("error" + "5")
# # run this if it fails; usually you want to run something that will make it succeed anyway
# # except needs specific errors
# except FileNotFoundError:
#         file = open("a_file.txt", "w")
#         file.write("Something")
# # you can have multiple errors
# # and you can grab the error itself and display it
# except TypeError as error_message:
#         print(f"Error: {error_message}")
# # if it works! will not be triggered if we dive into an except block
# else:
#         content = file.read()
#         print(content)
# # do this no matter what
# finally:
#         raise KeyError("This is an error that I made up")


height = float(input("height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human heights should not be over 3 meters")  # raise your own exceptions!

bmi = weight / height ** 2
print(bmi)
