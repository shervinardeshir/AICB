import os
import numpy as np
import random
import string


def compute_prefix_array(input_string):
	
	if len(input_string)==0:
		return []

	pointer_1 = 0
	pointer_2 = 1
	prefix_array = [0]

	while pointer_2<len(input_string):
		
		if input_string[pointer_1]==input_string[pointer_2]:

			pointer_1 += 1
			pointer_2 += 1
			
			prefix_array.append(pointer_1)

		elif input_string[pointer_1]!=input_string[pointer_2]:

			if pointer_1 == 0:
				prefix_array.append(0)
				pointer_2 += 1

			elif prefix_array[pointer_1 - 1] > 0:

				pointer_1 = prefix_array[pointer_1 - 1] - 1 + 1


			else:

				prefix_array.append(0)
				pointer_2 += 1
				pointer_1 = 0


	return prefix_array





def KMP_search(input_string,input_pattern):

	print 'string: ' + input_string

	print 'pattern: ' + input_pattern

	prefix_array = compute_prefix_array(input_pattern)

	pointer_i = 0
	pointer_j = 0

	matchesSoFar = 0
	count = 0

	while pointer_i < len(input_string) and pointer_j < len(input_pattern):

		print input_string[pointer_i] + ' vs ' + input_pattern[pointer_j]
		print 'i: ' + str(pointer_i)
		print 'j: ' + str(pointer_j)
		print 'prefix: ' + str(prefix_array[pointer_j])

		if input_string[pointer_i] == input_pattern[pointer_j]:

			pointer_i += 1
			pointer_j += 1

			print 'rule 1 '
			print 'matched ' + str(pointer_j) + ' so far'


		elif pointer_j == 0:

			print 'rule 2'

			pointer_i += 1

		elif pointer_j > 0 and pointer_j > prefix_array[pointer_j]:

			print 'rule 3'
			print 'prefix is: ' + str(prefix_array[pointer_j])
			pointer_j = prefix_array[pointer_j]

		else:

			pointer_j = 0
			pointer_i += 1


	return (pointer_j != len(input_pattern)) * (-1) + (pointer_j == len(input_pattern)) * (pointer_i - len(input_pattern)) 


def compute_Z_array(input_string):


	if len(input_string) == 0:

		return []

	z_array = [0]

	pointer_i = 1

	while pointer_i < len(input_string):
		print 'l1'

		pointer_j = 0
		z_array.append(0)

		while (input_string[pointer_i + pointer_j] == input_string[pointer_j]):
			
			z_array[pointer_i] += 1
			pointer_j += 1

		pointer_i += 1
		
		print z_array
		print pointer_i


		while z_array[pointer_i - 1] > 1:
			print 'l2'
			counter = z_array[pointer_i - 1]
			pointer_j = 1
			while pointer_j < counter+1 and len(z_array) < len(input_string):
				print 'l3'
				z_array.append(z_array[pointer_j])
				

				if z_array[pointer_i] > 0:
					print 'l4'

					pointer_k = z_array[pointer_j]
					while (pointer_i + pointer_k < len(input_string)) and (input_string[pointer_i + pointer_k] == input_string[pointer_k]):
						
						z_array[pointer_i] += 1
						pointer_k += 1
						pointer_j = 1
						counter = z_array[pointer_i]


				pointer_i += 1
				
				print z_array
				print pointer_i

	return z_array








def generate_test_case(string_length,pattern_length,number_of_alphabet):

	generated_pattern = ''
	generated_string = ''

	for iString in range(0,string_length):
		generated_string = generated_string + random.choice(string.lowercase[:number_of_alphabet])

	for iPattern in range(0,pattern_length):
		generated_pattern = generated_pattern + random.choice(string.lowercase[:number_of_alphabet])

	return generated_string, generated_pattern