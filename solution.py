# Returns integer representation of binary gap
def solution(N):
    binary = f'{N:08b}'
   
    return check_gap(binary)

# Checks how many 0's there are from first encountered 1 to next 1 and returns only highest gap
def check_gap(binary):

    
    gap = 0         # Gap between first 1 and the next 1 in a binary num
    final_gap = 0   # The largest found gap 

    # Checks if the number 1 has been found to start incrementing the gap number
    # this way, in the case of '00000101' we should get a gap of only 1
    start_increment = False

    # Loop over binary number 
    for bit in binary:

        if bit == '1' and start_increment == False:
            start_increment = True

        elif bit == '0' and start_increment == True:
            gap += 1

        elif bit == '1':
            if final_gap < gap:
                final_gap = gap
            gap = 0

    # Parse binary to integer to avoid unpredictable errors
    return int(final_gap)

if __name__ == "__main__":
    print("Write an integer to find its binary gap: ")
    N = int(input())
    print('Binary gap: ' + str(solution(N)))