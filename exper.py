userDict ={}
uInput = "0"
while uInput != "0 0":

        uInput = input("Enter a room number followed by the duration of stay make sure there is a space. If you want to quit enter a ? ")
        uInputList = uInput.split(" ")
        if uInput != "0 0":
            userDict[int(uInputList[0])] = int(uInputList[1])
print(userDict)
# #
# # for key in userDict:
# #     print(userDict[key])
#
# # numberFloorDict = {}
# # for x in range(1,31,1):
# #     numberFloorDict[x] = 0
# # for key in numberFloorDict:
# #     print(str(key) + " : " + str(numberFloorDict[key]))
#
# userDict = {101:2, 3099: 3, 2054: -1, 3100: -1, 99:2, -546: 3, 3064: 2, 2134: 3, 2122:4, 2144: 5}
# newDict = {}
# negNights = 0
# invalidRoom =0
# for key in userDict:
#     if int(userDict[key]) < 0:
#         negNights += 1
#     elif int(key) < 100 or int(key) > 3099:
#         invalidRoom += 1
#     else:
#         newDict[key] = userDict[key]
# for key in newDict:
#     print(print(str(key) + " : " + str(newDict[key])))
#
# # for key in newDict:
# #     if len(str(key)) > 3:
# #         floor = key // 100
# #     else:
# #         floor = key // 10
# #     print(str(key) + " : " + str(newDict[key]) + " " + str(floor))