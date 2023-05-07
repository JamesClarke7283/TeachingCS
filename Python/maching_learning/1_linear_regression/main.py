import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Load the Boston Housing dataset
boston = datasets.fetch_openml(data_id=531, as_frame=True)

X = boston.data['RM'].to_numpy()  # Average number of rooms
y = boston.target.to_numpy()      # House prices

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Neural network model
model = Sequential()
model.add(Dense(1, input_dim=1, activation='linear'))

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.1), loss='mse')

# Train the model
history = model.fit(X_train, y_train, epochs=100, verbose=0)

loss = model.evaluate(X_test, y_test, verbose=0)
print(f"Test loss: {loss}")

plt.scatter(X_train, y_train, label='Training data')
plt.scatter(X_test, y_test, label='Testing data')

x_line = np.arange(min(X), max(X), 0.1)
y_line = model.predict(x_line)

plt.plot(x_line, y_line, 'r', label='Linear Regression')
plt.xlabel('Average Number of Rooms')
plt.ylabel('House Price')
plt.legend()
plt.show()
