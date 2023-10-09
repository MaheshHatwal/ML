def permute(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack
    
    result = []
    backtrack(0)
    return result

# Get user input for the array
input_string = input("Enter a list of unique integers separated by spaces: ")
input_array = list(map(int, input_string.split()))

# Call the permute function with the user's input
permutations = permute(input_array)

# Print the permutations
print("Permutations:", permutations)
