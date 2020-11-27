import numpy as np

def the_type(the_input):
    if isinstance(the_input, int) or isinstance(the_input, float):
        return 'Integer'
    new_input = np.array(the_input)
    isVector = False
    try:
        new_input.shape[1]
    except:
        isVector = True
    if isVector:
        return 'Vector'
    return 'Matrix'

class LinearAlgebra:
    def __init__(self, the_inputs=None):
        self.the_inputs = {}

    def matrix(self, the_matrix):
        if the_type(the_matrix) != 'Matrix':
            raise TypeError("This is not a matrix. Please specify correctly.")
        return the_matrix

    def vector(self, the_vector):
        if the_type(the_vector) != 'Vector':
            raise TypeError("This is not a vector. Please specify correctly.")
        return the_vector

    def multiply(self, input_one, input_two):
        types = [the_type(input_one), the_type(input_two)]
        
        if types[0] == 'Vector' and types[1] == 'Vector':
            if len(input_one) != len(input_two):
                raise ValueError("The dimensions of the two vectors specified are not the same")
            new_vector = []
            for i in range(len(input_one)):
                new_vector.append(input_one[i]*input_two[i])
            return new_vector
        
        elif types[0] == 'Matrix' and types[1] == 'Matrix':
            original_shape = np.array(input_one).shape
            if str(np.array(input_one).shape) != str(np.array(input_two).shape):
                raise ValueError("The dimensions of the two matrix specified are not the same")
            input_one = np.ravel(input_one)
            input_two = np.ravel(input_two)
            new_matrix = []
            for i in range(len(input_one)):
                new_matrix.append(input_one[i]*input_two[i])
            return np.array(new_matrix).reshape(original_shape[0], original_shape[1])

        elif 'Vector' in types and 'Integer' in types:
            the_vector = []
            the_int = 0
            if types[0] == 'Vector':
                the_vector = input_one
                the_int = input_two
            else:
                the_vector = input_two
                the_int = input_one
            new_vector = []
            for num in the_vector:
                new_vector.append(num*the_int)
            return new_vector

        elif 'Matrix' in types and 'Integer' in types:
            the_matrix = []
            the_int = 0
            if types[0] == 'Matrix':
                the_matrix = input_one
                the_int = input_two
            else:
                the_matrix = input_two
                the_int = input_one
            original_shape = np.array(the_matrix).shape
            the_matrix = np.ravel(the_matrix)
            new_matrix = []
            for num in the_matrix:
                new_matrix.append(num*the_int)
            return np.array(new_matrix).reshape(original_shape[0], original_shape[1])

        elif 'Vector' in types and 'Matrix' in types:
            the_matrix = []
            the_vector = []
            if types[0] == 'Matrix':
                the_matrix = input_one
                the_vector = input_two
            else:
                the_matrix = input_two
                the_vector = input_one
            original_shape = np.array(the_matrix).shape
            new_matrix = []
            the_matrix = np.ravel(the_matrix)
            counter_vect = 0
            for i in range(len(the_matrix)):
                new_matrix.append(the_matrix[i]*the_vector[counter_vect])
                counter_vect += 1
                if counter_vect == len(the_vector):
                    counter_vect = 0
            return np.array(new_matrix).reshape(original_shape[0], original_shape[1])
        
            

    def print_info(self, the_input):
        print("Dim: %s" % str(np.array(the_input).shape))
        print("Type: %s" % the_type(the_input))
        if the_type(the_input) == 'Vector':
            print("R: R%s" % np.array(the_input).shape[0])
        else:
            print("R: R({} * {})".format(np.array(the_input).shape[0], np.array(the_input).shape[1]))

la = LinearAlgebra()
the_matrix = la.matrix([[1,2,3,4],[5,6,7,8],[5,6,7,8]])
the_vector = la.vector([0,0,0,0])
print(la.multiply(the_matrix, the_vector))
