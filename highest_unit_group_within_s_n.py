
"""
This program generates sequence A380222: 
the highest k for which the multiplicative group modulo k is a subgroup of the symmetric group of degree n

Notation:
multiplicative group modulo k (units mod k): U_k
symmetric group of degree n: S_n
cyclic group of order a: C_a

For example, a(10) = 126 because U_126 is a subgroup of S_10 and there is no higher such value  
U_126 ≅ U_2 x U_9 x U_7 ≅ C_6 x C_6 ≅ C_2 x C_3 x C_2 x C_3
2 + 3 + 2 + 3 = 10, so U_126 is a subgroup of S_n for any n >= 10

In this example, we'll say that U_126 has 'weight' 10
This is the sum of the weights of its prime powers:
U_2 has weight 0, U_9 has weight 5, and U_7 has weight 5

To find terms in this sequence, we'll find the weight of each prime power up to some limit,
then check combinations of such prime powers.

The weight of a prime power p^r = sum(prime powers dividing phi(p^r))
For example, weight 121 = sum(prime powers dividing 110) = sum(2, 5, 11) = 18

Suppose a prime power p^r is between the jth and j+1th primorial.
phi(p^r) is divisible by at most j prime powers.
phi(p^r) is at least p^r /2
Therefore weight(p^r) > j * jth root of (p^r /2)

This function uses a given jth primorial as the upper limit.
Any prime power > jth primorial has weight > j * jth root of (primorial /2)
Therefore we can find all terms of the sequence for n < j * jth root of (primorial /2)
by checking just all prime powers < jth primorial.

So let's do it up!
"""


# add a number to the list of primes, where each row is [p, weight of p] 
def add_prime(prime):

    # starting checking 2 above the highest prime
    test_number = prime[-1][0] + 2
    
    # check until a prime is found
    while True:
        p = 0
        is_prime = True
        while prime[p][0] ** 2 <= test_number:
            if test_number % prime[p][0] == 0:
                is_prime = False
                break
            p += 1

        # if a prime p is found, add it to the list, along with the # of primes that divide p-1
        if is_prime:
            cycles, prime = get_prime_fact(test_number-1,prime)
            prime.append([test_number,sum([x[0]**x[1] for x in cycles])])
            return(prime)

        test_number += 2



# get the prime factorization of m. Returns with primes and exponents
# the return value for m = 720 is [[2,4],[3,2],[5,1]]
def get_prime_fact(m,prime,odd_cube_return = False):

    current_prime = 0
    factors = [[0]]

    # use m_current to track value of m that hasn't been accounted for yet
    m_current = m 
    while m_current > 1:

        # add a prime to the list if needed
        if len(prime) <= current_prime:
            prime = add_prime(prime)

        while m_current % prime[current_prime][0] == 0:
            # if the current prime has already been tracked, add 1 to the count
            if factors[-1][0] == prime[current_prime][0]:
                factors[-1][1] += 1
            # otherwise, add a new element to track it
            else:
                factors.append([prime[current_prime][0],1])

            m_current = m_current // prime[current_prime][0]

        current_prime += 1

    # get rid of the [0] that is used to prevent an error when checking factors[-1][0] before anything is added
    factors.pop(0)

    return(factors,prime)


# recursively iterate through the primes, checking each possible combination
def primes_iterate(results,prime,p_index,curr_value,curr_weight,lowest_missing):

    # if at end, exit
    if p_index == len(prime):
        results_index = curr_weight
        while results_index < len(results) and results[results_index] < curr_value:
            results[results_index] = curr_value
            results_index += 1
        return results

    # otherwise, try each option that fits
    p_pow = 0
    pow_val = 1
    add_weight = 0
    while curr_weight+add_weight < lowest_missing:

        results = primes_iterate(results,prime,p_index+1,curr_value*pow_val,curr_weight+add_weight,lowest_missing)
        pow_val *= prime[p_index][0]
        p_pow += 1
        if p_pow == 1:
            add_weight = prime[p_index][1]
        else:
            add_weight = prime[p_index][1] + prime[p_index][0]**(p_pow-1)
    

    return results



def highest_units_in_s_n(j): # j is the index of limiting primorial

    prime = [[2,0],[3,2]] # each row is [p, weight of p]
    primorial = 6

    # find the jth primorial
    while len(prime) < j:
        prime = add_prime(prime)
        primorial *= prime[-1][0]


    weight_limit = j*((primorial/2)**(1/j))
    print('Upper Limit: ',weight_limit)
    results = [2]*int(weight_limit) # U_2 fits within any S_n

    # find all primes up to primorial limit
    while prime[-1][0] < primorial:
        prime = add_prime(prime)

    # remove primes with too high weight
    for p in range(len(prime)-1,-1,-1):
        if prime[p][1] > weight_limit:
            prime.pop(p)

    # powers of 2 weights are tricky so deal with them separately
    pow_2_weights = [0,-2,0,2]
    while pow_2_weights[-1]*2 + 2 < weight_limit:
        pow_2_weights.append(pow_2_weights[-1]*2)

    for pow_2 in range(1,len(pow_2_weights)):
        results = primes_iterate(results,prime,1,2**pow_2,pow_2_weights[pow_2]+2,weight_limit)

    results[0] = 0
    print(results)


highest_units_in_s_n(7)