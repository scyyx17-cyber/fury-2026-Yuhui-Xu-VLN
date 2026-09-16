import argparse
import yaml
import torch
import torch.nn as nn
import torch.optim as optim
from model import VLNPolicy


def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def train(config):
    device = torch.device(
        f"cuda:{config['training']['gpu']}" if torch.cuda.is_available() else "cpu"
    )
    print(f"Using device: {device}")

    vocab_size = 5000
    model = VLNPolicy(
        vocab_size=vocab_size,
        use_action_history=config['model']['use_action_history']
    ).to(device)
    optimizer = optim.Adam(model.parameters(), lr=config['training']['learning_rate'])
    criterion = nn.CrossEntropyLoss()

    print("Training started.")
    for epoch in range(config['training']['epochs']):
        print(f"Epoch {epoch + 1}/{config['training']['epochs']}")
        # In a real run, loop over the R2R dataset here.
    print("Training finished.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config.yaml')
    args = parser.parse_args()
    config = load_config(args.config)
    train(config)
