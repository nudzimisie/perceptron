from perceptron import Perceptron, BIAS
from inputs import Input

perceptron = Perceptron()

train_datas = [Input(0.3),]

expected = 1.0

EPOCHS = 1
for epoch in range(EPOCHS):
    for train_data in train_datas:
        print(f'wynik: {perceptron.run(train_data, BIAS)}')
        perceptron.train(expected, train_data, BIAS)