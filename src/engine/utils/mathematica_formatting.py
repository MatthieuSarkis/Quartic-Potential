with open('./archived/output_mathematica/plusNumerator.py', 'r+') as f:

    s = f.read()
    s = '\tv0 = ' + s[1:-1]

    counter = 0
    counter_variables = 1

    for i in range(len(s)):
        if counter >= 10000 and s[i]=='+':
            s = s[:i] + '\n\tv' + str(counter_variables) + ' = ' + s[i+1:]
            counter = 0
            counter_variables += 1
        counter += 1

num = '(' + ''.join(['v' + str(i) + ' + ' for i in range(counter_variables)])[:-3] + ')'

with open('./archived/output_mathematica/plusDenominator.py', 'r+') as f:

    denom = f.read()
    denom = '(' + denom[1:-1] + ')'

with open('./src/engine/expansion_coefficients/N_15/positive_coefficient.py', 'w') as f:

    f.write('import numpy as np\n\ndef coefPlus(\n\tepsilon: float,\n\tS: float,\n\talpha: float,\n\tbeta: float,\n\tgamma: float,\n\tdelta: float,\n\tH: float\n) -> float:\n\n')
    f.write(s)
    f.write('\n\n')
    f.write('\treturn ' + num + ' / ' + denom)

with open('./archived/output_mathematica/minusNumerator.py', 'r+') as f:

    s = f.read()
    s = '\tv0 = ' + s[1:-1]

    counter = 0
    counter_variables = 1

    for i in range(len(s)):
        if counter >= 10000 and s[i]=='+':
            s = s[:i] + '\n\tv' + str(counter_variables) + ' = ' + s[i+1:]
            counter = 0
            counter_variables += 1

        counter += 1

num = '(' + ''.join(['v' + str(i) + ' + ' for i in range(counter_variables)])[:-3] + ')'

with open('./archived/output_mathematica/minusDenominator.py', 'r+') as f:

    denom = f.read()
    denom = '(' + denom[1:-1] + ')'

with open('./src/engine/expansion_coefficients/N_15/negative_coefficient.py', 'w') as f:

    f.write('import numpy as np\n\ndef coefMinus(\n\tepsilon: float,\n\tS: float,\n\talpha: float,\n\tbeta: float,\n\tgamma: float,\n\tdelta: float,\n\tH: float\n) -> float:\n\n')
    f.write(s)
    f.write('\n\n')
    f.write('\treturn ' + num + ' / ' + denom)