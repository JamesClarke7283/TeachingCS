// Define the main function that gets executed when the program is run.
fn main() {
    // Create a new, empty vector of strings to hold the shopping list items.
    let mut shopping_list: Vec<String> = Vec::new();

    // Start an infinite loop to repeatedly ask the user for input.
    loop {
        // Create a new, mutable string to store the user's input.
        let mut input = String::new();

        // Print a prompt asking the user for a shopping list item.
        println!("Enter a shopping list item(type 'quit' to quit): ");

        // Read a line of input from the user, trim it and assign it to the 'input' string.
        std::io::stdin().read_line(&mut input).unwrap();

        // Convert the input to a string to ensure it's in the correct format.
        input = input.to_string();

        // If the user types 'quit', break the loop and end the program.
        if input.trim() == "quit" {
            break;
        }

        // Push the user's input onto the end of the shopping_list vector.
        shopping_list.push(input.to_string());

        // Print a message indicating the current shopping list.
        println!("Shopping list: ");

        // Iterate over each item in the shopping list vector.
        for item in &shopping_list {
            // Print the item followed by a space.
            print!("{}", item);
        }
    }
}
