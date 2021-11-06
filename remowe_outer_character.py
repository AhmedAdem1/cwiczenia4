def outer_char(x):
    x=x.replace(x[0],"",1)
    x=x.replace(x[-1],"",1)
    print(x)

outer_char("string")
