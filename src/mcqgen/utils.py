"""
Utility Functions for MCQ Generator
Helper functions for file I/O, data processing, and configuration
"""

import json
import os
from typing import Dict, List, Any
from .logger import log_info, log_error, log_debug


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Load configuration from JSON file
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Configuration dictionary
    """
    try:
        if not os.path.exists(config_path):
            log_error(f"Config file not found: {config_path}")
            return {}
        
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        log_info(f"Configuration loaded from {config_path}")
        return config
    
    except Exception as e:
        log_error(f"Error loading config: {str(e)}")
        return {}


def save_results(data: List[Dict[str, Any]], 
                 output_path: str = "output/mcqs.json") -> bool:
    """
    Save generated MCQs to a JSON file
    
    Args:
        data: List of MCQs to save
        output_path: Path to output file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            log_debug(f"Created output directory: {output_dir}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        log_info(f"Results saved to {output_path}")
        return True
    
    except Exception as e:
        log_error(f"Error saving results: {str(e)}")
        return False


def load_text_file(file_path: str) -> str:
    """
    Load text content from a file
    
    Args:
        file_path: Path to text file
        
    Returns:
        File content as string
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        log_info(f"Loaded text file: {file_path}")
        return content
    
    except Exception as e:
        log_error(f"Error loading text file: {str(e)}")
        return ""


def validate_input(text: str, min_length: int = 50) -> bool:
    """
    Validate input text for MCQ generation
    
    Args:
        text: Input text to validate
        min_length: Minimum required length of text
        
    Returns:
        True if valid, False otherwise
    """
    if not text or not isinstance(text, str):
        log_error("Invalid input: text is empty or not a string")
        return False
    
    if len(text.strip()) < min_length:
        log_error(f"Input text too short: {len(text)} chars (minimum: {min_length})")
        return False
    
    log_debug("Input validation passed")
    return True


def format_mcq_for_display(mcq: Dict[str, Any]) -> str:
    """
    Format a single MCQ for human-readable display
    
    Args:
        mcq: MCQ dictionary
        
    Returns:
        Formatted string representation
    """
    formatted = f"\nQuestion: {mcq.get('question', 'N/A')}\n"
    
    options = mcq.get('options', [])
    for idx, option in enumerate(options, 1):
        formatted += f"  {chr(64+idx)}. {option}\n"
    
    formatted += f"\nCorrect Answer: {mcq.get('correct_answer', 'N/A')}"
    formatted += f"\nDifficulty: {mcq.get('difficulty', 'N/A')}\n"
    
    return formatted


def batch_process(texts: List[str], 
                  num_questions_per_text: int = 5) -> List[Dict[str, Any]]:
    """
    Process multiple texts and generate MCQs for each
    
    Args:
        texts: List of text strings
        num_questions_per_text: Number of questions to generate per text
        
    Returns:
        Combined list of all generated MCQs
    """
    from .mcqgen import generate_mcq
    
    all_mcqs = []
    
    for idx, text in enumerate(texts, 1):
        log_info(f"Processing text {idx}/{len(texts)}")
        
        if validate_input(text):
            mcqs = generate_mcq(text, num_questions_per_text)
            all_mcqs.extend(mcqs)
    
    log_info(f"Batch processing complete. Generated {len(all_mcqs)} MCQs")
    return all_mcqs
