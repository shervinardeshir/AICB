import kmp_lib
import numpy as np


#print kmp_lib.compute_prefix_array('acacabacacabacacac')

input_string, input_pattern = kmp_lib.generate_test_case(300,3,5)
#input_string = 'abcdeaaa'
#input_pattern = 'aaa'
index = kmp_lib.KMP_search(input_string,input_pattern)

print input_string
print input_pattern

if index > -1:

	print input_pattern + ' found here: ' + input_string[index:] 

else:

	print 'not found'


print kmp_lib.compute_Z_array('aabcaabxaaaz')