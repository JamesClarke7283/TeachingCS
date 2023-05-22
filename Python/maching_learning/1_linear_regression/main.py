import numpy as np  # Import NumPy library for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib's pyplot for plotting
from sklearn import datasets  # Import the datasets module from scikit-learn
from sklearn.model_selection import train_test_split  # Import train_test_split function to split data into training and testing sets
from tensorflow.keras.models import Sequential  # Import Sequential model class from TensorFlow's Keras API
from tensorflow.keras.layers import Dense  # Import Dense layer class from TensorFlow's Keras API
from tensorflow.keras.optimizers import Adam  # Import Adam optimizer class from TensorFlow's Keras API

# Load the Boston Housing dataset
boston = datasets.fetch_openml(data_id=531, as_frame=True)

X = boston.data['RM'].to_numpy()  # Extract the average number of rooms (RM) as a NumPy array
y = boston.target.to_numpy()      # Extract the target values (house prices) as a NumPy array

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a neural network model with a single layer (linear regression)
model = Sequential()
model.add(Dense(1, input_dim=1, activation='linear'))

# Compile the model with the Adam optimizer and mean squared error loss function
model.compile(optimizer=Adam(learning_rate=0.1), loss='mse')

# Train the model on the training data for 100 epochs without displaying progress (verbose=0)
history = model.fit(X_train, y_train, epochs=100, verbose=0)

# Evaluate the model on the testing data and print the loss
loss = model.evaluate(X_test, y_test, verbose=0)
print(f"Test loss: {loss}")

# Create a scatter plot of the training data
plt.scatter(X_train, y_train, label='Training data')
# Create a scatter plot of the testing data
plt.scatter(X_test, y_test, label='Testing data')

# Generate an array of x values for the linear regression line
x_line = np.arange(min(X), max(X), 0.1)
# Generate an array of corresponding y values using the trained model
y_line = model.predict(x_line)

# Plot the linear regression line
plt.plot(x_line, y_line, 'r', label='Linear Regression')
# Set the x-axis label
plt.xlabel('Average Number of Rooms')
# Set the y-axis label
plt.ylabel('House Price')
# Add a legend to the plot
plt.legend()
# Display the plot
plt.show()
