1. Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan.

The algorithm we use is linear search because the rooms are ordered numerically and clearly labeled. Read the sign at the entrance. It indicates that rooms EY100–130 are to the left, so we turn left.
1. Walk forward, checking each room number sequentially.
2. Since the rooms are sorted in ascending order, we continue moving until we reach EY128.
3. Stop when EY128 is found.

This approach is efficient given the circumstances, as it scans the ordered sequence without unnecessary detours.


2. How many ”steps” it will take to find room EY128? And what is a “step” in this case?

It would take 19 steps to reach EY128, as we pass 15 doors before arriving at the correct room.

A step is defined as the movement required to reach the next door or make a turn. Each door passed counts as one step, and turning at a junction also adds one step.
Since the entrance is positioned at the bottom of the map, the search involves:

1. Moving left (following the sign).
2. Walking past 15 rooms sequentially.
3. Turning when necessary to stay within the EY100–130 range.

Thus, the total number of steps includes both forward movement and any required turns to navigate correctly.

3. Is this a best-case scenario, worst-case scenario, or neither?

This scenario is neither the best-case nor the worst-case.
A best-case scenario would occur if EY128 were the first room encountered, requiring minimal steps.
A worst-case scenario would involve searching all possible rooms before finding EY128, taking the maximum number of steps.
Since EY128 is near the middle of the search range, it doesn’t represent either extreme. 

4. With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like?

In the best-case scenario. You enter, turn right, and EY128 is just ahead, requiring minimal steps. This makes for a fast and efficient journey with no backtracking. In the worst-case scenario, you turn right but realize EY128 isn’t there, so you go all the way back to the entrance and start again. This makes the trip much longer and more as you waste time retracing your steps. 

5. Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm to make it more efficient?

When someone has memorized the building's layout, they can significantly improve navigation efficiency to EY128 by implementing an algorithm that capitalizes on their spatial knowledge. Rather than relying on signs and sequential decision-making, they can execute a direct path algorithm consisting of an immediate 90-degree right turn from the entrance, followed by walking straight along the right corridor until reaching EY128, which is the third room from the corner. This optimized approach eliminates the need to read and interpret signs, reduces the journey to a single straight-line movement, leverages the known fixed position of EY128 relative to the entrance, and minimizes mental processing by not reading numbered ranges. This would take 7 steps.
