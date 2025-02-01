/*

This program is used for the first half of finding terms for this sequences:
https://oeis.org/A380222

The output has rows of this form, for some prime power p^a:
( p, weight_p^a - weight_p^(a-1) )
where p is the prime
weight_p^a is the minimum number of elements of a permutation group needed to express the multiplicative group mod p^a
This is equal to the sum of the prime powers that divide the totient of p^a

There will be some real number r such that every possible row with such that ln(p^a)/weight_p^a > r is included in the output
*/

use std::{fs::File, u128};
extern crate csv;
use csv::WriterBuilder;
//use std::time;

struct Bound {
    weight: usize,
    cost: f64,
}


fn cost(raw_value: u128, weight: usize) -> f64{
    (raw_value as f64).ln()/(weight as f64)
}

fn primes_below_limit(primes: &mut Vec<bool>,limit: usize) {
    
    //generates a vector of all integers up to limit, true for prime, false for composite
    //this uses the sieve of eratosthenes

    let mut small_primes: Vec<usize> = vec![2,3,5];
    assert_eq!(vec![false,true,false,false,false,true],*primes); //primes should be input with 6 values
    let mut current_len: usize = primes.len(); 
    let mut next_small: usize = 5; 
    
    //process each small prime until the size would exceed limit
    while primes.len()*next_small <= limit {
    
        //add copies of the current values, to multiply the length by next_small
        for _ in 1..next_small{
            for j in 0..current_len{
                primes.push(primes[j]);
            }
        }
        
        //mark multiples of next_small as composites
        for i in (1..current_len).rev() {
            if primes[i]{
                primes[i*next_small] = false;
            }
        }

        println!("Sieve at {}",primes.len());
        
        //find the following small prime
        while !primes[next_small]{
            next_small += 1;
        }
        small_primes.push(next_small);
        current_len = primes.len();
    }
    
    //once highest primorial is reached, fill the rest of the vector
    for _ in 1..next_small{
        for j in 0..current_len{
            if primes.len() == limit{
                break;
            }
            primes.push(primes[j]);
        }
        if primes.len() == limit{
            break;
        }
    }
    
    //finish the sieve, checking up to the square root of the limit
    let max_small = (limit as f64).sqrt() as usize;
    
    while next_small <= max_small{
        
        for i in (1..limit/next_small as usize + 1).rev() {
            if i*next_small == primes.len(){
                continue;
            }
            if primes[i]{
                primes[i*next_small] = false;
            }
        }
        
        while !primes[next_small]{
            next_small += 1;
        }
        small_primes.push(next_small);
    }
    
    //set the low values to be correct
    primes[1] = false;
    for i in small_primes{
        primes[i] = true;
    }
    
    
}


fn primorial_at_index(primorial_index: &usize) -> u128{
    
    let mut primes: Vec<u128> = vec![2];
    let mut test: u128 = 3;
    let mut primorial: u128 = 2;
    let mut current_index: usize = 1;
    while current_index < *primorial_index{
        let mut is_prime: bool = true;
        for p in primes.iter(){
            if test % p == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime{
            primes.push(test);
            primorial *= test;
            current_index += 1;
        }
        test += 2;
    }
    primorial
}

fn is_prime(test_prime: u128, prime_values: &Vec<u128>, primes: &Vec<bool>) -> bool{
    
    let mut check_is_prime: bool = true;
    // if possible, just check primes for true/false
    if (primes.len() as u128) > test_prime{
        check_is_prime = primes[test_prime as usize];

    // if too large, we've got work to do.
    } else {
        
        // check some small primes to quickly rule out composites
        for p in 0..50.min(prime_values.len()){

            if test_prime % prime_values[p] == 0{
                check_is_prime = false;
                break;
            }
        }

        // run a fermat primality test on 2^p-1 to rule out more composites
        if check_is_prime{

            let mut exp_2_2: u128 = 2;
            let mut exp_2_ord: u128 = 1;
            let mut remaining_order: u128 = (test_prime - 1)/2;

            while remaining_order > 0 {
                exp_2_2 = (exp_2_2 * exp_2_2) % test_prime;
                if remaining_order % 2 == 1{
                    remaining_order -= 1;
                    exp_2_ord = (exp_2_ord * exp_2_2) % test_prime; 
                }
                remaining_order /= 2;
            }

            if exp_2_ord != 1{
                check_is_prime = false;
            }
            
        }
        

        // confirm remaining primes by checking for divisibility
        if check_is_prime{
            let p_limit = (test_prime as f64).sqrt() as u128 + 1;
            for p in 50..prime_values.len(){
                if p_limit < prime_values[p]{
                    break;
                }
                if test_prime % prime_values[p] == 0{
                    check_is_prime = false;
                    break;
                }
            }
            
        }

    }
    check_is_prime
}


fn generate_prime_weights(primorial_index: usize,file_path: &str){

    let primorial: u128 = primorial_at_index(&primorial_index);
    let mut primes: Vec<bool> = vec![false,true,false,false,false,true]; // boolean vector of primes, index n = (n is prime)
    let limit: usize = (primorial as f64).sqrt() as usize; // the length that we will extend 'primes' to
    primes_below_limit(&mut primes,limit);

    let mut prime_values: Vec<u128> = vec![2]; 
    for p in 3..primes.len(){
        if primes[p]{
            prime_values.push(p as u128);
        }
    }

    let mut test_index: f64 = primorial_index as f64;
    let mut primorial_log: f64 = (primorial as f64).ln();
    let weight = test_index*(primorial_log as f64/test_index).exp();
    let mut bounds = Bound {
        weight: weight as usize,
        cost: primorial_log/(test_index*(primorial as f64).powf(1.0/test_index))
    };

    // this verifies the assumption that bounds.cost is a true upper bound of item cost. 
    // the stronger bound is good for finding many terms, but is not proved to extend to infinity.
    // the weaker bound is too high, but once valid it extends for all future primorials
    loop{
        primorial_log += (prime_values[test_index as usize] as f64).ln();
        test_index += 1.0;
        // once the weaker bound is valid, we can be certain the cost bound is valid
        if 1.5*(test_index+1.0)*( (test_index+1.0).ln() + 2.0*(test_index+1.0).ln().ln() )/test_index.powi(2) < bounds.cost{
            println!("Confirmed weaker bound at index {}",test_index);
            break;
        }

        // make sure the strong bound applies to this primorial
        if primorial_log/(test_index*(primorial_log as f64/test_index).exp()) > bounds.cost{
            println!("Failed to confirm cost bound at index {}",test_index);
            return;
        }
    }
    
    // create rows for powers of 2 separately since they're a little different, and so we don't perform prime tests on even numbers
    let mut items: Vec<(u128,usize)> = vec![
        (2,2),
        (2,2),
        (2,2)
    ];
    let mut pow_of_2: usize = 4;
    while pow_of_2 <= bounds.weight{
        items.push((2,pow_of_2));
        pow_of_2 *= 2;
    }

    // create rows for other primes p. the weight bound is on sum of prime powers of p-1, 
    // so we construct all possible values k below that bound, and then test if k+1 is prime
    recursive_prime_weights(
        1, 
        0,
        0, 
        &prime_values,
        &primes,
        &mut bounds, 
        &mut items,
    );
    
    // incomplete knapsack needs a sorted list for efficiency, so sort in rust and not python
    items.sort_by( |a: &(u128, usize), b: &(u128, usize)| cost(b.0,b.1 ).partial_cmp(&cost(a.0,a.1 )).unwrap());

    // csv code below thanks to https://gistlib.com/rust/create-a-csv-file-in-rust
    // Create our file object
    let file = File::create(file_path).expect("Unable to create file");

    // Create our CSV writer using the builder
    let mut csv_writer = WriterBuilder::new()
        .delimiter(b',')
        .quote_style(csv::QuoteStyle::NonNumeric)
        .from_writer(file);

    // Write our data to the CSV file
    for item in items{
        csv_writer.write_record(&[item.0.to_string(),item.1.to_string()]).expect("Unable to write record");
    }
    println!("weight bound: {}  cost bound: {} ",bounds.weight,bounds.cost);

}

fn recursive_prime_weights(
    product: u128, 
    weight: usize, 
    p: usize, 
    prime_values: &Vec<u128>,
    primes: &Vec<bool>,
    bounds: &mut Bound, 
    items: &mut Vec<(u128,usize)>,
){

    // if any future primes would exceed the weight bound, process the current value
    if prime_values[p] as usize + weight > bounds.weight{
        let is_it_prime = is_prime(product+1, prime_values, primes);
        if is_it_prime{ // if prime, we want to log this prime
            items.push((product+1,weight)); //the row for p
            if (product+1) as usize <= bounds.weight{
                items.push((product+1,(product+1) as usize)); // the row for p^2
            } 
                
            let mut power_add: usize = (product*(product+1)) as usize;
            while power_add <= bounds.weight{
                items.push((product+1,power_add)); // the row for p^a with a>2
                power_add *= (product+1) as usize;
            }

        }
        return;
    }

    // process without the current if not 2. We do this separately since a 1 cycle is 0 weight so the logic below is a problem
    // but we don't want to skip 2, otherwise we'd be testing if even numbers are prime
    if prime_values[p] > 2{
        recursive_prime_weights(
            product, 
            weight,
            p + 1, 
            prime_values,
            primes,
            bounds, 
            items,
        );
    }

    // process all powers of the current prime that would fit
    let mut p_power: u128 = prime_values[p];
    while p_power as usize + weight <= bounds.weight{
        recursive_prime_weights(
            product*p_power, 
            weight + p_power as usize,
            p + 1, 
            prime_values,
            primes,
            bounds, 
            items,
        );
        p_power *= prime_values[p];
    }

}


fn main(){
    //let now = time::Instant::now();
    generate_prime_weights(14,"A380222_factors.csv");
    //println!("{}",now.elapsed().as_millis());
}

