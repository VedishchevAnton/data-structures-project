from src.stack import Node, Stack

if __name__ == '__main__':
    stack = Stack()
    stack.push('data1')
    data = stack.pop()
    print(data)

    # стэк стал пустой
    assert stack.top is None
    print(stack.top)

    # pop() удаляет элемент и возвращает данные удаленного элемента
    assert data == 'data1'
    print(data)

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()
    print(data)

    # теперь последний элемента содержит данные data1
    assert stack.top.data == 'data1'
    print(stack.top.data)

    # данные удаленного элемента
    assert data == 'data2'
    print(data)

