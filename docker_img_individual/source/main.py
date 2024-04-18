import numpy as np
from tqdm import tqdm

num_sum = 0
number_of_randoms = 1e6
for _ in tqdm(range(number_of_randoms)):
    num_sum += np.random.randint(10, 1000)
print(num_sum / number_of_randoms)

