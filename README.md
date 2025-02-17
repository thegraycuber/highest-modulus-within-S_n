# Highest $` U_k `$ within $` S_n `$
This repository is intended to calculate terms for [A380222](https://oeis.org/A380222) - Highest integer k such that the multiplicative group modulo k is a subgroup of the symmetric group $`S_n`$.  

## Introduction
This sequence begins: 2, 6, 6, 12, 18, 30, 42, 60, 90, 126, 210, 252, 420... The 10th term is 126. This means two things:  
### First, $` U_{126} \subseteq S_{10} `$  
  
To go step-by-step, we break the multiplicative group into a product using its prime powers:  
### $` U_{126} \cong U_2 \times U_9 \times U_7 `$  
Being prime powers, each $`U_{p^k}`$ is a cyclic group of order $`\phi(p^k)`$  
### $`U_2 \times U_9 \times U_7 \cong C_1 \times C_6 \times C_6 `$  
The cyclic group of order 1 is trivial. Since 2 and 3 are coprime, $`C_6 \cong C_2  \times C_3 `$  
### $`C_1 \times C_6 \times C_6 \cong C_2 \times C_3 \times C_2 \times C_3  `$  
We can represent $`C_2`$ in $`S_{10}`$ with the generator (1 2), $`C_3`$ with (3 4 5), $`C_2`$ with (6 7), and $`C_3`$ with (8 9 10).  

### Second, there is no k > 126 such that $` U_k \subseteq S_{10} `$    
  
This is harder to demonstrate. How do we know without checking all integers? Well, higher moduli tend to have larger multiplicative groups, so we aim find an upper bound for a given n, and then just check up to that point. But in order to do that, we first should understand more generally how to determine if $` U_k \subseteq S_n `$  

## Abelian Subgroups of $` S_n `$

We generalize the process used to show that $` U_{126} \subseteq S_{10} `$.

The multiplicative groups are abelian, so by the [fundamental theorem of finite abelian groups](https://en.wikipedia.org/wiki/Abelian_group#Classification), $`U_k`$ is isomorphic to some product of prime power cyclic groups:  
### $`U_k \cong C_{p_1} \times C_{p_2} \times ... \times C_{p_r}`$  

As shown by [John D. Dixon](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3DB42029FAAF5CF128361D73E6E211CD/S0008414X00053360a.pdf/maximal-abelian-subgroups-of-the-symmetric-groups.pdf), each maximal abelian subgroup $`A \subseteq S_n`$ is as follows:  
### $`A \cong A_1 \times A_2 \times ... \times A_m `$
such that $`\displaystyle\sum |A_j| \leq n`$  

For each $`A_j \cong \displaystyle\prod C_{j,i}`$ we have $`\displaystyle\sum |C_{j,i}| \leq |A_j|`$ and therefore $`\displaystyle\sum\sum |C_{j,i}| \leq \displaystyle\sum |A_j| \leq n`$  

This is shown for maximal abelian subgroups, but will also apply to all abelian subgroups since their sum would be less than or equal to some maximal subgroup. Therefore, if $` U_k \subseteq S_n `$ then
$`\displaystyle\sum p_i = \leq n`$. We saw this above, 2 + 3 + 2 + 3 = 10, so $` U_{126} \subseteq S_n `$ for any $`n \geq 10.`$

For k in general, we find [the structure](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n#Structure) of $`U_k`$ as follows:  
### $`U_k \cong \displaystyle\prod\prod C_{p_{i,j}}`$ 
Where $`2^a, q_1, q_2, ...`$ are the prime powers of k  
  $`p_{i,1}, p_{i,2}, ... `$ be the prime powers of odd $`\phi(q_i)`$  
  and for $`2^a`$: $`p_{0,1} = 2, p_{0,2} = 2^{a-2}`$ if a > 2, $`p_{0,1} = 2`$ if a = 2, and there be no such $`p_{0,j}`$ if a < 2.  

This gives a method by which to calculate the size of symmetric group needed for each $`U_k`$, which we will now apply to find an upper bound. We denote $`\displaystyle\sum\sum p_{i,j} = weight_k`$ such that $`U_k \subseteq S_n `$ for any n $`\geq weight_k`$.

## Finding an upper bound

To find the highest $` U_k `$ within $` S_n `$ we will find an upper bound for prime values of k, then consider the products of primes below this bound.

### Theorem 1: If k is a prime greater than the mth primorial $`p_m\#`$ then $`weight_k \geq m(p_m\#)^\frac{1}{m}`$.

We first show that if k is a prime between the mth and m+1th primorials, then $`weight_k \geq m(k-1)^\frac{1}{m}`$.

Given that k is prime, there is only 1 prime power: $`q_1 = k`$ itself. Therefore $`weight_k`$ is simply the sum of prime powers of $`\phi(k) = k-1`$. Because k is less than the m+1th primorial, there are at most m prime powers of k-1.

Suppose k-1 has r prime powers $`p_1, ... p_r`$. We show by induction on r that $`weight_k \geq r(k-1)^\frac{1}{r}`$. This is clear when r = 1. 

Let r = 2, with $`k-1 = p_1p_2`$. Consider the function $`f(x) = x + \frac{k-1}{x}`$. The function is minimal at $`f(\sqrt{k-1}) = 2\sqrt{k-1}`$ and so $`weight_k = f(p_1) \geq 2\sqrt{k-1}`$.  

We now suppose that this holds for r-1. Using this induction hypothesis $`weight_k = \displaystyle\sum p_i \geq p_1 + (r-1)(k-1/p_1)^\frac{1}{r-1}`$. We will consider the function $`g(x) = x + (r-1)(k-1/x)^\frac{1}{r-1}`$. g is minimal at $`(k-1)^\frac{1}{r}`$ and it follows that $`weight_k \geq r(k-1)^\frac{1}{r}`$.  

It remains to show that $`r(k-1)^\frac{1}{r} \geq m(k-1)^\frac{1}{m}`$. It is sufficient to show that $`(m-1)(x)^\frac{1}{m-1} \geq m(x)^\frac{1}{m}`$ for all x greater than the mth primorial. We begin by setting these equal and solving for x:  
### $`(m-1)x^\frac{1}{m-1} = mx^\frac{1}{m}`$ &nbsp; $` \longrightarrow `$ &nbsp; $`x^\frac{1}{m(m-1)} = \frac{m}{m-1} `$ &nbsp; $`\longrightarrow`$ &nbsp; $` x = (\frac{m}{m-1})^{m(m-1)}`$   
We now show that $`(\frac{m}{m-1})^{m(m-1)}`$ is less than the mth primorial, using induction on m. This is only relevant when m > 1, so we begin by showing this explicitly for 2, 3, and 4.  
  
$`2^2 = 4 < p_2\# = 6`$  
$`\frac{3}{2}^6 \approx 11.39 < p_3\# = 30`$  
$`\frac{4}{3}^{12} \approx 31.57 < p_4\# = 210`$  
  
We now show that each following term increases by a factor less than 11. We do this using the limit definition of e to show that the factor is less than $`e^2`$. Since each following prime is at least 11, this proves the case when k is between the mth and m+1th primorials:  
### $`\frac{(\frac{m}{m-1})^{m(m-1)}}{(\frac{m-1}{m-2})^{(m-1)(m-2)}} `$ &nbsp; $`=`$ &nbsp; $` (\frac{m}{m-1})^{2(m-1)}(\frac{m(m-2)}{(m-1)^2})^{(m-1)(m-2)} `$ &nbsp; $`<`$ &nbsp; $` (\frac{m}{m-1})^{2(m-1)}`$ &nbsp; $` < e^2 < 11`$

To prove Theorem 1 we notice that $`(m+1)(p_{m+1}\#)^\frac{1}{m+1} > (m)(p_m\#)^\frac{1}{m}`$ since they are the geometric means of the first m+1 and m primes. Each k greater than the mth primorial is between some m+rth and m+r+1th primorials, so by induction on r: 
### $`weight_k `$ &nbsp; $` \geq `$ &nbsp; $` (m+r)(k-1)^\frac{1}{m+r}`$ &nbsp; $`  \geq `$ &nbsp; $` (m+r)(p_{m+r}\#)^\frac{1}{m+r} `$ &nbsp; $` \geq `$ &nbsp; $` m(p_m\#)^\frac{1}{m}`$

This gives us an upper bound. Using only primes below the mth primorial, we can calculate all terms of this sequence below $`m(p_m\#)^\frac{1}{m}`$ since all higher primes will have a higher weight.

## Calculating terms below $`m(p_m\#)^\frac{1}{m}`$

Finding terms of this sequence can be approached as a [0/1 Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem). This is a well-known optimal packing programming problem. Given some set of items, each with a weight and value, which items should be selected to maximize the value under a certain weight threshold? Applied to A380222 each item is some prime power $`p^a`$, the weight is $`weight_p^a`$ as described above, and the value is $`ln(p^a)`$ since the Knapsack problem uses values additively. 

But notice, each item is a *prime power*, not just a prime. The 5th term is 18. We do need to check the higher powers of primes. This creates a problem for the Knapsack algorithm - we shouldn't allow more than one power from the same prime, but the standard algorithm does not account for any such restrictions. We *could* modify it to allow this, but instead will proceed with a different solution. Rather than using an item to represent each power of a prime, $`p, p^2, p^3 ...`$, we will have a sequence of items each being just p, the combination of which makes the higher powers. For example with the powers of 3, instead of using:  

$`item: 3,`$ &nbsp; $`weight_3 = 2,`$ &nbsp; $` value_3 = ln(3)`$   
$`item: 9,`$ &nbsp; $` weight_9 = 5,`$ &nbsp; $` value_9 = ln(9)`$   
$`item: 27,`$ &nbsp; $` weight_{27} = 11,`$ &nbsp; $` value_{27} = ln(27)`$   
$`item: 81,`$ &nbsp; $` weight_{81} = 29,`$ &nbsp; $` value_{81} = ln(81)`$   
...  

We will use:

$`item: 3_1,`$ &nbsp; $` weight_{3_1} = 2,`$ &nbsp; $` value_{3_1} = ln(3)`$   
$`item: 3_2,`$ &nbsp; $` weight_{3_2} = 3,`$ &nbsp; $` value_{3_2} = ln(3)`$   
$`item: 3_3,`$ &nbsp; $` weight_{3_3} = 6,`$ &nbsp; $` value_{3_3} = ln(3)`$   
$`item: 3_4,`$ &nbsp; $` weight_{3_4} = 18,`$ &nbsp; $` value_{3_4} = ln(3)`$   
...  

The weights of the new are the differences between consectutive weights of the old items. $`weight_{3_3} = 6 = 11 - 5 = weight_{27} - weight_9`$  . This approach works because these differences are non-decreasing. If the algorithm selects $`3_2`$ but not $`3_1`$ there will be no issues since it has effectively set aside 3 elements of $`S_n`$ to represent $`U_3`$. Only 2 are needed, but perhaps there would be no better option than leaving one element unmoved. To demonstrate that this is non-decreasing, recall that $`weight_k`$ is the sum of prime powers dividing $`phi(k)`$: 

$`weight_{p_1} = weight_p \leq p-1`$  
$`weight_{p_2} = weight_{p^2} - weight_p = p`$  
$`weight_{p_a} = weight_{p^a} - weight_{p^{a-1}} = (p-1)p^{a-2}`$ &nbsp; for a > 2

So to implement to Knapsack algorithm, which is done in highest_modulus_within_s_n.py, we prepare a list of items by checking all primes less than some mth primorial, and for each prime add a rows $`p_1, p_2, ...`$ until some $`weight_{p_j}`$ is found that exceeds $`m(p_m\#)^\frac{1}{m}`$. Then we input that list into the Knapsack algorithm and get our sequence. Fantastic! But we can't celebrate just yet.
### There is a problem.
This approach is inefficient. We can find the first 100 or so terms of the sequence, but this approach can't get much further. $`12(p_{12}\#)^\frac{1}{12} \approx 141.8`$ so to get 141 terms we must check *all* primes up to the 12th primorial, which is over 7 trillion. Checking primes that high will take a long time, and is unnecessary. The 141st term is 375 159 113 055 066 740 400, the highest prime factor of which is only 421. A more effcient approach to find higher terms is a modified version of the algorithm that I call the 'Incomplete Knapsack'.

## The Incomplete Knapsack algorithm

This version of the algorithm is effective when the list of items is incomplete. We don't need to have information for all items, just for the *best* items. Specifically, the items with the highest cost, where cost = value/weight. The input of this algorithm is that such list, as well as an upper bound C for the cost of missing items. $`C \geq cost_j`$ for any $`item_j`$ not present in the list.

First, we run the Knapsack algorithm on the list, which returns a sequence of candidate terms. We then try to validate each term by showing that it cannot be beaten by an optimal missing item, one with cost c. A term $`a_j`$ is valid if:  
### $`value(a_j) \geq value(a_{j-i}) + Ci`$ &nbsp; for all i such that $`0 < i \leq j`$
We can compute this more efficiently by just testing, which is sufficient if $`a_{j-1}`$ is valid
### $`value(a_j) \geq value(a_{j-1}) + C`$

Using this test, we step through each term until we find one that cannot be validated, and return all valid terms. So let's try it out!
### Results: 2, 6
The third term cannot be validated, because it is also 6. It's equal to the second term. In order to validate this the upped bound C must be 0, meaning all primes are included in the list. The reason $`a_2 = a_3`$ is that there are no items with weight 1. There is nothing available to improve upon $`a_2`$. Let's introduce a new bound: L is the lightest possible missing item. If L > 1 then we shouldn't need to validate $`a_2`$ against $`a_3`$. The test is now:
### $`value(a_j) \geq value(a_{j-i}) + Ci`$ &nbsp; for all i such that $`L \leq i \leq min(2L-1,j)`$

Using this test we can validate thousands of terms of the sequence! We just need to find appropriate values for C and L.

## Finding *another* upper bound

Take k to be a prime between the mth and m+1th primorials. We can place a lower bound on the weight as shown in the proof Theorem 1: $`weight_k \geq m(k-1)^\frac{1}{m}`$, which gives the following upper bound on the cost:
### $`\frac{ln(k)}{m(k-1)^\frac{1}{m}}`$  
As a function of k, this is decreasing for all values greater than or equal to the mth primorial, so we get the following upper bound on all k such that $`p_m\# < k < p_{m+1}\#`$:
### $`B_m = \frac{ln(p_m\#)}{mp_m\#^\frac{1}{m}}`$  
This upper bound would work great in practice but does not lend itself well to general proof. To extend to all primes above the mth primorial we would like to show that it is larger than the following upper bound: $`B_m > B_{m+1}`$. We can check that this is true for small values of m > 1, but proving it generally is difficult as we are dealing with both the logarithm of and fractional power of primorials. However we can loosen this bound into a state that makes a proof more straightforward.

### Theorem 2: For all prime $`k > p_m\# `$ with m > 3 we have $`cost_k < b_m`$ where
### $`b_m = 1.5\frac{(m+1)(ln(m+1)+2ln(ln(m+1)))}{m^2}`$

We first show that $`cost_k < b_m`$ for all prime k between the mth and m+1th primorials, m > 3.

To demostrate this, we first loosen the upper bound on the value of k. Given that k is less than the m+1th primorial we have $`value_k < ln(p_{m+1}\#)`$. By [Proposition 5.1, Dusart](https://arxiv.org/pdf/1002.0442):   
### $`ln(p_{m+1}\#) = \vartheta(p_{m+1}) < 1.00003(p_{m+1})`$.  
By [Theorem 2, Rosser](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms/s2-45.1.21) for any m > 3 we have $`p_{m+1} < (m+1)(ln(m+1) + 2ln(ln(m+1)))`$ which gives a more explicit upper bound of:  
### $`ln(p_{m+1}\#) < 1.00003(m+1)(ln(m+1)+2ln(ln(m+1)))`$   

We now turn our attention to the lower bound of the weight of k: $`mp_m\#^\frac{1}{m}`$. By [Theorem 5.2, Dusart](https://arxiv.org/pdf/1002.0442), for m > 1:  
### $`ln(p_m\#) = \vartheta(p_m) > (1-\frac{3.965}{ln(p_m)^2})p_m`$.  
Using the lower bound $`p_m > mln(m)`$ from [Theorem 1, Rosser](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms/s2-45.1.21) we get:  
### $`mp_m\#^\frac{1}{m} > me^{\frac{1}{m}(1-\frac{3.965}{ln(p_m)^2})p_m} > me^{(1-\frac{3.965}{ln(mln(m))^2})ln(m)}`$.  
For all $`m \geq 264, \frac{-3.965ln(m)}{ln(mln(m))^2} > ln(0.66) `$ such that:  
### $`mp_m\#^\frac{1}{m} > me^{ln(m)+ln(0.66)} = 0.66m^2`$
We verify by computer that this is also true for values $`264 > m > 3`$.

Combinining the upper value bound and lower weight bound, we prove this for k between the mth and m+1th primorials. We now view $`b_m`$ as a function over the reals, and notice that it is decreasing for all x > 3. This proves Theorem 2:
### $`b(x) = 1.5\frac{(x+1)(ln(x+1)+2ln(ln(x+1)))}{x^2}`$

Great, we can now be confident using $`b_m`$ as a value for the cost upper bound C in the Incomplete Knapsack algorithm. But it doesn't work well in practice as this bound is too weak. The prime with the highest cost is 3: $`cost_3 = 0.55`$ so in order to get the first few terms we need $`b_m < 0.55`$ meaning m > 13. This does not improve upon the issue with the finite knapsack approach, we still need to check all prime values up to a trillion!  

However, we can effectively approach this problem using both bounds $`B_m`$ and $`b_m`$. We select the desired m based upon how many primes to check, and calculate the stronger bound $`B_m`$. We then check all values j starting at m+1, verifying that $`B_j < B_m`$ until we find some j for which $`b_j < B_m`$. This confirms the validity of $`B_m`$ as an upper bound on the cost for all primes above the mth primorial. We do this confirmation and find the primes within the rust script. This is then run through the incomplete knapsack algorithm using A380222.py.  

### Using this approach, we can confirm over 21 thousand terms of the sequence in just a matter of minutes!
