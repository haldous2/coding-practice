 def parse_expression(expression, nbrs):
      """
      Parse string to list, separate operands from operators
      Note: keep track of negative values, only addition will result
            e.g. (2 - 5) -> (2 + -5)

      This is my hacky first instinct version - which works, 
         but may be difficult to follow
      """
      nbr = ""
      # First pass - parse to list[number, operator, number, operator, etc..]
      for c in expression:
          if c in "+*/":
              # Negatives will be attached to nbr
              # e.g., 2+-5 -> [2,+,-5]; 2-5 -> [2+-5] etc.
              nbrs.append(float(nbr))
              nbrs.append(c)
              nbr = ""
          else:
              if c == "-" and nbr:
                  # Negative already defined
                  # append nbr, start new negative nbr
                  if nbr == "-":
                      # fix for 1--1
                      nbr = 0
                  nbrs.append(float(nbr))
                  nbrs.append("+")
                  nbr = "-"
              else:
                  # Continue building nbr
                  nbr += c
      nbrs.append(float(nbr))

  # Second pass - multiply and divide
  def multiply_divide(nbrs):
      """
      Multiply and divide numbers. 
      Store result in front, zero out back number
      """
      i = 0
      while i < len(nbrs) - 2:
          operanda = nbrs[i]
          operator = nbrs[i + 1]
          operandb = nbrs[i + 2]
          if operator == "*":
              nbrs[i] = 0
              nbrs[i + 1] = "+"
              nbrs[i + 2] = operanda * operandb
          if operator == "/":
              if operandb > 0:
                  nbrs[i] = 0
                  nbrs[i + 1] = "+"
                  nbrs[i + 2] = operanda / operandb
              else:
                  return None
          i += 2
      return nbrs

  def addition(nbrs):
      """
      Add all remaining values.
      Note: not subtracting values here, because parser set
            numbers as negative in first step
      """
      i = 0
      result = 0
      for i in range(0, len(nbrs), 2):
          operand = nbrs[i]
          result += operand
      return result

  nbrs = []
  parse_expression(expression, nbrs)
  # print "nbrs:", nbrs
  if multiply_divide(nbrs) is not None:
      # print "nbrs:", nbrs
      print "result:", addition(nbrs)
  else:
      return None

# calculateV1("2*3+5/6*3+15")
# calculateV1("2*3-5/6*3+15")
# calculateV1("1+2+3")
# calculateV1("-1-2-3")
# calculateV1("2*2*2")
# calculateV1("-2*2*2")
# calculateV1("-2*-2*2")
# calculateV1("-2*-2*-2")
# calculateV1("1")
# calculateV1("-1")
# calculateV1("2--1")
# calculateV1("1+-1")

## --------------------------------------------------------------------------------
def calculateV2(expression):
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

  def getresult(exp):
      """
      Process expression and return result
      Input: exp as expression parts list -> [2,+,3,*,4] etc.
      """

      print "exp:", exp

      nds = deque()
      ops = deque()

      for i in range(len(exp)):

          # Let's do some stacking
          future_op = None
          if type(exp[i]) is str:
              # stack operator
              ops.append(exp[i])
          else:
              # stack operand
              nds.append(exp[i])
              if (i + 1) < len(exp):
                  future_op = exp[(i + 1)]

          # Let's do some processing
          if future_op is not None:
              run_operations(nds, ops, future_op)

      # process the last final remaining bits
      run_operations(nds, ops, None)

      if len(nds) == 1:
          return nds[0]
      else:
          return None

  def expressiontolist():
      infix = []
      while True:
          operand = getoperand()
          if operand is not None:
              infix.append(operand)
          operator = getoperator()
          if operator is not None:
              infix.append(operator)
          else:
              break
      return infix

  index = [0]
  def getoperand():
      """
      Get number, including negative numbers
      """
      nbr = ""
      digits = "0123456789"
      if index[0] < len(expression):
          for c in expression[index[0]:]:
              if nbr:
                  if c in digits:
                      nbr += c
                  else:
                      index[0] += len(nbr)
                      return float(nbr)
              else:
                  if c in "+-" or c in digits:
                      nbr = c
      if nbr:
          index[0] += len(nbr)
          return float(nbr)
      return None

  def getoperator():
      """
      Get operators, including +, *, /
      """
      opr = ""
      if index[0] < len(expression) and expression[index[0]] in "+-*/":
          opr = expression[index[0]]
          index[0] += 1
          return opr
      else:
          return None

  ## INIT calling method for V2
  try:
      print "result:", getresult(expressiontolist())
  except ZeroDivisionError:
      print "Division by zero error"

calculateV2("1+2+4*3/2+5")
# calculateV2("2*3+5/6*3+15")
# calculateV2("2*3-5/6*3+15")
# calculateV2("1+2+3")
# calculateV2("-1-2-3")
# calculateV2("2*2*2")
# calculateV2("-2*2*2")
# calculateV2("-2*-2*2")
# calculateV2("-2*-2*-2")
# calculateV2("1")
# calculateV2("-1")
# calculateV2("2--1")
# calculateV2("1+-1")

## --------------------------------------------------------------------------------
def calculateV3(expression):
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
      for i in range(len(infix)):
          if type(infix[i]) == str and infix[i] in "+-*/":
              # operator
              if stack:
                  # print stack
                  while stack:
                      # take a peek
                      peek = stack[-1]
                      # pop to postfix if operation less or equal to peek
                      if infix[i] in "*/":
                          # operator is *,/ which is <= *,/
                          if peek in "*/":
                              # equal value
                              postfix.append(stack.pop())
                          else:
                              break
                      else:
                          # operator is +,- which is <= *,/,+,-
                          postfix.append(stack.pop())
              # add current operator to stack
              stack.append(infix[i])
          else:
              # operand
              postfix.append(infix[i])
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

  def expressiontolist():
      infix = []
      while True:
          operand = getoperand()
          if operand is not None:
              infix.append(operand)
          operator = getoperator()
          if operator is not None:
              infix.append(operator)
          else:
              break
      return infix

  index = [0]
  def getoperand():
      """
      Get number, including negative numbers
      """
      nbr = ""
      for c in expression[index[0]:]:
          if c in "+-*/":
              if nbr:
                  # sign signals end if nbr already set
                  index[0] += len(nbr)
                  return float(nbr)
              else:
                  # start building nbr
                  # assume formatting correct
                  nbr += c
          else:
              # build nbr
              nbr += c
      if nbr:
          return float(nbr)
      return None

  def getoperator():
      """
      Get operators, including +, *, /
      """
      # print "index:", index[0]
      if expression[index[0]] in "+-*/":
          index[0] += 1
          return expression[index[0] - 1]
      else:
          return None

  print postfixvalue(infixtopostfix(expressiontolist()))

# calculateV3("1+2+4*3/2+5")  # postfix: 1,2,+,4,3,*,2/+5+ -> 14
# calculateV3("2*3+5/6*3+15")
# calculateV3("2*3-5/6*3+15")
# calculateV3("1+2+3")
# calculateV3("-1-2-3")
# calculateV3("2*2*2")
# calculateV3("-2*2*2")
# calculateV3("-2*-2*2")
# calculateV3("-2*-2*-2")
# calculateV3("1")
# calculateV3("-1")
# calculateV3("2--1")
# calculateV3("1+-1")
