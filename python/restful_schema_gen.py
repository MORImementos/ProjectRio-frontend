import glob
import ast
import re
import inspect
import os

def find_py_files(folder_path):
    py_files = []
    
    # Recursive glob search for .py files
    for file_path in glob.iglob(os.path.join(folder_path, '**', '*.py'), recursive=True):
        py_files.append(file_path)
        with open(file_path, 'r') as file:
            code = file.read()
            route_match = re.findall(r"@app\.route\(\'(.*?)\'", code)
            if route_match:
                route = route_match.group(1)
                print(route)
            methods_match = re.findall(r"methods=\[(.*?)\]", code)
            if methods_match:
                methods = methods_match.group(1)
                print(methods)
            args_match = re.findall(r"request\.json\['(.*?)'\]", code)
            if args_match:
                args = args_match.group(1)
                print(args)

    return py_files


# def analyze_python_code(file_path):
#     with open(file_path, 'r') as file:
#         source_code = file.read()
        
#         # Parse the Python code into an abstract syntax tree
#         try:
#             tree = ast.parse(source_code)
#         except SyntaxError as e:
#             print(f"Error parsing {file_path}: {e}")
#             return
        
#         # Store information about functions with decorators
#         functions_with_decorators = []
#         for node in ast.walk(tree):

#             if isinstance(node, ast.FunctionDef):
#                 if len(node.decorator_list) > 0:
#                     print(inspect.getmembers(node))
#                     function_info = {
#                         'name': node.name,
#                         'method': 'GET' if any(arg.arg == 'request' for arg in node.args.args) else 'POST',
#                         'args': [arg.arg for arg in node.args.args],
#                         'request_json': 'request.json' in ast.dump(node),
#                         # Add more properties as needed
#                     }
#                     functions_with_decorators.append(function_info)
        
#         return functions_with_decorators

# # Usage example
folder_path = 'C:/Users/micah/WebstormProjects/rioSkeleton/rioskeleton/python/ProjectRio-web/app/views'
py_files = find_py_files(folder_path)

# # Analyze each .py file
# for file_path in py_files:
#     functions_with_decorators = analyze_python_code(file_path)
#     if len(functions_with_decorators) > 0:
#         print(f"Functions with decorators in {file_path}:")
#         for function_info in functions_with_decorators:
#             print(function_info)
#         print()