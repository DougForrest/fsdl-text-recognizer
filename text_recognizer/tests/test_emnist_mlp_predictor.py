import pathlib
import unittest

from text_recognizer.emnist_mlp_predictor import EmnistMlpPredictor


SUPPORT_DIRNAME = pathlib.Path(__file__).parents[0].resolve() / 'support' / 'emnist'


class TestEmnistMlpPredictor(unittest.TestCase):
    def test(self):
      predictor = EmnistMlpPredictor()

      for filename in SUPPORT_DIRNAME.glob('*.png'):
        pred, conf = predictor.predict(str(filename))
        print(pred, conf, filename.stem)
        self.assertEqual(pred, filename.stem)
        self.assertGreater(conf, 0.9)
