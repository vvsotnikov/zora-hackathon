import json
import logging
import os
import pickle

import PIL
import clip
import numpy as np
import torch
from PIL import Image
from tqdm import tqdm

PIL.Image.MAX_IMAGE_PIXELS = 977576000


class ImageSearcher:
    def __init__(self, model_name='ViT-B/32'):
        self.device = "cuda" if torch.cuda.is_available() else 'cpu'
        logging.info('Starting the model loading process')
        self.model, self.preprocess = clip.load(model_name,
                                                device=self.device)
        logging.info('Model loading process finished')
        self.image_features, self.image_links = self._load_image_index()
        with open('data/nft_index.json', 'r') as f:
            self.nft_index = json.load(f)

    def _generate_image_index(self):
        image_features = []
        image_ids = []
        with tqdm(total=len(os.listdir('data/images'))) as pbar:
            for image_name in os.listdir('data/images'):
                try:
                    image = (self.preprocess(Image.open(f'data/images/{image_name}'))
                             .unsqueeze(0)
                             .to(self.device))
                except (OSError, SyntaxError) as e:
                    print(e, image_name)
                    pbar.update()
                    continue
                image_ids.append(image_name.split('.')[0])
                with torch.no_grad():
                    image_features.append(
                        self.model.encode_image(image).cpu().numpy())
                pbar.update()
        print(len(image_ids))
        with open('data/image_features_links.bin', 'wb') as f:
            pickle.dump([np.array(image_features), image_ids], f)
        image_features = torch.tensor(image_features)
        return image_features, image_ids

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
        similarity = (100.0 * self.image_features @ text_features.T.cpu()
                      ).cpu().numpy()
        similarity = similarity.squeeze().argsort()[::-1][:6]
        return [{'contract': self.nft_index[self.image_links[i]][0],
                 'token_id': self.nft_index[self.image_links[i]][1]}
                for i in similarity]

    def search_image(self, image):
        image = (self.preprocess(image)
                 .unsqueeze(0)
                 .to(self.device))
        with torch.no_grad():
            image_features = self.model.encode_image(image)
        similarity = (100.0 * self.image_features @ image_features.T.cpu()
                      ).cpu().numpy()
        similarity = similarity.squeeze().argsort()[::-1][:6]
        return [{'contract': self.nft_index[self.image_links[i]][0],
                 'token_id': self.nft_index[self.image_links[i]][1]}
                for i in similarity]


if __name__ == '__main__':
    searcher = ImageSearcher()
    result = searcher.search('image of a monkey')
    print(result)
