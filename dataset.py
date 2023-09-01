import os
from PIL import Image
import torch
from torchvision import transforms
from torch.utils.data import Dataset, random_split


class MyDataset(Dataset):
    def __init__(self, data_path, train_ratio, test_ratio):
        super(MyDataset, self).__init__()
        self.root_dir = data_path
        self.files = os.listdir(self.root_dir)
        self.img_transform = transforms.Compose([
               transforms.ToTensor()])
        self.data_len = self.__len__()
        self.train_size = int(train_ratio * self.data_len)
        self.test_size = int(test_ratio * self.data_len)
        self.val_size = self.data_len - self.train_size - self.test_size
        self.data_dict = {}
        self.split_data()

    def __getitem__(self, index):
        path = self.files[index]
        image = Image.open(os.path.join(self.root_dir, path, )).convert("RGB")
        image = image.resize((128, 128))
        image = self.img_transform(image)
        sample = {'image': image}

        return sample

    def __len__(self):
        return len(self.files)

    def split_data(self):
        self.d = {f'{y}': x for x, y in zip(random_split(
            dataset=self,
            lengths=[self.train_size, self.test_size, self.val_size]),
                                            ['train', 'val', 'test'])}

    def get_split_data(self, split='train'):
        assert split in ['train', 'val', 'test']
        return self.d[split]


class CLEVR(Dataset):
    def __init__(self, data_path, split='train'):
        super(CLEVR, self).__init__()
        assert split in ['train', 'val', 'test']
        self.split = split
        self.root_dir = data_path + self.split
        self.files = os.listdir(self.root_dir)
        self.img_transform = transforms.Compose([
               transforms.ToTensor()])

    def __getitem__(self, index):
        path = self.files[index]
        image = Image.open(os.path.join(self.root_dir, path, )).convert("RGB")
        image = image.resize((128 , 128))
        image = self.img_transform(image)
        sample = {'image': image}

        return sample

    def __len__(self):
        return len(self.files)