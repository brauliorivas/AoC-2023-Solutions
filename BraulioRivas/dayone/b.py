def strToInt(string):
    if string.isnumeric():
        return int(string)
    
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return numbers.index(string) + 1
    

def run():
    sum = 0
    
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    with open('b.txt') as f:
        for line in f:
            num = 0
            
            minIndex = len(line)
            minToken = ''
            for token in numbers:
                if token in line:
                    index = line.index(token)
                    if index < minIndex:
                        minIndex = index
                        minToken = token
                        
            num += 10 * strToInt(minToken)
            
            maxIndex = -1
            maxToken = ''
            for token in numbers:
                index = line.rfind(token)
                if index > maxIndex:
                    maxIndex = index
                    maxToken = token

            num += strToInt(maxToken)
            
            sum += num          
                
    print(sum)

if __name__ == '__main__':
    run()