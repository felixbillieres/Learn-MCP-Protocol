# Instructions - Project 38 (Anomaly Detector)

## Your Mission

Create an anomaly detection system with baselines and real-time alerting.

## Steps to Follow

1. **Create Pydantic Models**:
   - `Baseline`:
     - `id` : str
     - `metric` : str (e.g., "network_traffic", "cpu_usage", "login_attempts")
     - `normal_range` : Dict[str, float] (min, max, mean)
     - `created_at` : str
   - `Anomaly`:
     - `id` : int
     - `baseline_id` : str
     - `metric_value` : float
     - `deviation` : float
     - `severity` : str (enum: "low", "medium", "high", "critical")
     - `detected_at` : str
     - `description` : str
   - `DetectionModel`:
     - `id` : str
     - `name` : str
     - `parameters` : Dict[str, Any]
     - `accuracy` : float | None

2. **Create Server with Subscriptions**:
   ```python
   capabilities={"resources": {"subscribe": True}}
   ```

3. **Create Tools**:
   - `creer_baseline` : Create baseline for a metric
   - `detecter_anomalie` : Detect anomalies in metrics
   - `lister_anomalies` : List detected anomalies
   - `generer_modele` : Generate detection model (uses sampling)

4. **Create Resources**:
   - `anomaly://recent` : Recent anomalies
   - `baseline://list` : List baselines

5. **Implement Subscriptions**:
   - Subscribe to anomaly alerts
   - Notify when anomalies are detected

6. **Use Sampling**:
   - Generate detection models
   - Suggest threshold values

## Hints

- Store baselines: `baselines: Dict[str, Baseline] = {}`
- Store anomalies: `anomalies: List[Anomaly] = []`
- Calculate deviation from baseline
- Use subscriptions for real-time alerts

## Test

Use `python test.py` to verify anomaly detection.

