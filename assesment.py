class StringCalculator:

    def add(self, input_str):
        if len(input_str) == 0:
            return 0

        listOfNumbers = input_str.split(',')
        sumOfNumbers = 0
        for number in listOfNumbers:
            sum_of_numbers += int(number)

        return sumOfNumbers