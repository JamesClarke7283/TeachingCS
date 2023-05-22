// Define the main function that gets executed when the program is run.
fn main() {
    // Print a prompt asking the user for a calculation.
    println!("Enter a calculation");

    // Create a new mutable string to store the user's input.
    let mut input = String::new();

    // Read a line of input from the user, trim it and assign it to the 'input' string.
    std::io::stdin().read_line(&mut input).unwrap();

    // Create an iterator over the characters in the input string.
    let mut chars = input.chars();

    // Create a new, empty vector to store the numbers from the user's input.
    let mut numbers = Vec::new();

    // Create a new mutable string to store the operator from the user's input.
    let mut op = String::new();

    // Iterate over each character in the input string.
    for c in chars {
        // If the character is numeric, add it to the 'numbers' vector.
        if c.is_numeric() {
            numbers.push(c.to_string());
        // If the character is an operator, store it in the 'op' string.
        } else if c == '+' || c == '-' || c == '*' || c == '/'{
            op = c.to_string();
        }
    }

    // Convert the first two numbers from the 'numbers' vector to i32 type.
    let num1: i32 = numbers[0].trim().parse().unwrap();
    let num2: i32 = numbers[1].trim().parse().unwrap();

    // Calculate the result based on the operator and the two numbers.
    let result = match op.as_str() {
        "+" => num1 + num2,
        "-" => num1 - num2,
        "*" => num1 * num2,
        "/" => num1 / num2,
        // Return 0 if the operator is not recognised.
        _ => 0,
    };

    // Print the result.
    println!("Result: {}", result);
}
