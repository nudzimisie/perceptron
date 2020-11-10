import activations_and_derivatives as aad
from inputs import Input


class Perceptron:
    def __init__(self, learning_rate=0.1, activation=aad.sigmoid):
        '''
        Podczas tworzenia perceptronu ustawiamy jego współczynnik uczenia oraz funkcję funkcję aktywacji, która domyślnie jest funkcją sigmoid;
        Wagi początkowe są ustawiane jednakowo dla wszystkich wejść;
        '''
        self.weights = []
        self.learning_rate = learning_rate
        self.activation = activation
        self.weighted_sum = []

    def init_weights(self, number_inputs):
        init_weight = 1/number_inputs
        self.weights = [init_weight for i in range(number_inputs)]

    @property
    def weighted_sum(self):
        # wartość sumy ważonej
        return self._weighted_sum

    @weighted_sum.setter
    def weighted_sum(self, inputs):
        # funkcja obliczająca sumę ważoną
        self._weighted_sum = sum([data * self.weights[i] for i, data in enumerate(inputs)])

    def run(self, *inputs):
        '''
        Funkcja run jest skrótem funkcji xrun;
        Ma zastosowanie do wszystkich funkcji aktywacji, które nie potrzebują dodatkowych argumentów;
        '''
        return self.xrun([], *inputs)

    def _input_correction(self, inputs):
        return [data.value for data in inputs]

    def _run(self, inputs):
        '''
        Ukryta funkcja run inicjuje wagi oraz wylicza sumę ważoną
        '''
        self._inputs = self._input_correction(inputs)
        if not self.weights:
            self.init_weights(len(self._inputs))
        self.weighted_sum = self._inputs

    def xrun(self, activation_args:list, *inputs):
        '''
        Funkcja przyjmuje dodatkowe argumenty dla funkcji aktywacji oraz sygnały wejściowe;
        Jeśli nie ma konieczności podawania dodatkowych argumentów należy użyć funkcji skróconej run;
        Sygnały na wejściu powinny być obiektami klasy Input, która zwraca parametr liczbowy value;
        Funkcja zwraca wynk działania perceptronu;
        '''
        self._run(inputs)
        return self.activation()(self.weighted_sum, *activation_args)

    @property
    def _fn_error(self):
        # zwraca funkcję błędu
        return lambda x, expected: x - expected

    @property
    def _sqr_error(self):
        # zwraca funkcję liczącą średni błąd kwadratowy
        return lambda x, expected: pow(self._fn_error(x, expected), 2) / 2

    def error(self, expected):
        # zwraca wartość błędu
        return self._fn_error(self.weighted_sum, expected)

    def sqr_error(self, expected):
        # zwraca średni błąd kwadratowy
        return self._sqr_error(self.weighted_sum, expected)

    @property
    def activation_deriv(self):
        # zwraca wartość pochodnej funkcji aktywacji w punkcie u (suma ważona)
        return self._activation_deriv

    @activation_deriv.setter
    def activation_deriv(self, args):
        self._activation_deriv = aad.derivative(self.activation, *args)(self.weighted_sum)

    @property
    def error_fn_deriv(self):
        # zwraca funkcję obliczajacą pochodną funkcji błędu dla poszczególnych wejść
        return self._error_fn_deriv

    @error_fn_deriv.setter
    def error_fn_deriv(self, expected):
        self._error_fn_deriv = lambda x: self.error(expected) * self.activation_deriv * x

    def update_weights(self, inputs):
        # funkcja korygująca wagi
        new_weights = []
        for i, weight in enumerate(self.weights):
            weight = weight - self.learning_rate * self.error_fn_deriv(inputs[i])
            new_weights.append(weight)
        self.weights = new_weights

    def train(self, expected, *inputs):
        '''
        Funkcja train jest skrótem funkcji xtrain;
        Ma zastosowanie do wszystkich funkcji aktywacji, które nie potrzebują dodatkowych argumentów;
        '''
        return self.xtrain([], expected, *inputs)        

    def xtrain(self, activation_args:list, expected, *inputs):
        '''
        Funkcja przyjmuje dodatkowe argumenty dla funkcji aktywacji oraz sygnały wejściowe;
        Jeśli nie ma konieczności podawania dodatkowych argumentów należy użyć funkcji skróconej train;
        Sygnały na wejściu powinny być obiektami klasy Input, która zwraca parametr liczbowy value;
        Funkcja uczy perceptron;
        '''
        self._run(inputs)
        print(f'Błąd przed korekcją: {self.sqr_error(expected)}')
        self.activation_deriv = activation_args
        self.error_fn_deriv = expected
        self.update_weights(self._inputs)
        # kontrolnie
        self._run(inputs)
        print(f'Błąd po korekcji: {self.sqr_error(expected)}')

BIAS = Input(1)