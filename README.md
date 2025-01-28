# Highest $` U_k `$ within $` S_n `$
This repository is intended to calculate terms for [A380222](https://oeis.org/A380222) - Highest integer k such that the multiplicative group modulo k is a subgroup of the symmetric group S_n.  

This sequence begins: 2, 6, 6, 12, 18, 30, 42, 60, 90, 126, 210, 252, 420...

### For demonstration, the 10th term is 126. This means two things:  
First:  
$` U_{126} \subseteq S_{10} `$   
To go step-by-step, we break the multiplicative group into a product using its prime powers:  
$` U_{126} \cong U_2 \times U_9 \times U_7 `$  
Being prime powers, each $`U_{p^k}`$ is a cyclic group of order $`\phi(p^k)`$  
$`U_2 \times U_9 \times U_7 \cong C_1 \times C_6 \times C_6 `$  
The cyclic group of order 1 is trivial. Since 2 and 3 are coprime, $`C_6 \cong C_2  \times C_3 `$  
$`C_1 \times C_6 \times C_6 \cong C_2 \times C_3 \times C_2 \times C_3  `$  
We can represent $`C_2`$ in $`S_{10}`$ with the generator (1 2), $`C_3`$ with (3 4 5), $`C_2`$ with (6 7), and $`C_3`$ with (8 9 10).  

Second:  
There is no k > 126 such that $` U_k \subseteq S_{10} `$   
This is harder to demonstrate. That is the purpose of this repository!  
