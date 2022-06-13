try:
    Y_of_StartingSquare = int(input())
    X_of_StartingSquare = int(input())
    Y_of_TargetSquare = int(input())
    X_of_TargetSquare = int(input())
except:
    print("Only integer values")

if ((8 < Y_of_StartingSquare < 1) or (8 < X_of_StartingSquare < 1) or (8 < Y_of_TargetSquare < 1) or (
        8 < X_of_TargetSquare < 1)):
    print("No! Aut of chess border")
else:
    if (Y_of_StartingSquare == Y_of_TargetSquare) or (X_of_StartingSquare == X_of_TargetSquare) or (
            abs(Y_of_StartingSquare - X_of_StartingSquare) == abs(Y_of_TargetSquare - X_of_TargetSquare)):
        print("YES")
    else:
        print("NO")
