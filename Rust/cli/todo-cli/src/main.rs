use clap::{Arg, App};
use std::fs::OpenOptions;
use std::io::{self, Read, Write};
use serde_json::{from_str, to_string};

mod todo;
use todo::Todo;

const TODO_FILE: &str = "todo.json";

fn main() -> io::Result<()> {
    let matches = App::new("Todo App")
        .version("1.0")
        .author("Your Name <yourname@example.com>")
        .about("Manage your todo list")
        .subcommand(
            App::new("add")
                .about("Add a new task to the list")
                .arg(
                    Arg::new("TASK")
                        .help("The task to add")
                        .required(true)
                        .index(1),
                ),
        )
        .subcommand(
            App::new("done")
                .about("Mark a task as done")
                .arg(
                    Arg::new("INDEX")
                        .help("The index of the task to mark as done")
                        .required(true)
                        .index(1),
                ),
        )
        .subcommand(App::new("list").about("List all tasks"))
        .get_matches();

    let mut file = OpenOptions::new()
        .read(true)
        .write(true)
        .create(true)
        .open(TODO_FILE)?;

    let mut content = String::new();
    file.read_to_string(&mut content)?;

    let mut todo_list: Vec<Todo> = if content.is_empty() {
        Vec::new()
    } else {
        from_str(&content).unwrap()
    };

    if let Some(matches) = matches.subcommand_matches("add") {
        if let Some(task) = matches.value_of("TASK") {
            todo_list.push(Todo::new(task));
        }
    }

    if let Some(matches) = matches.subcommand_matches("done") {
        if let Some(index) = matches.value_of("INDEX") {
            if let Ok(index) = index.parse::<usize>() {
                if index < todo_list.len() {
                    todo_list[index].done();
                }
            }
        }
    }
    

    // Write the updated todo list back to the file
    file.set_len(0)?;
    file.write_all(to_string(&todo_list)?.as_bytes())?;

    if matches.subcommand_matches("list").is_some() {
        println!("Current Tasks:");
        for (i, todo) in todo_list.iter().enumerate() {
            let status = if todo.done { "Done" } else { "Not done" };
            println!("{}: {} [{}]", i, todo.task, status);
        }
    }

    Ok(())
}
