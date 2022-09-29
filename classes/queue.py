from stack import Pilha


def main():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q)

    q.dequeue()
    print(q)


class Queue:
    def __init__(self):
        self.input = Pilha()
        self.output = Pilha()

    def enqueue(self, item):
        self.input.empilhe(item)

    def dequeue(self):
        while not (self.input.vazia()):
            el = self.input.desempilhe()
            self.output.empilhe(el)

        return_el = self.output.desempilhe()

        while not (self.output.vazia()):
            el = self.output.desempilhe()
            self.input.empilhe(el)

        return return_el

    def __str__(self):
        return f'{self.input.dados}'


main()
