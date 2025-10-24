"""
Logger Module for MCQ Generator
Provides logging functionality for the application
"""

import logging
import os
from datetime import datetime


def setup_logger(name: str = "mcqgen", log_dir: str = "logs") -> logging.Logger:
    """
    Set up and configure a logger for the application
    
    Args:
        name: Name of the logger
        log_dir: Directory to store log files
        
    Returns:
        Configured logger instance
    """
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Create formatters
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_formatter = logging.Formatter(
        '%(levelname)s - %(message)s'
    )
    
    # File handler
    log_file = os.path.join(log_dir, f"{name}_{datetime.now().strftime('%Y%m%d')}.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


# Create default logger instance
default_logger = setup_logger()


def log_info(message: str):
    """Log info level message"""
    default_logger.info(message)


def log_error(message: str):
    """Log error level message"""
    default_logger.error(message)


def log_warning(message: str):
    """Log warning level message"""
    default_logger.warning(message)


def log_debug(message: str):
    """Log debug level message"""
    default_logger.debug(message)
