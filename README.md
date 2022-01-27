## LightestCoin
![image](/asset/img/scaleIllustration.png)

Python script for determining a fake coin in a bunch of real coins using a balance scale with the least amount of weighings.

### Why?
This algorithm simulates the best approach to solve the following puzzle:

>Given _n_ coins where all but one is of the same weight, find the least amount of weighings needed to determine
which of the coins is fake (lighter) using a balance scale.

It turns out that you need surprisingly few weighings to solve this puzzle, even for large amounts of coins due to the 
logarithmic nature of the best solution.

### The solution
The solution to the puzzle is best illustrated with an example using perhaps the most common number of coins, n=9, as
illustrated below.

![image](/asset/img/9coinsExample.png)

The key insight is to divide the number of coins into __three__. In the case where 3 does not divide n, round up such 
that two of the divided stacks are equal in size.
After dividing, weigh two of the equally divided stacks and discard all stacks of coins that do not contain the fake one.
If the two weighed stacks are equal, discard them both and keep the remaining stack that was not weighed.

![image](/asset/img/3coinsExample.png)

Repeat this process until each divided stack contains at most 1 coin. At this point, there is only one more weighing that
needs to be done before the answer is imminent.

The maximum number of weighings _W(n)_ is
<div style="text-align: center;">
<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;W(n)&space;=\left&space;\lceil{log_3(n)}\right&space;\rceil,&space;n&space;\in&space;\mathbb{Z^&plus;}" title="W(n) =\left \lceil{log_3(n)}\right \rceil, n \in \mathbb{Z^+}" />
</div>

### How does the algorithm work?
The algorithm follows the same procedure as mentioned above in a recursive manner. Whenever it encounters a number of 
coins that 3 does not divide, it weighs the two largest stacks. The plot below shows the number of weighings 
simulated for n = 1...100 as well as the theoretical maximum plotted as a red line.

![image](/asset/img/resultPlot.png)


Note that the algorithm often performs better than the maximum for values close but above 3<sup>k</sup> where k is some
positive integer. The reason for this is as follows:

Assume that you have 10 coins. This satisfies the condition that n is close to and above 9 = 3<sup>2</sup>. Divide the 
coins into 3 stacks as explained in the solution procedure. This yields two stacks of 4 and one of two. Assuming that 
the fake coin is selected by random using a flat probability distribution, the probability of the fake coin being in the
stack of 2 coins is 1/5. If this actually happens to be the case, the number of weighings left is only one, compared to
two if the coin was located in one of the stacks containing four coins.


