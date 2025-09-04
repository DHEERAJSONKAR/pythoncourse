# 6. you can also create a if elif ladder using multiple condition of elif.
''' . for undrstanding solve this questions
take the input a temperatura in celcius.
. Below 0c - Freezing Cold
. 0c to 10c - very cold
. 10c to 20c - cold
. 20c to 30c - pleasant
. 30c to 40c - hot
. above 40c - very hot
.'''

t = int(input("Please tell us Temperature :- "))
if t<0:
    print("Freezing cold")
elif t>=0 and t<10:
    print("Very cold")
elif t>=10 and t< 20:
    print("cold")
elif t>=20 and t<30:
    print("pleasant")
elif t>=30 and t<40:
    print("hot")
else:
    print("very hot")