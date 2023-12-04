def run():
    matchings = []
    
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            line = line[line.index(':')+1:]
            winning, numbers = line.split('|')
            winning = winning[1:len(winning)-1].split(' ')
            numbers = numbers[1:].split(' ')
            
            matching = 0
            
            for number in winning:
                if number in numbers and number != '':
                    matching += 1
            
            matchings.append(matching)
             
    times_repeated = [1] * len(matchings)
    
    for i in range(len(matchings)):
        for j in range(matchings[i]):
            times_repeated[i+j+1] += times_repeated[i]
            
    print(sum(times_repeated))

if __name__ == '__main__':
    run()