with open('./src/engine/expansion_coefficients/N_20/numerator/rationalNumerator_coefficients.py', 'w') as f:

    f.write('import numpy as np\n\n')


for j in range(20):

    with open('./archived/output_mathematica_coefficients/numerator/rationalNumerator_coefficients_{}.py'.format(j), 'r+') as f:

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

    with open('./src/engine/expansion_coefficients/N_20/numerator/rationalNumerator_coefficients.py', 'a') as f:

        f.write('def num_coef_degree_{}(\n\talpha: float,\n\tbeta: float,\n\tgamma: float,\n\tdelta: float,\n\tH: float\n) -> float:\n\n'.format(j))
        f.write(s)
        f.write('\n\n')
        f.write('\tcoef = ')
        f.write(num)
        f.write('\n\n')
        f.write('\treturn coef')
        f.write('\n\n')


with open('./src/engine/expansion_coefficients/N_20/denominator/rationalDenominator_coefficients.py', 'w') as f:

    f.write('import numpy as np\n\n')


for j in range(10):

    with open('./archived/output_mathematica_coefficients/denominator/rationalDenominator_coefficients_{}.py'.format(j), 'r+') as f:

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

    with open('./src/engine/expansion_coefficients/N_20/denominator/rationalDenominator_coefficients.py', 'a') as f:

        f.write('def den_coef_degree_{}(\n\talpha: float,\n\tbeta: float,\n\tgamma: float,\n\tdelta: float,\n\tH: float\n) -> float:\n\n'.format(j))
        f.write(s)
        f.write('\n\n')
        f.write('\tcoef = ')
        f.write(num)
        f.write('\n\n')
        f.write('\treturn coef')
        f.write('\n\n')
