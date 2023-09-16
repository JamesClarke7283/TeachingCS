use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct Todo {
    pub task: String,
    pub done: bool,
}

impl Todo {
    pub fn new(task: &str) -> Self {
        Self {
            task: task.to_string(),
            done: false,
        }
    }

    pub fn done(&mut self) {
        self.done = true;
    }
}
