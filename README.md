# Necessary modules:
-pygame
-math

# How it works?
Tentacle is separated into segments of certain lenght - here lenght of each section is 8px and number of secttions is 50. End of the tentacle always follows user cursor - speed of following is define by the distance between the tentacle end point and cursor. For each time step (time step is not defined, tentacle updates for every frame instead) program iterates through the tentacle backwards and first sets the position of the end point, then moves every following point according to the lenght of each segment. This way however the tentacle as a whole would follow the cursor, so another loop is introduced which iterates other way from the beginnig of the tentacle to it's end and sets it's first position to a certain point, then moves every point the same way as in the first loop. Resulting tentacle:

![image](https://user-images.githubusercontent.com/94861828/148652663-81c55c33-a9d0-4bd4-bf0e-69a368e86db1.png)

By changing the L and N values (file main.py lines 12 and 13) to L = 80 and N = 3 it is possible to simulate something resembling a robotic arm:

![image](https://user-images.githubusercontent.com/94861828/148652648-42757e4e-9a91-474c-bd66-2f1bd44abb20.png)



