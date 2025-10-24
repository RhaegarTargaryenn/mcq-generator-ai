"""
MCQ Generator Package
"""

__version__ = "0.1.0"
__author__ = "Your Name"

from .mcqgen import generate_mcq
from .logger import setup_logger
from .utils import load_config, save_results

__all__ = [
    "generate_mcq",
    "setup_logger",
    "load_config",
    "save_results",
]
