f = open("/Users/kateferrandino/adventinputs/day1-1.txt","r")
lines = f.readlines()
times_increased = 0
previous_value = 9999999
for line in lines:
    value = int(line)
    if value > previous_value:
        times_increased += 1
    previous_value = value

print(times_increased)