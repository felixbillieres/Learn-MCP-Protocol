"""
Test script for project 35
This script verifies the malware analyzer
"""

import sys
import importlib.util
import asyncio
from unittest.mock import AsyncMock, MagicMock

def test_models_exist():
    """Test that models exist"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(solution)
    except Exception as e:
        print(f"Error during import: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    if not hasattr(solution, 'MalwareSample'):
        print("The model 'MalwareSample' does not exist")
        return False
    
    if not hasattr(solution, 'AnalysisResult'):
        print("The model 'AnalysisResult' does not exist")
        return False
    
    if not hasattr(solution, 'YaraRule'):
        print("The model 'YaraRule' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_analyze_file():
    """Test file analysis with elicitation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'samples'):
        solution.samples.clear()
    
    # Mock elicitation for confirmation
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"confirm": True})
    mock_ctx.elicitation = mock_elicitation
    
    try:
        result = await solution.analyze_file("suspicious.exe", "binary_content", mock_ctx)
        
        if not isinstance(result, solution.AnalysisResult):
            print(f"analyze_file should return AnalysisResult, but returned {type(result)}")
            return False
        
        if len(solution.samples) != 1:
            print(f"Sample should be added, but list contains {len(solution.samples)} samples")
            return False
        
        print("analyze_file works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_extract_strings():
    """Test string extraction"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'samples'):
        solution.samples.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"confirm": True})
    mock_ctx.elicitation = mock_elicitation
    
    # Create a sample first
    analysis = await solution.analyze_file("test.exe", "test content", mock_ctx)
    sample_id = analysis.sample_id if hasattr(analysis, 'sample_id') else 0
    
    try:
        result = await solution.extract_strings(sample_id, mock_ctx)
        
        if not isinstance(result, list):
            print(f"extract_strings should return a list, but returned {type(result)}")
            return False
        
        print(f"extract_strings works: extracted {len(result)} strings")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_compare_threat_intel():
    """Test threat intelligence comparison"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'samples'):
        solution.samples.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"confirm": True})
    mock_ctx.elicitation = mock_elicitation
    
    analysis = await solution.analyze_file("malware.exe", "content", mock_ctx)
    sample_id = analysis.sample_id if hasattr(analysis, 'sample_id') else 0
    
    try:
        result = await solution.compare_threat_intel(sample_id, mock_ctx)
        
        if not isinstance(result, list):
            print(f"compare_threat_intel should return a list, but returned {type(result)}")
            return False
        
        print(f"compare_threat_intel works: found {len(result)} matches")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_generate_yara_rule():
    """Test YARA rule generation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'samples'):
        solution.samples.clear()
    
    mock_ctx = AsyncMock()
    mock_elicitation = MagicMock()
    mock_elicitation.create = AsyncMock(return_value={"confirm": True})
    mock_ctx.elicitation = mock_elicitation
    
    analysis = await solution.analyze_file("sample.exe", "content", mock_ctx)
    sample_id = analysis.sample_id if hasattr(analysis, 'sample_id') else 0
    
    try:
        result = await solution.generate_yara_rule(sample_id, mock_ctx)
        
        if not isinstance(result, solution.YaraRule):
            print(f"generate_yara_rule should return YaraRule, but returned {type(result)}")
            return False
        
        if hasattr(result, 'rule') and len(result.rule) == 0:
            print("YARA rule should not be empty")
            return False
        
        print("generate_yara_rule works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Test for Project 35\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing analyze_file...")
    success = asyncio.run(test_analyze_file()) and success
    print()
    
    print("Testing extract_strings...")
    success = asyncio.run(test_extract_strings()) and success
    print()
    
    print("Testing compare_threat_intel...")
    success = asyncio.run(test_compare_threat_intel()) and success
    print()
    
    print("Testing generate_yara_rule...")
    success = asyncio.run(test_generate_yara_rule()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional malware analyzer!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
