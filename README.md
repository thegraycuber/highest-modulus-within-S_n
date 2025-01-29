# WIP Highest $` U_k `$ within $` S_n `$
This repository is intended to calculate terms for [A380222](https://oeis.org/A380222) - Highest integer k such that the multiplicative group modulo k is a subgroup of the symmetric group $`S_n`$.  

## Introduction
This sequence begins: 2, 6, 6, 12, 18, 30, 42, 60, 90, 126, 210, 252, 420... The 10th term is 126. This means two things:  
### First 
$` U_{126} \subseteq S_{10} `$  
  
To go step-by-step, we break the multiplicative group into a product using its prime powers:  
### $` U_{126} \cong U_2 \times U_9 \times U_7 `$  
Being prime powers, each $`U_{p^k}`$ is a cyclic group of order $`\phi(p^k)`$  
### $`U_2 \times U_9 \times U_7 \cong C_1 \times C_6 \times C_6 `$  
The cyclic group of order 1 is trivial. Since 2 and 3 are coprime, $`C_6 \cong C_2  \times C_3 `$  
### $`C_1 \times C_6 \times C_6 \cong C_2 \times C_3 \times C_2 \times C_3  `$  
We can represent $`C_2`$ in $`S_{10}`$ with the generator (1 2), $`C_3`$ with (3 4 5), $`C_2`$ with (6 7), and $`C_3`$ with (8 9 10).  

### Second
There is no k > 126 such that $` U_k \subseteq S_{10} `$    
  
This is harder to demonstrate. How do we know wihtout checking all integers? Well, higher moduli tend to have larger multiplicative groups, so we aim find an upper bound for a given n, and then just check up to that point. But in order to do that, we first should understand more generally how to determine if $` U_k \subseteq S_n `$  

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

This gives a method by which to calculate the size of symmetric group needed for each $`U_k`$, which we will now apply to find an upper bound. We denote $`\displaystyle\sum\sum p_{i,j} = w_k`$ as the 
'weight' of k, such that $`U_k \subseteq S_n `$ for any n $`\geq w_k`$.

## Finding an Upper Bound

To find the highest $` U_k `$ within $` S_n `$ we will find an upper bound for prime values of k, then consider the products of primes below this bound.

### Lemma 1: If k is an odd prime between the mth and m+1th primorials, then $`w_k \geq m(k-1)^\frac{1}{m}`$.  

Given that k is prime, there is only 1 prime power: $`q_1 = k`$ itself. Therefore $`w_k`$ is simply the sum of prime powers of $`\phi(k) = k-1`$. Because k is less than the m+1th primorial, there are at most m prime powers of k-1.

Suppose k-1 has r prime powers $`p_1, ... p_r`$. We show by induction on r that $`w_k \geq r(k-1)^\frac{1}{r}`$. This is clear when r = 1. 

Let r = 2, with $`k-1 = p_1p_2`$. Consider the function $`f(x) = x + \frac{k-1}{x}`$. To minimize the function we find $`f'(x) = 1 - \frac{k-1}{x^2}`$ and solve for 0:  
### $`0 = 1 - \frac{k-1}{x^2}   \longrightarrow   k-1 = x^2   \longrightarrow   \sqrt{k-1} = x`$
Therefore the function is minimal at $`f(\sqrt{k-1}) = 2\sqrt{k-1}`$ and so $`w_k = f(p_1 \geq) 2\sqrt{k-1}`$.  

We now suppose that this holds for r-1. Using this induction hypothesis $`w_k = \displaystyle\sum p_i \geq p_1 + (r-1)(k-1/p_1)^\frac{1}{r-1}`$. We will consider the function $`g(x) = x + (r-1)(k-1/x)^\frac{1}{r-1}`$. To minimize, find the derivative:  
### $`g'(x) = 1 - \frac{k-1}{x^2}(\frac{k-1}{x})^{\frac{-(r-2)}{r-1}} = 1 - (\frac{k-1}{x^r})^{\frac{1}{r-1}}`$  
and then set to 0:  
### $`0 = 1 - (\frac{k-1}{x^r})^{\frac{1}{r-1}}   \longrightarrow   \frac{k-1}{x^r} = 1   \longrightarrow   (k-1)^\frac{1}{r} = x`$  
Thus g is minimal at $`(k-1)^\frac{1}{r}`$ and it follows that $`w_k \geq r(k-1)^\frac{1}{r}`$.  

To conclude Lemma 1 it remains to show that $`r(k-1)^\frac{1}{r} \geq m(k-1)^\frac{1}{m}`$. It is sufficient to show that $`(m-1)(x)^\frac{1}{m-1} \geq m(x)^\frac{1}{m}`$ for all x greater than the mth primorial. We begin by setting these equal and solving for x:  
### $`(m-1)x^\frac{1}{m-1} = mx^\frac{1}{m} \longrightarrow x^\frac{1}{m(m-1)} = \frac{m}{m-1} \longrightarrow x = (\frac{m}{m-1})^{m(m-1)}`$   
We now show that $`(\frac{m}{m-1})^{m(m-1)}`$ is less than the mth primorial, using induction on m. This is only relevant when m > 1, so we begin by showing this explicitly for 2, 3, and 4.  
  
$`2^2 = 4 < p_2\# = 6`$  
$`\frac{3}{2}^6 \approx 11.39 < p_3\# = 30`$  
$`\frac{4}{3}^{12} \approx 31.57 < p_4\# = 210`$  
  
We now show that each following term increases by a factor less than 11. Since each following prime is at least 11, this proves the Lemma.
### $`\frac{(\frac{m}{m-1})^{m(m-1)}}{(\frac{m-1}{m-2})^{(m-1)(m-2)}} = (\frac{m}{m-1})^{2(m-1)}(\frac{m(m-2)}{(m-1)^2})^{(m-1)(m-2)} < (\frac{m}{m-1})^{2(m-1)} < e^2 < 11`$

This gives us an upper bound. Using only primes below the mth primorial, we can calculate all terms of this sequence below $`m(p_m\#)^\frac{1}{m}`$. We will denote this $`u_m`$.

## Calculating terms below $`u_m`$




