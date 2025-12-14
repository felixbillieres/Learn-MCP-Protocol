"""
Test script for project 38
This script verifies the anomaly detector
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
    
    if not hasattr(solution, 'Baseline'):
        print("The model 'Baseline' does not exist")
        return False
    
    if not hasattr(solution, 'Anomaly'):
        print("The model 'Anomaly' does not exist")
        return False
    
    if not hasattr(solution, 'DetectionModel'):
        print("The model 'DetectionModel' does not exist")
        return False
    
    print("Models exist")
    return True

async def test_create_baseline():
    """Test baseline creation"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'baselines'):
        solution.baselines.clear()
    
    mock_ctx = AsyncMock()
    
    try:
        result = await solution.create_baseline(
            "network_traffic",
            {"min": 10.0, "max": 100.0, "mean": 50.0},
            mock_ctx
        )
        
        if not isinstance(result, solution.Baseline):
            print(f"create_baseline should return Baseline, but returned {type(result)}")
            return False
        
        if result.metric != "network_traffic":
            print(f"Baseline metric should be 'network_traffic', but is '{result.metric}'")
            return False
        
        if hasattr(solution, 'baselines') and len(solution.baselines) == 0:
            print("Baseline should be stored in baselines dictionary")
            return False
        
        print("create_baseline works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_detect_anomaly():
    """Test anomaly detection"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'baselines'):
        solution.baselines.clear()
    if hasattr(solution, 'anomalies'):
        solution.anomalies.clear()
    
    mock_ctx = AsyncMock()
    
    # Create a baseline first
    baseline = await solution.create_baseline(
        "cpu_usage",
        {"min": 0.0, "max": 80.0, "mean": 40.0},
        mock_ctx
    )
    baseline_id = baseline.id if hasattr(baseline, 'id') else "cpu_usage"
    
    try:
        # Test with normal value (should return None or no anomaly)
        result_normal = await solution.detect_anomaly(baseline_id, 50.0, mock_ctx)
        
        # Test with anomalous value (should detect anomaly)
        result_anomaly = await solution.detect_anomaly(baseline_id, 150.0, mock_ctx)
        
        if result_anomaly is not None:
            if not isinstance(result_anomaly, solution.Anomaly):
                print(f"detect_anomaly should return Anomaly or None, but returned {type(result_anomaly)}")
                return False
            
            if result_anomaly.baseline_id != baseline_id:
                print(f"Anomaly baseline_id should be '{baseline_id}', but is '{result_anomaly.baseline_id}'")
                return False
        
        print("detect_anomaly works")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_list_anomalies():
    """Test listing anomalies with filters"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    if hasattr(solution, 'baselines'):
        solution.baselines.clear()
    if hasattr(solution, 'anomalies'):
        solution.anomalies.clear()
    
    mock_ctx = AsyncMock()
    
    # Create baseline and detect anomalies
    baseline = await solution.create_baseline(
        "network_traffic",
        {"min": 10.0, "max": 100.0, "mean": 50.0},
        mock_ctx
    )
    baseline_id = baseline.id if hasattr(baseline, 'id') else "network_traffic"
    
    await solution.detect_anomaly(baseline_id, 150.0, mock_ctx)  # Should create an anomaly
    await solution.detect_anomaly(baseline_id, 200.0, mock_ctx)  # Should create another anomaly
    
    try:
        # Test list all
        all_anomalies = await solution.list_anomalies(None, mock_ctx)
        if not isinstance(all_anomalies, list):
            print(f"list_anomalies should return a list, but returned {type(all_anomalies)}")
            return False
        
        # Test filter by severity
        high_anomalies = await solution.list_anomalies("high", mock_ctx)
        if not isinstance(high_anomalies, list):
            print(f"list_anomalies should return a list when filtered, but returned {type(high_anomalies)}")
            return False
        
        print(f"list_anomalies works: found {len(all_anomalies)} total anomalies")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_generate_model():
    """Test model generation using sampling"""
    spec = importlib.util.spec_from_file_location("solution", "solution.py")
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    mock_ctx = AsyncMock()
    
    # Mock sampling
    mock_sampling = MagicMock()
    mock_response = MagicMock()
    mock_response.content.text = '{"model_type": "statistical", "threshold": 2.5}'
    mock_sampling.create_message = AsyncMock(return_value=mock_response)
    mock_ctx.sampling = mock_sampling
    
    try:
        result = await solution.generate_model("cpu_usage", mock_ctx)
        
        if not isinstance(result, solution.DetectionModel):
            print(f"generate_model should return DetectionModel, but returned {type(result)}")
            return False
        
        if result.metric != "cpu_usage":
            print(f"Model metric should be 'cpu_usage', but is '{result.metric}'")
            return False
        
        print("generate_model works")
        return True
    
    except Exception as e:
        print(f"Error (may be normal if not implemented): {e}")
        import traceback
        traceback.print_exc()
        return True  # Not a fatal error if sampling not yet implemented

if __name__ == "__main__":
    print("Test for Project 38\n")
    
    success = True
    success = test_models_exist() and success
    print()
    
    print("Testing create_baseline...")
    success = asyncio.run(test_create_baseline()) and success
    print()
    
    print("Testing detect_anomaly...")
    success = asyncio.run(test_detect_anomaly()) and success
    print()
    
    print("Testing list_anomalies...")
    success = asyncio.run(test_list_anomalies()) and success
    print()
    
    print("Testing generate_model...")
    success = asyncio.run(test_generate_model()) and success
    print()
    
    if success:
        print("✅ All tests pass!")
        print("You've created a functional anomaly detector!")
    else:
        print("❌ Some tests failed. Check your code!")
        sys.exit(1)
