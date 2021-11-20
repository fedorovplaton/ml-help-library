from src.preprocessing.text.pipeline.PipelineTextPreprocessing import PipelineTextPreprocessing
from src.preprocessing.text.pipeline.UnitLower import UnitLower
from src.preprocessing.text.pipeline.UnitSplitJoinTokenizer import UnitSplitJoinTokenizer


if __name__ == '__main__':
    pipe = PipelineTextPreprocessing()
    pipe.set_units([UnitSplitJoinTokenizer(), UnitLower()])

    texts = [', .df ,f. ,d.sf, sdf sdf sdfsd FDGSGFDG . .ds f ered?']
    result = pipe.execute(texts)

    print(result)
