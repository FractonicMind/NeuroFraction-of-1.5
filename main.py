"""
main.py
NeuroFraction-of-1.5

Main entry point for training and evaluating the neural network.
"""

from core import Base15Number
from losses import MSELoss
from optim import Base15SGD
from base15_nn import Base15NeuralNetwork

def main():
    # Example dataset (XOR problem)
    X = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    y = [0, 1, 1, 0]

    # Initialize the neural network
    nn = Base15NeuralNetwork(input_size=2, hidden_size=4, output_size=1)
    criterion = MSELoss()
    optimizer = Base15SGD(nn.parameters(), lr=0.1)

    # Training loop
    epochs = 1000
    for epoch in range(epochs):
        total_loss = Base15Number([0])
        for xi, yi in zip(X, y):
            # Forward pass
            output = nn.forward(xi)[0]
            
            # Compute loss
            loss = criterion(output, yi)
            total_loss += loss

            # Zero gradients
            optimizer.zero_grad()

            # Backward pass
            output.gradient.value = Base15Number([1.0])  # dL/dL = 1
            output.gradient.backward()

            # Update weights
            optimizer.step()
        
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {total_loss.to_float() / len(X):.4f}")

if __name__ == "__main__":
    main()
