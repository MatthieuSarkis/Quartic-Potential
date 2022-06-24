with open('./archived/output_mathematica/rationalNumerator.py', 'r+') as f:

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

with open('./src/engine/expansion_coefficients/N_20/rational_numerator.py', 'w') as f:

    f.write('import numpy as np\n\ndef rational_numerator(\n\tepsilon: float,\n\talpha: float,\n\tbeta: float,\n\tgamma: float,\n\tdelta: float,\n\tH: float\n) -> float:\n\n')
    f.write(s)
    f.write('\n\n')
    f.write('\treturn ' + num)

with open('./archived/output_mathematica/rationalDenominator.py', 'r+') as f:

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

with open('./src/engine/expansion_coefficients/N_20/rational_denominator.py', 'w') as f:

    f.write('import numpy as np\n\ndef rational_denominator(\n\tepsilon: float,\n\talpha: float,\n\tbeta: float,\n\tgamma: float,\n\tdelta: float,\n\tH: float\n) -> float:\n\n')
    f.write(s)
    f.write('\n\n')
    f.write('\treturn ' + num)