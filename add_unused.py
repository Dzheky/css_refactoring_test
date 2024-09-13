import random

# Function to generate random unused CSS classes
def generate_unused_css(num_classes):
    css_classes = ""
    for i in range(1, num_classes + 1):
        class_name = f".unused-class-{i}"
        styles = [
            f"color: #{random.randint(100000, 999999):06x};",
            f"font-size: {random.randint(12, 24)}px;",
            f"margin-left: {random.randint(0, 50)}px;",
            f"padding: {random.randint(0, 20)}px;",
            f"border: {random.randint(1, 5)}px solid #{random.randint(100000, 999999):06x};",
            f"background-color: #{random.randint(100000, 999999):06x};",
            f"text-transform: uppercase;",
            f"font-weight: {random.choice(['bold', 'normal', 'lighter'])};",
            f"letter-spacing: {random.randint(0, 5)}px;",
            f"line-height: {random.uniform(1.0, 2.0):.1f};"
        ]
        css_classes += f"{class_name} {{\n    " + "\n    ".join(random.sample(styles, 4)) + "\n}\n\n"
    return css_classes

# Function to append generated CSS to the input file
def update_css_file(file_path, num_classes):
    # Generate the random unused CSS classes
    unused_css = generate_unused_css(num_classes)

    # Read the existing CSS content
    with open(file_path, 'r') as file:
        existing_css = file.read()

    # Append the generated unused CSS classes to the existing CSS
    with open(file_path, 'a') as file:
        file.write("\n/* Unused CSS Classes */\n")
        file.write(unused_css)

    print(f"Added {num_classes} unused CSS classes to {file_path}.")

# Example usage
css_file_path = "dynamic_unoptimized.css"  # Replace with your CSS file path
num_classes_to_add = 500  # Number of unused CSS classes to add

# Update the CSS file with unused classes
update_css_file(css_file_path, num_classes_to_add)
