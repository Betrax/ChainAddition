<<<<<<< HEAD
for x in range (9, 10):
    print (x)
=======
import time

start_time = time.time()

print(all(198418741 % x != 0 for x in range(2, 9999999999)))

print((time.time() - start_time), "secs")

for x in range(2, 9999999999):
    if 198418741 % x == 0:
        print("false")
print((time.time() - start_time), "secs")
>>>>>>> fe34b7d0f175cbc91577a23df29951a6c2e4e8b5
