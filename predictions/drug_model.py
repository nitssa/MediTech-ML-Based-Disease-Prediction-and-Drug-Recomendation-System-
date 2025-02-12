import torch.nn as nn

class DrugRecommendationModel(nn.Module):
    def __init__(self):
        super(DrugRecommendationModel, self).__init__()
        self.fc1 = nn.Linear(75160, 100)
        self.fc2 = nn.Linear(100, 100)
        self.fc3 = nn.Linear(100, 3264)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x
