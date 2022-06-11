import logging
import os
import pickle

import clip
import numpy as np
import torch
from PIL import Image
from tqdm import tqdm


class ImageSearcher:
    def __init__(self, model_name='ViT-B/32'):
        self.device = "cuda" if torch.cuda.is_available() else 'cpu'
        logging.info('Starting the model loading process')
        self.model, self.preprocess = clip.load(model_name,
                                                device=self.device)
        logging.info('Model loading process finished')
        self.image_features, self.image_links = self._load_image_index()

    def _generate_image_index(self):
        image_features = []
        image_links = []
        with tqdm(total=len(os.listdir('data/images'))) as pbar:
            for image_name in os.listdir('data/images'):
                try:
                    image = (self.preprocess(Image.open(f'data/images/{image_name}'))
                             .unsqueeze(0)
                             .to(self.device))
                except OSError:
                    pbar.update()
                    continue
                image_links.append(image_name)
                with torch.no_grad():
                    image_features.append(
                        self.model.encode_image(image).cpu().numpy())
                pbar.update()
        with open('data/image_features_links.bin', 'wb') as f:
            pickle.dump([np.array(image_features), image_links], f)
        image_features = torch.tensor(image_features)
        return image_features, image_links

    def _load_image_index(self):
        if not os.path.exists('data/image_features_links.bin'):
            return self._generate_image_index()
        with open('data/image_features_links.bin', 'rb') as f:
            image_features, image_links = pickle.load(f)
        return torch.tensor(image_features), image_links

    def search(self, text):
        text = clip.tokenize([text]).to(self.device)
        with torch.no_grad():
            text_features = self.model.encode_text(text)
        similarity = (100.0 * self.image_features @ text_features.T.cpu())
        return similarity.cpu().numpy()


if __name__ == '__main__':
    searcher = ImageSearcher()
    result = searcher.search('image of a monkey')
    print('\n'.join(searcher.image_links[i]
                    for i in result.squeeze().argsort()[::-1][:5]))
    Image.open(
        f'data/images/{searcher.image_links[result.squeeze().argmax()]}').show()
