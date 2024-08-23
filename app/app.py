import os

# Access and print each environment variable
my_variable_from_os = os.getenv('MY_VARIABLE_FROM_OS')
my_variable_from_env = os.getenv('MY_VARIABLE_FROM_ENV')
my_variable_from_dockerfile = os.getenv('MY_VARIABLE_FROM_DOCKERFILE')
my_variable_from_dc = os.getenv('MY_VARIABLE_FROM_DC')
my_build_arg_from_dc = os.getenv('MY_BUILD_ARG_FROM_DC')
my_build_arg = os.getenv('MY_VARIABLE')  

# Print the environment variables
print(f'MY_VARIABLE_FROM_OS: {my_variable_from_os}')
print(f'MY_VARIABLE_FROM_ENV: {my_variable_from_env}')
print(f'MY_VARIABLE_FROM_DOCKERFILE: {my_variable_from_dockerfile}')
print(f'MY_VARIABLE_FROM_DC: {my_variable_from_dc}')
print(f'MY_BUILD_ARG (MY_VARIABLE): {my_build_arg}')
print(f'MY_BUILD_ARG_FROM_DC (MY_BUILD_ARG_FROM_DC): {my_build_arg_from_dc}')
