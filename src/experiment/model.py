import torch
import torch.nn as nn
import torchvision.models as models


class VisualEncoder(nn.Module):
    def __init__(self, feature_dim=2048):
        super().__init__()
        resnet = models.resnet50(pretrained=True)
        self.features = nn.Sequential(*list(resnet.children())[:-1])
        self.feature_dim = feature_dim
        for param in self.features.parameters():
            param.requires_grad = False

    def forward(self, x):
        with torch.no_grad():
            feat = self.features(x)
        return feat.view(feat.size(0), -1)


class LanguageEncoder(nn.Module):
    def __init__(self, vocab_size, embed_dim=256, hidden_dim=256):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.hidden_dim = hidden_dim

    def forward(self, x):
        emb = self.embedding(x)
        out, (h, c) = self.lstm(emb)
        return h[-1]


class ActionHistoryEncoder(nn.Module):
    """A small innovation: encode the last few actions to reduce looping."""
    def __init__(self, num_actions=4, history_len=3, out_dim=32):
        super().__init__()
        self.history_len = history_len
        self.embedding = nn.Embedding(num_actions, 8)
        self.fc = nn.Linear(history_len * 8, out_dim)

    def forward(self, action_history):
        emb = self.embedding(action_history)
        emb = emb.view(emb.size(0), -1)
        return self.fc(emb)


class VLNPolicy(nn.Module):
    def __init__(self, vocab_size, num_actions=4, use_action_history=True):
        super().__init__()
        self.visual_encoder = VisualEncoder()
        self.language_encoder = LanguageEncoder(vocab_size)
        self.use_action_history = use_action_history
        if use_action_history:
            self.action_history_encoder = ActionHistoryEncoder(num_actions=num_actions)
            fusion_dim = 2048 + 256 + 32
        else:
            fusion_dim = 2048 + 256
        self.policy_lstm = nn.LSTM(fusion_dim, 512, batch_first=True)
        self.action_head = nn.Linear(512, num_actions)

    def forward(self, images, instructions, action_history=None, hidden=None):
        vis_feat = self.visual_encoder(images)
        lang_feat = self.language_encoder(instructions)
        feats = [vis_feat, lang_feat]
        if self.use_action_history and action_history is not None:
            hist_feat = self.action_history_encoder(action_history)
            feats.append(hist_feat)
        fused = torch.cat(feats, dim=1).unsqueeze(1)
        out, hidden = self.policy_lstm(fused, hidden)
        logits = self.action_head(out.squeeze(1))
        return logits, hidden
