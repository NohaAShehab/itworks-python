def name_validation(var_text):
  while(True):
      user_input = input(f"Enter your {var_text} : ")
      user_input = user_input.strip()
      if len(user_input) >0 and not user_input.isspace() and user_input.isalpha():
          break
  return user_input

# print(name_validation("firstname"))


def text_validation(var_text):
  while(True):
    user_input  = input(f"Enter your {var_text} : ")
    user_input = user_input.strip()
    if(user_input.isspace() or user_input == ""):
      print(f"your {var_text} must not be empty or spaces ")
      continue
    else:
      break
  return user_input