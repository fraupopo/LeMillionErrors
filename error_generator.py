import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def get_real_imports():
    # List of real, unused imports
    imports = [
        "java.util.ArrayList",
        "java.util.HashMap",
        "java.util.HashSet",
        "java.util.LinkedList",
        "java.util.PriorityQueue",
        "java.util.TreeMap",
        "java.util.TreeSet",
        "java.io.BufferedReader",
        "java.io.FileReader",
        "java.io.PrintWriter"
    ]
    result_import = random.choice(imports)
    return f"import {result_import};"

def generate_random_value(value_type):
    if value_type == "int":
        return random.randint(1, 100)
    elif value_type == "double":
        return round(random.uniform(1.0, 100.0), 2)
    elif value_type == "boolean":
        return random.choice(["true", "false"])
    elif value_type == "String":
        return '"' + generate_random_string(random.randint(3, 10)) + '"'
    elif value_type == "char":
        return f"'{random.choice(string.ascii_letters)}'"
    return None

def generate_incorrect_if_statement():
    error_types = [
        "empty_statement",
        "unreachable_code"
    ]
    error_type = random.choice(error_types)

    if error_type == "empty_statement":
        return "if (true) {    };"
    elif error_type == "unreachable_code":
        return f"if (true) {{\n    System.out.println(\"Unreachable code\");\n}}\nelse {{\n    System.out.println(\"This will never be executed\");\n}}"

def generate_unused_variable():
    variable_name = generate_random_string(5)
    type_choice = random.choice(["int", "double", "boolean", "String", "char"])
    value = generate_random_value(type_choice)
    return f"{type_choice} {variable_name} = {value};"

def generate_method_with_unused_argument():
    methods = [
        '''
        public void {method_name}(int {unused_arg1}, int {used_arg}) {{
            System.out.println("This method has an unused argument.");
        }}
        ''',
        '''
        public void {method_name}(String {unused_arg1}, String {used_arg}) {{
            System.out.println("This method has an unused argument.");
        }}
        ''',
        '''
        public void {method_name}(boolean {unused_arg1}, boolean {used_arg}) {{
            System.out.println("This method has an unused argument.");
        }}
        ''',
        '''
        public void {method_name}(double {unused_arg1}, double {used_arg}) {{
            System.out.println("This method has an unused argument.");
        }}
        '''
    ]
    method_template = random.choice(methods)
    method_name = generate_random_string(7)
    unused_arg1 = generate_random_string(5)
    used_arg = generate_random_string(5)
    return method_template.format(method_name=method_name, unused_arg1=unused_arg1, used_arg=used_arg)

def generate_java_program(class_name):
    imports = "\n".join([get_real_imports() for _ in range(100)])
    body = [
        "\n".join(generate_incorrect_if_statement() for _ in range(300)),
        "\n".join(generate_unused_variable() for _ in range(300)),
        "\n".join(generate_method_with_unused_argument() for _ in range(300))
    ]

    java_program = f"""
    
    {imports}
    
    public class {class_name} {{
        public static void mainMethod(String[] args) {{
            {body[0]}
            {body[1]}
        }}
        
        {body[2]}
    }}
    """

    return java_program

def save_java_program(file_path, class_name):
    java_program = generate_java_program(class_name)
    with open(file_path, "w") as file:
        file.write(java_program)
    print(f"Java program saved to {file_path}")

if __name__ == "__main__":
    # Hardcoded path to save the Java program
    for i in range(1000):
        class_name = f"Error{i}"
        file_path = f"src/{class_name}.java"
        save_java_program(file_path, class_name)
