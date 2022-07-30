import yarn
import random

ammount = int(input('Enter number of sentences >> '))
sentences = ['']
for i in range(ammount):
    print(f"ITERATION {i + 1}")

    print("FUSED SENTENCES")
    for i in range(3):
        print(yarn.fusesent(yarn.genesent(random.randint(1,6)),yarn.genesent(random.randint(1,6))))

    print('SIMPLE SENTENCES')
    for i in range(3):
        print(yarn.genesent(random.randint(1, 6)))

    print('PARAGRAPH')
    for i in range(3):
        sentences.append(yarn.genesent(random.randint(1,6)))
        sentences.append(yarn.fusesent((yarn.genesent(random.randint(1,6))),yarn.genesent(random.randint(1,6))))
    print(yarn.writeparagraph((sentences)))