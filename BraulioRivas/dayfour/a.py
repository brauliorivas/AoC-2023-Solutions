def run():
    suma = 0
    
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            line = line[line.index(':')+1:]
            winning, numbers = line.split('|')
            winning = winning[1:len(winning)-1].split(' ')
            numbers = numbers[1:].split(' ')
            common = 0
            
            for number in winning:
                if number in numbers and number != '':
                    common += 1
            
            suma += pow(2, common - 1) if common > 0 else 0 
                    
    print(suma)
            

if __name__ == '__main__':
    run()