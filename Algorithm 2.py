#Team 6: Aria Askaryar, Shriya Bannikop
"""
Algorithm 2:Finding the Longest String Chain

def longestStringChain(Strings):
    # Create a dictionary to store the chain length for each string
    chain_length = {}
    
    # Sort the list of strings in ascending order by length
    Strings.sort(key=len)
    
    # Initialize variables for the result
    max_chain_length = 0
    result = []
    
    # Iterate through each string
    for s in Strings:
        chain_length[s] = 1  # Initialize the chain length as 1
        for i in range(len(s)):
            new_string = s[:i] + s[i+1:]  # Generate a new string by removing a character
            if new_string in chain_length and chain_length[new_string] + 1 > chain_length[s]:
                chain_length[s] = chain_length[new_string] + 1
        
        # Update the result if a longer chain is found
        if chain_length[s] > max_chain_length:
            max_chain_length = chain_length[s]
            result = [s]
        elif chain_length[s] == max_chain_length:
            result.append(s)
    
    # Reconstruct the result chain by following the longest path
    final_result = []
    for s in result:
        chain = [s]
        current_length = chain_length[s]
        for i in range(len(s), 0, -1):
            for j in range(i):
                new_string = s[:j] + s[j+1:i]
                if new_string in chain_length and chain_length[new_string] == current_length - 1:
                    chain.append(new_string)
                    current_length -= 1
                    s = new_string
                    break
        final_result.extend(chain[::-1])  # Reverse the chain and add to the result
    
    return final_result

# Sample input
Strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
# Call the function and print the result
result = longestStringChain(Strings)
result.reverse()
print(result)

