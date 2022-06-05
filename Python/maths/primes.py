def multiples(num, n_mult):
    i = 1
    while i <= n_mult:
        yield num * i
        i += 1


primes = [2, 3]


def get_primes(trial_primes):
    copy_trial_primes = trial_primes[:]
    for trial in copy_trial_primes:
        # remove even numbers greater than 2
        if trial > 2 and trial % 2 == 0:
            trial_primes.remove(trial)

        # remove non-positive numbers and number 1
        elif trial == 1 or trial < 1:
            trial_primes.remove(trial)

        # remove multiples of 2 and 3 from list.
        #elif trial in multiples(2, 1000) or trial in multiples(3, 1000):
          #  trial_primes.remove(trial)

        # checks if number is divisible by 2 > trial_num
        # prime should only be dividable by 1 and itself.
        else:
            for div_candidate in range(2, trial):
                if trial % div_candidate == 0:
                    trial_primes.remove(trial)
                    break

    return trial_primes


print(get_primes(list(range(1, 100))))
