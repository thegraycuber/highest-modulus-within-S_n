# Highest $` U_k `$ within $` S_n `$
This repository is intended to calculate terms for [A380222](https://oeis.org/A380222) - Highest integer k such that the multiplicative group modulo k is a subgroup of the symmetric group $`S_n`$.  

This sequence begins: 2, 6, 6, 12, 18, 30, 42, 60, 90, 126, 210, 252, 420...

## The 10th term is 126. This means two things.  
### First:  
$` U_{126} \subseteq S_{10} `$  
  
To go step-by-step, we break the multiplicative group into a product using its prime powers:  
$` U_{126} \cong U_2 \times U_9 \times U_7 `$  
Being prime powers, each $`U_{p^k}`$ is a cyclic group of order $`\phi(p^k)`$  
$`U_2 \times U_9 \times U_7 \cong C_1 \times C_6 \times C_6 `$  
The cyclic group of order 1 is trivial. Since 2 and 3 are coprime, $`C_6 \cong C_2  \times C_3 `$  
$`C_1 \times C_6 \times C_6 \cong C_2 \times C_3 \times C_2 \times C_3  `$  
We can represent $`C_2`$ in $`S_{10}`$ with the generator (1 2), $`C_3`$ with (3 4 5), $`C_2`$ with (6 7), and $`C_3`$ with (8 9 10).  

### Second:  
There is no k > 126 such that $` U_k \subseteq S_{10} `$    
  
This is harder to demonstrate. How do we know wihtout checking all integers? Well, higher moduli tend to have larger multiplicative groups, so we aim find an upper bound for a given n.

## Finding an Upper Bound

The multiplicative groups are abelian, so by the [fundamental theorem of finite abelian groups](https://en.wikipedia.org/wiki/Abelian_group#Classification), $`U_k`$ is isomorphic to some product of prime power cyclic groups:  
$`U_k \cong C_{p_1} \times C_{p_2} \times ... \times C_{p_r}`$  

As shown by [John D. Dixon](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3DB42029FAAF5CF128361D73E6E211CD/S0008414X00053360a.pdf/maximal-abelian-subgroups-of-the-symmetric-groups.pdf), each maximal abelian subgroup $`A \subseteq S_n`$ is as follows:  
$`A \cong A_1 \times A_2 \times ... \times A_m `$  
where $`\displaystyle\sum |A_j| \leq n`$  

For each $`A_j \cong \displaystyle\prod C_{j,i}`$ ,  
$`\displaystyle\sum |C_{j,i}| \leq |A_j|`$  

Therefore, $`\displaystyle\sum\sum |C_{j,i}| \leq \displaystyle\sum |A_j| \leq n`$  

This is shown for maximal abelian subgroups, but will also apply to all abelian subgroups since their sum would be less than or equal to some maximal subgroup. Therefore, if $` U_k \subseteq S_n `$ then
$`\displaystyle\sum p_i \leq n`$  


