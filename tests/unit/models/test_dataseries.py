import trainer.models.dataseries as ds

class TestWeights:

    def test_init(self):
        assert ds.Weights() is not None
