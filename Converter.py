print("1.   HEX --> RGB")
print("2.   RGB --> HEX")

inp = input()

def HEXRGB():
    print("Enter HEX")
    HEX = input().lstrip('#')
    HEX_R = int(str(HEX[0]) + str(HEX[1]))
    HEX_G = int(str(HEX[2]) + str(HEX[3]))
    HEX_B = int(str(HEX[4]) + str(HEX[5]))
    R = int(str(HEX_R), 16)
    G = int(str(HEX_G), 16)
    B = int(str(HEX_B), 16)
    print("Red: " + str(R), "Green: " + str(G), "Blue: " + str(B))

def RGBHEX():
    print("Enter red-value")
    R = int(input())
    print("Enter green-value")
    G = int(input())
    print("Enter blue-value")
    B = int(input())
    RGB = "%02x%02x%02x" % (R, G , B)
    print("#" + str(RGB))
if inp == "1":
    HEXRGB()
elif inp == "2":
    RGBHEX()
