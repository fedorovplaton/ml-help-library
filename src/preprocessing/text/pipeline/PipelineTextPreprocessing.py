"""
    PipelineTextPreprocessing
"""

from typing import List
from src.preprocessing.text.pipeline.base.PipelineBase import PipelineBase


class PipelineTextPreprocessing(PipelineBase[List[str]]):
    """
        PipelineTextPreprocessing
    """
    def __init__(self):
        super().__init__(name='TextPreprocessingPipeline')
