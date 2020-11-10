from inputs_generator import CaseFiles, guilty_scenarios, guiltlessness_scenarios
from random import choice

NUMBER_TRAIN_DATAS = 30

NUMBER_TEST_DATAS = 50

train_data = []
test_data = []

for i in range(NUMBER_TRAIN_DATAS):
    guilty = choice([True, False])
    if guilty:
        scenarios = guilty_scenarios
    else:
        scenarios = guiltlessness_scenarios
    train_data.append(CaseFiles(scenarios, guilty))

for i in range(NUMBER_TEST_DATAS):
    guilty = choice([True, False])
    if guilty:
        scenarios = guilty_scenarios
    else:
        scenarios = guiltlessness_scenarios
    test_data.append(CaseFiles(scenarios, guilty))

