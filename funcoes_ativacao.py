import numpy as np

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))

def tahnFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

def reluFunction(soma):
    if soma >= 0:
        return soma
    return 0

def linearFunction(soma):
    return soma

def softmaxFunction(x):
    ex = np.exp(x)
    return ex / ex.sum()

teste1  = stepFunction(-1)
teste2  = sigmoidFunction(-0.358)
teste3  = tahnFunction(-0.358)
teste4  = reluFunction(0.358)
teste5  = linearFunction(-0.358)
teste6  = [7.0, 2.0, 1.3]

print(softmaxFunction(teste1))
print(softmaxFunction(teste2))
print(softmaxFunction(teste3))
print(softmaxFunction(teste4))
print(softmaxFunction(teste5))
print(softmaxFunction(teste6))