import platform

# def boolQuestion(default):
#     inputRes = input()
#     match inputRes:
#         case "y":
#             res = "y"
#         case "Y":
#             res = "y"
#         case "n":
#             res = "n"
#         case "N":
#             res = "n"
#         case "":
#             res = default
#         case _:
#             print("Please answer \"Y\" or \"N\"")
#             res = boolQuestion(default)
#     return res

def boolQuestion(default):
    inputRes = input().lower()
    if inputRes == "y":
        res = "y"
    elif inputRes == "n":
        res = "n"
    elif inputRes == "":
        res = default
    else:
        print("Please answer \"Y\" or \"N\"")
        res = boolQuestion(default)
    return res

def isPlatformSupported():
    if "linux" == platform.system():
        res = "y"
    else:
        res = "n"
    return res

def getPlatform():
    print(platform.system())
    print(platform.release())
    print(platform.platform())
