# Engineering plan — exploration rover

## Working objective

Demonstrate autonomous movement, obstacle avoidance, estimated position, and an initial 2D map in a small, flat, controlled arena representing narrow passages. Display progress on a phone. Add image capture, recording, and advisory AI hazard flags after the driving and mapping baseline works.

The prototype does not certify structural stability, air quality, human passage safety, or rescue suitability. No 3D reconstruction or vertical terrain/drop analysis is in the current milestone.

## Proposed computation and communication

- ESP motion controller: encoder acquisition, PI/PID wheel-speed control, immediate stop checks, and command timeout.
- Camera subsystem: capture and stream imagery; processor-equipped hardware and independent function are pending selection.
- Laptop: time alignment, pose estimation, map updates, navigation decisions, event storage, and AI requests.
- Phone: map, pose/path, status, captured events, AI reasoning/uncertainty, start/stop and manual control.
- Wi-Fi transports data and commands; local stop behavior must not depend on the laptop or cloud. Use timestamps, sequence numbers, bounded queues, command expiry, and a heartbeat. Stop motion on lost/stale commands or invalid critical sensing.
- At least one controller exchanges status/data with an internet service for the IoT requirement. Phone access over a local network alone is not proof of internet communication.

## Candidate algorithms — recommendations, not finalized decisions

1. Finite-state machine: idle, manual, autonomous, obstacle stop/avoidance, recovery, and fault.
2. PI/PID wheel-speed feedback from encoders; differential-drive kinematics to execute velocity commands.
3. Differential-drive odometry for planar position and heading; optionally gyro fusion after measuring drift.
4. Median or low-pass sensor filtering, with explicit treatment of invalid readings and data age.
5. Reactive obstacle avoidance as the first autonomous behavior, with an independently enforced local stop distance.
6. Occupancy grid: transform horizontal range observations using the estimated pose; mark observed free/occupied cells and retain unknown cells. A monocular image alone does not provide reliable metric range. Select ToF, LiDAR, another range method, or a calibrated vision approach before claiming metric mapping.
7. A* path planning only after a usable map exists. Exploration/coverage planning is a separate later decision; obstacle avoidance alone does not ensure coverage.
8. Progress and timeout checks to detect stalls or repeated blocked behavior.

First maps will drift. Evaluate against a known arena before committing to full SLAM. Full SLAM, complete coverage, autonomous return, and real-cave operation are extensions, not initial deliverables.

## Camera hazard assessment goal

Define observable hazard categories with the supervisor: for example a blocked passage, a narrow opening, or a visually suspicious obstacle. Trigger capture from sensor events, operator marking, or a later validated visual detector; the trigger itself is not yet implemented. Retain a short clip or still, timestamp, estimated location, trigger reason, and model/version.

Send selected imagery to the chosen AI service. Store its advisory result, evidence/reasoning, uncertainty, and request outcome. Display possible hazard, no hazard detected, or unknown. On timeout, missing imagery, or model failure, show unknown/pending. Navigation and local stop behavior do not wait for AI. Evaluate missed hazards and false alarms on controlled labelled scenes. The ambiguous spoken model name remains unresolved.

## Build milestones and validation

1. Bench-test each intended student subsystem independently and settle school requirements.
2. Manual drive with local stopping, stable power, and measured encoder behavior.
3. Repeatable straight movement and turns; measure distance/heading error.
4. Autonomous obstacle avoidance; test different obstacle positions and communication loss.
5. Initial occupancy map and phone display; compare obstacle positions with measured arena ground truth.
6. Event capture, playback, and advisory AI assessment; test ambiguous scenes and service failure.
7. Integrated repeatable demonstration, physical measurements, photos/video, and project book.

Define numeric targets after hardware selection: collision count, stop distance, pose/map error, trial duration, connection-loss stop delay, capture completeness, and hazard-detection errors. No targets or experimental results have yet been confirmed.
