N = int(input())
s1 = 0
s2 = 0
lead_s1 = 0
lead_s2 = 0
leader = 0
for i in range(N):
  p1, p2 = map(int, input().split())
  s1 += p1
  s2 += p2

  if s1 > s2:
    lead_s1 = max(lead_s1, s1 - s2)

  else:
    lead_s2 = max(lead_s2, s2 - s1)


if lead_s1 > lead_s2:
  print(1, lead_s1)
else:
  print(2, lead_s2)
#   temp = abs(s1 - s2)
#   if s1 > s2:
#     #  s1 is the leader
#     # temp = max(temp, s1 - s2)
#   if temp > lead:
#       lead = temp
#       leader = i + 1
# print(leader, lead)