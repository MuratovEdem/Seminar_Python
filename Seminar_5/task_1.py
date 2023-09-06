# Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
import operator


def get_answer_equation(equ):
    list_members = equ.split()
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    count = 0
    while count < len(list_members):
        if el == '*' or el == '/':
            list_members[i-1] = opers[el](int(list_members[i-1]), int(list_members[i+1]))
            list_members.pop(i+1)
            list_members.pop(i)
            print(list_members)
            count -= 1
        elif '/' in list_members:
            i = list_members.index('/')
            list_members[i-1] = int(list_members[i-1]) / int(list_members[i+1])
            list_members.pop(i+1)
            list_members.pop(i)
            count -= 1
        elif '+' in list_members:
            i = list_members.index('+')
            list_members[i-1] = int(list_members[i-1]) + int(list_members[i+1])
            list_members.pop(i+1)
            list_members.pop(i)
            count -= 1
        elif '-' in list_members:
            i = list_members.index('-')
            list_members[i-1] = int(list_members[i-1]) - int(list_members[i+1])
            list_members.pop(i+1)
            list_members.pop(i)
            count -= 1
        count += 1
    return list_members




equation = '2 + 2 * 14'

print(get_answer_equation(equation))






































# import operator
# from pythonds.basic.stack import Stack
# from pythonds.trees.binaryTree import BinaryTree

# def buildParseTree(fpexp):
#     fplist = fpexp.split()
#     pStack = Stack()
#     eTree = BinaryTree('')
#     pStack.push(eTree)
#     currentTree = eTree
#     for i in fplist:
#         if i == '(':
#             currentTree.insertLeft('')
#             pStack.push(currentTree)
#             currentTree = currentTree.getLeftChild()
#         elif i not in ['+', '-', '*', '/', ')']:
#             currentTree.setRootVal(int(i))
#             parent = pStack.pop()
#             currentTree = parent
#         elif i in ['+', '-', '*', '/']:
#             currentTree.setRootVal(i)
#             currentTree.insertRight('')
#             pStack.push(currentTree)
#             currentTree = currentTree.getRightChild()
#         elif i == ')':
#             currentTree = pStack.pop()
#         else:
#             raise ValueError
#     return eTree

# def evaluate(parseTree):
#     opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

#     leftC = parseTree.getLeftChild()
#     rightC = parseTree.getRightChild()

#     if leftC and rightC:
#         fn = opers[parseTree.getRootVal()]
#         return fn(evaluate(leftC),evaluate(rightC))
#     else:
#         return parseTree.getRootVal()


# pt = buildParseTree("( 3 + ( 4 * 5 )")


# print(evaluate(pt))

