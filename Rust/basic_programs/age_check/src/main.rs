fn main() {
    // Print a prompt asking the user for their age.
    println!("Enter your age: ");
    // Create a new, mutable string to store the user's input.
    let mut age_str = String::new();

    // Read a line of input from the user and assign it to the 'age_str' string.
    std::io::stdin().read_line(&mut age_str).unwrap();

    // Convert the input to a string to ensure it's in the correct format.
    let age: u8 = age_str.trim().parse().unwrap();

    // If the user is 21 or older, print a message indicating they can drink.
    if age >= 21 {
        println!("You can drink!");
    } else {
        println!("You can't drink!");
    }
}
