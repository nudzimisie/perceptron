from perceptron import Perceptron, BIAS
from inputs import Input
from random import randint

perceptron = Perceptron()

train_datas = [Input(2*i+2 + randint(-10, 10) / 100) for i in range(10)]

expected = 1.0

EPOCHS = 1
for epoch in range(EPOCHS):
    for train_data in train_datas:
        print(f'wynik: {perceptron.run(train_data, BIAS)}')
        perceptron.train(expected, train_data, BIAS)