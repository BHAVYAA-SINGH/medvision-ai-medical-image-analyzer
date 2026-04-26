import torch
import cv2
import numpy as np


class GradCAM:
    def __init__(self, model, target_layer):
        self.model = model
        self.target_layer = target_layer

        self.activations = None
        self.gradients = None

        self._register_forward_hook()

    # ---------------------------------
    # Forward hook ONLY (safe)
    # ---------------------------------
    def _register_forward_hook(self):

        def forward_hook(module, input, output):
            self.activations = output

            # attach gradient hook directly to tensor
            output.register_hook(self._save_gradient)

        self.target_layer.register_forward_hook(forward_hook)

    def _save_gradient(self, grad):
        self.gradients = grad

    # ---------------------------------
    # Generate CAM
    # ---------------------------------
    def generate(self, input_tensor):

        self.model.zero_grad()

        output = self.model(input_tensor)
        class_idx = torch.argmax(output, dim=1)

        loss = output[:, class_idx]
        loss.backward()

        gradients = self.gradients[0]
        activations = self.activations[0]

        weights = gradients.mean(dim=(1, 2))

        cam = torch.zeros(activations.shape[1:], device=activations.device)

        for i, w in enumerate(weights):
            cam += w * activations[i]

        cam = torch.relu(cam)

        cam = cam.detach().cpu().numpy()
        cam = cv2.resize(cam, (224, 224))

        cam -= cam.min()
        cam /= (cam.max() + 1e-8)

        return cam


def overlay_heatmap(image, cam, alpha=0.0025):

    heatmap = cv2.applyColorMap(
        np.uint8(255 * cam), cv2.COLORMAP_JET
    )

    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)

    overlay = heatmap * alpha + image
    overlay = overlay / overlay.max()

    return np.uint8(255 * overlay)
