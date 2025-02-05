## Question 1:
Interpolation search is better then binary search when the data is uniformly ordered because it does not always split the array in half, but instead it estimates where most likely the element is within the array. This often means fewer comparisons to find correct element. Interpolation search also achieves an average-case time complexity of O(loglogn), compared to O(logn) for binary search. By leveraging the fact that the data is already sorted it is able to 'guess' its way to the correct location in the array to where the element is.


## Question 2:
If the data does not follow a uniform distribution then it will result in the algorithm making poor estimations of where the elemtn is within he array. This leads to many unnecessary comparisons which can degrade the algorithm’s performance to O(n) in the worst case. The reason for this is that interpolation search calculates an estimated position based on a uniform spread of values, which no longer holds true if the data is skewed or clustered. Therefore the "guessing" trick that the algorithms uses to easily find the element loses its advantage which goes to show how the performance of an Interpolation search heavily depends on the uniformity of the data.


## Question 3:
In the interpolation search code, the line that calculates pos is the main logic. That line uses the uniform distribution assumption to estimate where the target is most likely to be. For a different distribution, we must replace the fraction (x−arr[low])/(arr[high]−arr[low]) with a more suitable function which depends on how exactly the data is distributed. The rest of the code will remain the same. Adjusting this single part ensures that the algorithm is better suited for the actual data spread and not uniform distribution.


## Question 4:
Linear search is the only choice when the data is unsorted. Both binary and interpolation searches rely on the assumption that the data is sorted, allowing them to skip large portions of the search space and look specifcally at a smaller portion. If no ordering exists, these algorithms cannot function effectively. Therefore scanning each element from start to finish is the only solution for such scenarios.


## Question 5:
Linear search can outperform the others when the dataset is very small or if the target is known to be found near the beginning of the data. In these cases, the process of halving the data in binary search or calculating estimated positions in interpolation search offer no real benefit as a linear search that starts at the beginning will find the target faster. Also, if there is no  ordering or if elements are inputted in a way that breaks the uniform distribution assumption, those other two methods may degrade to near linear time anyway as stated in the previous answer above. Therefore, a straightforward linear search can outperform both binary and interpolation searches.


## Question 6:
One way to improve these search methods is to maintain a sorted dataset and proportionally distributed whenever possible which ensures that the benefits of these search methods are effective. If there is changing data, then it would be wise to have a function outside these searchs that inserts the new data is a way to perserve the uniform distribution of the overall data which ensures the searches never encounter an unsorted dataset. By ensuring the data is organized, you can be sure that the algorithms will not degrade to near linear search time complexity.