def doSomething(par):
  try:
    print("par:", par)
    print(" length:", len(par), end="")
    print(" Value at index 5:", par[5], end="")
    print(" As an integer:", int(par), end="")
  except ValueError as e:
    print(type(e))
    raise ValueError("ValueError: " + str(e))
  except TypeError as e:
    raise TypeError("TypeError: " + str(e))
  except IndexError as e:
    raise IndexError("IndexError: " + str(e))
  except KeyError as e:
    raise KeyError("KeyError: " + str(e))
  finally:
    print()
    