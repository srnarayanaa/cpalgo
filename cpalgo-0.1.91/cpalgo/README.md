# cpalgo
The library documentation will be made public by June 15, 2021.

cpalgo is a Python Library that contains over 100 standard competitive programming algorithms for faster access.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install cpalgo
```

## Usage

```python
import cpalgo

string1 = 'algorithms'
string2 = 'rhythms'

#To find the longest common subsequence between two strings
cpalgo.longest_common_subsequence(string1, string2) 

#To count the number of prime numbers in [1,N]
cpalgo.count_primes(234)

```

## Developers
[Narayanaa S R](https://srnarayanaa.me)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)

## Project Status
This project is expected to be completed by June 2021.

## Documentation for cpalgo

<details>
    <summary>Convex Hull</summary>
 
		import cpalgo

 		points=[(x1, y1),(x2, y2)]
    
		cpalgo.convex_hull(points)
  
</details>

___


<details>
    <summary>Euler Phi</summary>
    
		import cpalgo
    
		n = 234

		cpalgo.euler_phi(n)
    
  
</details>

___


<details>
    <summary>Count Primes Sieves</summary>
    
		import cpalgo

		n = 234
    
		cpalgo.count_primes(n)
    
  
</details>

___

<details>
    <summary>Chinese Remainder Theorem</summary>
    
		import cpalgo

		a = 3; p = 29
    
		cpalgo.chinese_remainder_theorem(a, p)
    
  
</details>

___


<details>
    <summary>Levenshtein Distance</summary>
    
		import cpalgo

		s1 = "INTENTION"
		s2 = "EXECUTION"
    
		cpalgo.edit_distance(s1, s2)
    
  
</details>

___


<details>
    <summary>Caesar Cipher</summary>
    
		import cpalgo

		s = "narayanaa"
		key = 7
    
		cpalgo.caesar_cipher(s, key)
    
  
</details>

___

<details>
    <summary>nCr Modulus</summary>
    
		import cpalgo

		n = 71
		r = 27
    
		cpalgo.nCr_mod(n, r)
    
  
</details>

___

<details>
    <summary>Unique Paths Combinations</summary>
    
		import cpalgo

		N = 21
		M = 19
    
		cpalgo.unique_paths(N, M)
    
  
</details>

___

<details>
    <summary>Two Sum Target</summary>
    
		import cpalgo
    
		arr = [1, 2, 3, 4, 9, 14]
		target = 18

		cpalgo.two_sum(arr, target)
    
  
</details>

___

<details>
    <summary>Three Sum Target</summary>
    
		import cpalgo
    
		arr = [1, 2, 3, 4, 9, 14]
		target = 15

		cpalgo.three_sum(arr, target)
    
  
</details>

___

<details>
    <summary>Longest Common Subsequence</summary>
    
		import cpalgo

		s1 = "ALGORITHMS"
		s2 = "RHYTHMS"

		cpalgo.longest_common_subsequence(s1, s2)
    
  
</details>

___

<details>
    <summary>Longest Increasing Subsequence</summary>
    
		import cpalgo

		nums = [1, 5, 4, 8, 2, 19, 30, 12, 92]
    
		cpalgo.longest_common_subsequence(nums)
    
  
</details>

___

<details>
    <summary>Longest Palindromic Substring</summary>
    
		import cpalgo

		string = "MADHAMAMAM"
    
		cpalgo.longest_palindromic_substring(string)
    
  
</details>

___

<details>
    <summary>Longest Palindromic Subsequence</summary>
    
		import cpalgo

		string = "MADHAMAMAM"
    
		cpalgo.longest_common_subsequence(string)
    
  
</details>

___

<details>
    <summary>Longest Common Prefix</summary>
    
		import cpalgo

		string = "MADHAMAMAM""
    
		cpalgo.longest_common_prefix(string)
    
  
</details>

___

<details>
    <summary>Word Break</summary>
    
		import cpalgo

		string = "applepenapple"
		words = ["apple", "pen"]
    
		cpalgo.word_break(string, words)
    
  
</details>

___

<details>
    <summary>Minimum Window Substring</summary>
    
		import cpalgo

		string = "ADOBECODEBANC"
		t = "ABC"
    
		cpalgo.minimum_window_substring(string, t)
    
  
</details>

___

<details>
    <summary>Maximum Subarray Sum</summary>
    
		import cpalgo

		arr = [1, 3, -2, 4, -6, 9, 2, -1, 3]
    
		cpalgo.maximum_subarray(arr)
    
  
</details>

___

<details>
    <summary>Maximum Product Subarray</summary>
    
		import cpalgo

		arr = [1, 3, -2, 4, -6, 9, 2, -1, 3]
    
		cpalgo.maximum_product_subarray(arr)
    
  
</details>

___

<details>
    <summary>Longest Substring Without Repetition</summary>
    
		import cpalgo

		string = "abcabcbb"
    
		cpalgo.longest_substring_without_repetition(string)
    
  
</details>

___

<details>
    <summary>Kth Largest Element - Heap</summary>
    
		import cpalgo

		arr = [1, 3, -2, 4, -6, 9, 2, -1, 3]
		k = 4
    
		cpalgo.kth_largest_element(arr, k)
    
  
</details>

___


<details>
    <summary>Valid Parantheses</summary>
    
		import cpalgo

		string = "{{}{}{{}}{}"
    
		cpalgo.is_valid_parantheses(string)
    
  
</details>

___

<details>
    <summary>Is Palindrome</summary>
    
		import cpalgo
    
		string = "ANSIUISNA"
		cpalgo.is_palindrom(string)
    
  
</details>

___

<details>
    <summary>Smallest Missing Positive</summary>
    
		import cpalgo
    
    	arr = [6, 3, -1, -9, 1]

		cpalgo.first_missing_positive(arr)
  
</details>

