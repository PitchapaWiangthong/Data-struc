print("*** Rabbit & Turtle ***")
d,Vr,Vt,Vf = (map(int,input("Enter Input : ").split()))
Sf = Vf*(abs(d/(Vr-Vt)))
print("{:.2f}".format(Sf))