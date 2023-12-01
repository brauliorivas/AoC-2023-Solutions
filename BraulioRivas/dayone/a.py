def run():
    sum = 0
    nums = '1234567890'
    
    with open('a.txt') as f:
        for line in f:
            a = ''
            b = ''
            for c in line:
                if c in nums:
                    a = c
                    break
            for c in line[::-1]:
                if c in nums:
                    b = c
                    break 
                    
            sum += int(f'{a}{b}')           
            
    print(sum)

if __name__ == '__main__':
    run()