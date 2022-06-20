lst = {
    "black" : "0",
    "brown" : "1",
    "red" : "2",
    "orange" : "3",
    "yellow" : "4",
    "green" : "5",
    "blue" : "6",
    "violet" : "7",
    "grey" : "8",
    "white" : "9"
}
a = lst[input()]
b = lst[input()]
c = lst[input()]

print(int(a+b) * (10 ** int(c)))