s = input()
s1 = s.split(" ")
start = int(s1[0])*60 + int(s1[1])
end  = int(s1[2])*60 + int(s1[3])
hour = (end-start)// 60
minute = (end-start)% 60
print("{}:{}".format(hour,minute))