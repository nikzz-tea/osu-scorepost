from PIL import Image
from .screenshot_util import write_with_img
from .score import ScoreInfo

def generate_statistics_taiko(im: Image.Image, score: ScoreInfo):
    count_300 = f"{score.count_300}"
    count_100 = f"{score.count_100}"
    count_miss = f"{score.count_miss}"

    accuracy = f"{score.accuracy * 100 :.2f}%"
    max_combo = f"{score.max_combo}"

    write_with_img(count_300, 180, 325, 1.5, im)
    write_with_img(count_100, 180, 455, 1.5, im)
    write_with_img(count_miss, 180, 575, 1.5, im)
    write_with_img(max_combo, 35, 740, 1.5, im)
    write_with_img(accuracy, 440, 740, 1.5, im)