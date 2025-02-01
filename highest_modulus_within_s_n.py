# This program generates sequence A380222:
# the highest k for which the multiplicative group modulo k is a subgroup of the symmetric group of degree n

from dataclasses import dataclass
import math


@dataclass
class Item:
    def __init__(self, index, prime, weight):
        self.index = index
        self.prime = prime
        self.weight = weight
        self.value = math.log(prime)
        self.cost = self.value / weight


@dataclass
class SequenceTerm:
    def __init__(self):
        self.modulus = 2  # U_2 is trivial
        self.weight = 0
        self.value = 0

    def replace(self, base_term, new_item):
        self.weight = base_term.weight + new_item.weight
        self.value = base_term.value + new_item.value
        self.modulus = base_term.modulus * new_item.prime

    def output_string(self, index):
        return str(index) + "," + str(self.modulus)


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
            cycles, prime = get_prime_fact(test_number - 1, prime)
            prime.append([test_number, sum([x[0] ** x[1] for x in cycles])])
            return prime

        test_number += 2


# get the prime factorization of m. Returns with primes and exponents
# the return value for m = 720 is [[2,4],[3,2],[5,1]]
def get_prime_fact(m, prime):
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
                factors.append([prime[current_prime][0], 1])

            m_current = m_current // prime[current_prime][0]

        current_prime += 1

    # get rid of the [0] that is used to prevent an error when checking factors[-1][0] before anything is added
    factors.pop(0)

    return (factors, prime)


# the 0/1 knapsack algorithm
def knapsack(sequence_length, item_list):
    sequence = []
    for s in range(sequence_length + 1):
        sequence.append(SequenceTerm())

    for item in item_list:
        for s in range(sequence_length, item.weight - 1, -1):
            if sequence[s].value < sequence[s - item.weight].value + item.value:
                sequence[s].replace(sequence[s - item.weight], item)

    return sequence


def highest_modulus_in_s_n(m):  # m is the index of limiting primorial
    prime = [[2, 0], [3, 2]]  # each row is [p, weight of p]
    primorial = 6

    # find the mth primorial
    while len(prime) < m:
        prime = add_prime(prime)
        primorial *= prime[-1][0]

    weight_limit = m * (primorial ** (1 / m))
    print("Upper Limit: ", weight_limit)

    # find all primes up to primorial limit
    while prime[-1][0] < primorial:
        prime = add_prime(prime)

    # prep the items for powers of 2 separately because they are weird
    item_list = [Item(0, 2, 2), Item(0, 2, 2), Item(0, 2, 2)]
    weight_power_2 = 4
    while weight_power_2 < weight_limit:
        item_list.append(Item(len(item_list), 2, weight_power_2))
        weight_power_2 *= 2

    # prep the items for each prime
    for p in prime[1:]:
        if p[1] > weight_limit:
            continue
        item_list.append(Item(len(item_list), p[0], p[1]))
        if p[0] > weight_limit:
            continue
        item_list.append(Item(len(item_list), p[0], p[0]))
        weight_power = p[0] * (p[0] - 1)
        while weight_power < weight_limit:
            item_list.append(Item(len(item_list), p[0], weight_power))
            weight_power *= p[0]

    # find terms and print
    sequence = knapsack(int(weight_limit), item_list)
    for s in range(1, len(sequence)):
        print(sequence[s].output_string(s))


highest_modulus_in_s_n(7)
