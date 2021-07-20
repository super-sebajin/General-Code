#Here is a short list of algorithims written for my undergraduate research project as a participant in the NSF-funded Puerto Rico Louis Stokes Alliance
#For Minority Participation. This code is actually written in a jupyter notebook, however I am currently using a 2021 Mac Mini with a M1 ARM CPU, SageMath has
#no support for this chipset as of the dat of creation of this file 2021-07-19. These algorithms have been tested to work in the CoCalc environment.

#The research was to Rank Metric Codes using a combinatorial construction. We specifically wanted to construct codes with an already prescribed rank distance. The
#first combinatorial object researched on was the De Bruijn Sequence in binary. 

#May these funcitons be of use to any who wishes to use them.

#Algorithm-1 to convert vector of a perfect square length in to a square matrix
def vector_to_matrix(in_vector):
    """ Returns a matrix that based on the mapping GF(2)^(n^2) -> M^(nxn)_GF(2) """
    return(matrix(GF(2),[in_vector[i:i + sqrt(len(in_vector))] for i in range(0, len(in_vector), sqrt(len(in_vector)))]))

#Algorithm-2 that will produce a list of "de bruijn" sequences so that they may be analyzed
from sage.combinat.debruijn_sequence import is_debruijn_sequence as is_dbs

def unconfirmed_debruijn_sequences(alphabet, substring_length):
    length_of_sequence = alphabet**substring_length
    general_vector_space = VectorSpace(GF(alphabet), length_of_sequence).list()
    #confirmed_vectors = []
    as_sequences =[]
    for vector in general_vector_space:
        if is_dbs(list(vector), alphabet, substring_length):
            as_sequences.append(list(vector))
    return(as_sequences)

#Algorithm-3 for rank distance of two square matrices
def rank_distance(matA, matB):
    """returns an integer denoting the rank distance between a matrix A and a matrix B"""
    return((matA - matB).rank())

#Algorithm-4 test for orhtogonality between two matrices
def orthogonal_matrices(matA, matB):
    """Returns a boolean value, True for othogoality and False otherwise"""
    return(matA*matB.transpose() == 0)

#Algorithm-5 generate and return a list of linearlly independent vectors
def generate_independent_vectors(characteristic, vector_dimension, subspace_dimension):
    assert vector_dimension.is_square(), "The dimension (length of the vector) must be a square"
    base_field = GF(characteristic)#the base field for the parent vector space
    vector_space = base_field^vector_dimension #Parent vector space
    pseudo_db_vector = vector(base_field, PseudoBinaryDeBruijnSequencesI(sqrt(vector_dimension)).base_de_bruijn_sequence())#Vector representation of the de bruijn sequence

    while true:
        test_vectors = [vector(base_field, {el: base_field.random_element() for el in range(vector_dimension)})
                       for i in range(subspace_dimension - 1)]
        test_vectors.append(pseudo_db_vector)
        test_vectors = list(filter(None.__ne__, test_vectors))# for some reason the list test_vectors was throwing in a NoneType
        linearity_check = vector_space.linear_dependence(test_vectors)
        if linearity_check == []:
            return(test_vectors)
        else:
            test_vectors.clear
