'''
Complete the calc_average() function that has an integer list parameter 
and returns the average value of the elements in the list as a float.
'''

def calc_average(nums):
    average = float(sum(nums) / len(nums))
    return average
    
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(calc_average(nums))   # calc_average() should return 3.0