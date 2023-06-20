def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

input_array = [[1,3,4],[5,2,6]]
result = flatten_and_sort(input_array)
print(result)

# How does this solution ensure data immutability?
  #this solution ensures data immutability by appending and returning what is in the array
# Is this solution a pure function? Why or why not?
  #pure function because it does not change value
# Is this solution a higher order function? Why or why not?
  #higher order function because it goes in ascending order
# Would it have been easier to solve this problem using a different programming style?
  #im not sure
# Why in particular is functional programming a helpful paradigm when solving this problem?
  #because it ensures immutability
