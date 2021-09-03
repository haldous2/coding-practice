"""
Givenan arithmetic equation 
  consisting of positive integers and + - * /
  compute the result.

Input:  2 * 3 + 5 / 6 * 3 + 15
        (2 * 3) + ((5 / 6) * 3) + 15
Output: 23.5

Method: remember pemdas. 
Hardest part will be how to handle parsing string 
"""

def getoperand(expression, index):
    """
    Get number, including negative numbers
    """
    nbr = ""
    digits = "0123456789"
    if index < len(expression):
        for c in expression[index:]:
            if nbr:
                if c in digits:
                    nbr += c
                else:
                    index += len(nbr)
                    return nbr
            else:
                if c in "+-" or c in digits:
                    nbr = c
    if nbr:
        return nbr
    return None

def getoperator(expression, index):
    """
    Get operators, including +, *, /
    """
    opr = ""
    if index < len(expression) and expression[index] in "+-*/":
        opr = expression[index]
        return opr
    else:
        return None

def expressiontoinfix(expression):
    index = 0
    infix = []
    while True:
        operand = getoperand(expression, index)
        if operand is not None:
            index += len(operand)
            infix.append(float(operand))
        operator = getoperator(expression, index)
        if operator is not None:
            index += 1
            infix.append(operator)
        else:
            break
    return infix

## --------------------------------------------------------------------------------
def calculateV1(infix):
    """
    My first hacky version - brute force ish?
    Stores equation as infix list
    There are no negatives, it's only plus negative value
    1. Read through list and multiply and divide everything
       Store values in place e.g. 3,*,4 -> 0,+,12 etc.
    2. Read through again and do addition and store to result to return
    """
    
    # First pass - multiply and divide
    def multiply_divide(infix):
        """
        Multiply and divide numbers. 
        Store result in front, zero out back number
        """
        i = 0
        while i < len(infix) - 2:
            operanda = infix[i]
            operator = infix[i + 1]
            operandb = infix[i + 2]
            if operator == "*":
                infix[i] = 0
                infix[i + 1] = "+"
                infix[i + 2] = operanda * operandb
            if operator == "/":
                if operandb > 0:
                    infix[i] = 0
                    infix[i + 1] = "+"
                    infix[i + 2] = operanda / operandb
                else:
                    return None
            i += 2
        return infix

    # Second pass - addition
    def addition(infix):
        """
        Add all remaining values.
        Note: not subtracting values here, because parser set
              numbers as negative in building infix
        """
        i = 0
        result = 0
        for i in range(0, len(infix), 2):
            operand = infix[i]
            result += operand
        return result

    ## INIT calling method for V1
    if multiply_divide(infix) is not None:
        print "result:", addition(infix)
    else:
        return None

print "==== V1 ====="
calculateV1(expressiontoinfix("2*3+5/6*3+15"))
# calculateV1(expressiontoinfix("2*3-5/6*3+15"))
# calculateV1(expressiontoinfix("1+2+3"))
# calculateV1(expressiontoinfix("-1-2-3"))
# calculateV1(expressiontoinfix("2*2*2"))
# calculateV1(expressiontoinfix("-2*2*2"))
# calculateV1(expressiontoinfix("-2*-2*2"))
# calculateV1(expressiontoinfix("-2*-2*-2"))
# calculateV1(expressiontoinfix("1"))
# calculateV1(expressiontoinfix("-1"))
# calculateV1(expressiontoinfix("2--1"))
# calculateV1(expressiontoinfix("1+-1"))

## --------------------------------------------------------------------------------
def calculateV2(infix):
    """
    Book(ish) version. The cracking the coding interview solution
    seems overly complicated - so, this version loosely follows
    what the book offers.
    """
    def run_operations(nds, ops, future_op = None):
        """
        Run and apply operations to operands
        return will be applied to nds, ops by reference
        """
        while ops:
            # Check precedence
            if future_op is not None:
                if future_op in "*/":
                    # future operation has high precedence
                    if ops[-1] in "+-":
                        # current operation has lower precedence
                        break
            if len(nds) >= 2:
                res = 0
                ndb = nds.pop()
                nda = nds.pop()
                op = ops.pop()
                if op == "*":
                    res = nda * ndb
                elif op == "/":
                    # Division by zero error could occur
                    # try block should catch
                    res = nda / ndb
                elif op == "+":
                    res = nda + ndb
                else:
                    res = nda - ndb
                nds.append(res)
            else:
                # not enough nds (operands)
                break

    def getresult(infix):
        """
        Process infix and return result
        Input: infix parts list -> [2,+,3,*,4] etc.
        """
        nds = deque()
        ops = deque()

        for i in range(len(infix)):

            # Let's do some stacking
            future_op = None
            if type(infix[i]) is str:
                # stack operator
                ops.append(infix[i])
            else:
                # stack operand
                nds.append(infix[i])
                if (i + 1) < len(infix):
                    future_op = infix[(i + 1)]

            # Let's do some processing
            if future_op is not None:
                run_operations(nds, ops, future_op)

        # process the last final remaining bits
        run_operations(nds, ops, None)

        if len(nds) == 1:
            return nds[0]
        else:
            return None

    ## INIT calling method for V2
    try:
        print "result:", getresult(infix)
    except ZeroDivisionError:
        print "Division by zero error"

print "==== V2 ====="
calculateV2(expressiontoinfix("2*3+5/6*3+15"))
# calculateV2(expressiontoinfix("2*3-5/6*3+15"))
# calculateV2(expressiontoinfix("1+2+3"))
# calculateV2(expressiontoinfix("-1-2-3"))
# calculateV2(expressiontoinfix("2*2*2"))
# calculateV2(expressiontoinfix("-2*2*2"))
# calculateV2(expressiontoinfix("-2*-2*2"))
# calculateV2(expressiontoinfix("-2*-2*-2"))
# calculateV2(expressiontoinfix("1"))
# calculateV2(expressiontoinfix("-1"))
# calculateV2(expressiontoinfix("2--1"))
# calculateV2(expressiontoinfix("1+-1"))

## --------------------------------------------------------------------------------
def calculateV3(infix):
    """
    Convert infix to postfix
    Process postfix to value

    Note: This seems the most logical way to do this problem, long winded though
    """
    def infixtopostfix(infix):
        """
        Convert infix into postfix
        if operand -> add to postfix
        if operator
        dump stack into prefix while operator <= stack precedence
            precedence +- < */
        add operator to prefix
        """
        postfix = []
        stack = deque()
        precedence = {"*":2, "/":2, "+":1, "-":1}
        for i in range(len(infix)):
            if type(infix[i]) == str and infix[i] in "+-*/":
                # operator
                while stack:
                    peek = stack[-1]
                    # precedence
                    # current operator <= pending operator
                    if precedence[infix[i]] <= precedence[peek]:
                        postfix.append(stack.pop())
                    else:
                        break
                # add current operator to stack
                stack.append(infix[i])
            else:
                # operand
                postfix.append(infix[i])
        # unload remaining pending operators
        while stack:
            postfix.append(stack.pop())
        return postfix

    def postfixvalue(postfix):
        """
        Process postfix into value
        Two stacks will track operands and operators
        If an operator is in the stack, and if two operands are available,
        perform operation on top two operands
        Otherwise, fill stacks as they are seen in postfix
        """
        operands = deque()
        operators = deque()
        for elem in postfix:                    
            if type(elem) is str and elem in "*/+-":
                operators.append(elem)
                if len(operands) >= 2:
                    operandb = operands.pop()       # order b, a
                    operanda = operands.pop()
                    operator = operators.pop()
                    # print operanda, type(operanda)
                    # print operandb, type(operandb)
                    # print operator
                    if operator == "*":
                        # print "   op:", operanda, "*", operandb
                        operands.append(operanda * operandb)
                    elif operator == "/":
                        # print "   op:", operanda, "/", operandb
                        operands.append(operanda / operandb)
                    elif operator == "+":
                        # print "   op:", operanda, "+", operandb
                        operands.append(operanda + operandb)
                    else:
                        # print "   op:", operanda, "-", operandb
                        operands.append(operanda - operandb)
            else:
                operands.append(elem)
        return operands[0]

    ## INIT calling method for V3
    try:
        print "result:", postfixvalue(infixtopostfix(infix))
    except ZeroDivisionError:
        print "Division by zero error"

print "==== V3 ====="
calculateV3(expressiontoinfix("2*3+5/6*3+15"))
# calculateV3(expressiontoinfix("2*3-5/6*3+15"))
# calculateV3(expressiontoinfix("1+2+3"))
# calculateV3(expressiontoinfix("-1-2-3"))
# calculateV3(expressiontoinfix("2*2*2"))
# calculateV3(expressiontoinfix("-2*2*2"))
# calculateV3(expressiontoinfix("-2*-2*2"))
# calculateV3(expressiontoinfix("-2*-2*-2"))
# calculateV3(expressiontoinfix("1"))
# calculateV3(expressiontoinfix("-1"))
# calculateV3(expressiontoinfix("2--1"))
# calculateV3(expressiontoinfix("1+-1"))
