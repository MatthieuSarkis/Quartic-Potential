for i in range(20):

    with open('./archived/output_mathematica_coefficients/numerator/rationalNumerator_coefficients_{}.py'.format(i), 'r+') as f:

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

    coef = '(' + ''.join(['v' + str(i) + ' + ' for i in range(counter_variables)])[:-3] + ')'

    with open('./src/engine/expansion_coefficients/N_20/rationalNumerator_coefficients_{}.py'.format(i), 'w') as f:

        f.write('import numpy as np\n\ndef rational_numerator_coefficients_{}(\n\tepsilon: float,\n\talpha: float,\n\tbeta: float,\n\tgamma: float,\n\tdelta: float,\n\tH: float\n) -> float:\n\n'.format(i))
        f.write('\treturn ')