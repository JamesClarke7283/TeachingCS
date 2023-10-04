// Importing the Express library
// @deno-types="npm:@types/express"
import express from "npm:express";

// Initialize the Express application
const app = express();

// Define the route for the root URL
app.get('/', (req, res) => {
  res.send('Hello World');
});

// Define the route for the /hello URL with a 'name' parameter
app.get('/hello/:name', (req, res) => {
  const name = req.params.name;
  res.send(`Hello, ${name}`);
});

// Define the route for the /greet URL with 'greeting' and 'name' query parameters
app.get('/greet', (req, res) => {
  const greeting = req.query.greeting || 'Hello';
  const name = req.query.name || 'World';
  res.send(`${greeting}, ${name}`);
});

// Start the server on port 3000
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
