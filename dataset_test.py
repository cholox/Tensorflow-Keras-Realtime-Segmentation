import tensorflow as tf
import matplotlib.pyplot as plt
from utils.load_datasets import DatasetGenerator
from utils.load_semantic_datasets import SemanticGenerator
import argparse
from skimage import color

parser = argparse.ArgumentParser()
parser.add_argument("--dataset_dir", type=str, help="데이터셋 다운로드 디렉토리 설정", default='./datasets/')
parser.add_argument("--dataset_type", type=str, help="테스트할 데이터셋 선택  'binary' or 'semantic'", default='semantic')
parser.add_argument("--dataset_nums", type=int, help="테스트 이미지 개수  'binary' or 'semantic'", default=100)
args = parser.parse_args()

DATASET_DIR = args.dataset_dir
DATASET_TYPE = args.dataset_type
DATASET_NUMS = args.dataset_nums
IMAGE_SIZE = (1024, 1024)

if __name__ == "__main__":
    if DATASET_TYPE == 'binary':
        train_dataset_config = DatasetGenerator(DATASET_DIR, IMAGE_SIZE, batch_size=1, mode='train')
    else:
        train_dataset_config = SemanticGenerator(DATASET_DIR, IMAGE_SIZE, batch_size=1, mode='train')
    train_data = train_dataset_config.get_testData(train_dataset_config.train_data)

    rows = 1
    cols = 3

    for img, mask, original in train_data.take(DATASET_NUMS):
        mask = tf.cast(mask, tf.float32)

        fig = plt.figure()
        ax0 = fig.add_subplot(rows, cols, 1)
        ax0.imshow(img[0])
        ax0.set_title('img')
        ax0.axis("off")

        ax0 = fig.add_subplot(rows, cols, 2)
        ax0.imshow(mask[0, :, :, 0])
        ax0.set_title('mask')
        ax0.axis("off")

        ax0 = fig.add_subplot(rows, cols, 3)
        ax0.imshow(original[0])
        ax0.set_title('original')
        ax0.axis("off")
        plt.show()
