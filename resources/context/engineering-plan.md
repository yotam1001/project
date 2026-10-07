# Engineering plan — exploration rover

## Working objective

Demonstrate autonomous movement, obstacle avoidance, estimated position, and an initial 2D map in a small, flat, controlled arena representing narrow passages. Display progress on a phone. Add image capture, recording, and advisory AI hazard flags after the driving and mapping baseline works.

The prototype does not certify structural stability, air quality, human passage safety, or rescue suitability. No 3D reconstruction or vertical terrain/drop analysis is in the current milestone.

## Proposed computation and communication

- ESP motion controller: encoder acquisition, PI/PID wheel-speed control, immediate stop checks, and command timeout.
- Onboard Raspberry Pi: camera capture, time alignment, pose estimation, map updates, navigation decisions, event storage, web backend and asynchronous AI requests. This is the current plan; exact Pi model and processing performance are unverified.
- Camera: one separate ESP CAM S3 unit sending images over WiFi to Raspberry Pi.
- Laptop: operator browser, development and testing.
- Home PC: local Clef-Flash Q8_0 image inference. The user has checked hardware suitability.
- Phone: map, pose/path, status, captured events, AI decision probabilities/uncertainty, start/stop and manual control.
- ESP–Pi uses UART over USB serial in the initial plan; suitable ESP sensors use I2C. Phone/laptop–Pi uses Wi-Fi and WebSocket. The current proposal plans authenticated HTTPS internet exchange between Pi and the home-PC AI service; deployment details remain to be implemented. Local stop behavior must not depend on Raspberry Pi, the laptop or AI. Use timestamps, sequence numbers, bounded queues, command expiry, and a heartbeat. Stop motion on lost/stale commands or invalid critical sensing.
- At least one controller exchanges status/data with an internet service for the IoT requirement. Phone access over a local network alone is not proof of internet communication.

## Candidate algorithms — recommendations, not finalized decisions

1. Finite-state machine: idle, manual, autonomous, obstacle stop/avoidance, recovery, and fault.
2. PI/PID wheel-speed feedback from encoders; differential-drive kinematics to execute velocity commands.
3. Differential-drive odometry for planar position and heading; optionally gyro fusion after measuring drift.
4. Median or low-pass sensor filtering, with explicit treatment of invalid readings and data age.
5. Reactive obstacle avoidance as the first autonomous behavior, with an independently enforced local stop distance.
6. Occupancy grid: transform horizontal range observations using the estimated pose; mark observed free/occupied cells and retain unknown cells. A monocular image alone does not provide reliable metric range. The current plan uses USB 2D LiDAR for planar range mapping, supplemented by left/right ToF for side clearance.
7. A* path planning only after a usable map exists. Exploration/coverage planning is a separate later decision; obstacle avoidance alone does not ensure coverage.
8. Progress and timeout checks to detect stalls or repeated blocked behavior.

First maps will drift. Evaluate against a known arena before committing to full SLAM. Full SLAM, complete coverage, autonomous return, and real-cave operation are extensions, not initial deliverables.

## Camera hazard assessment goal

Define observable hazard categories with the supervisor: for example a blocked passage, a narrow opening, or a visually suspicious obstacle. Trigger capture from sensor events, operator marking, or a later validated visual detector; the trigger itself is not yet implemented. Retain a short clip or still, timestamp, estimated location, trigger reason, and model/version.

Preferred AI deployment is local inference on the user’s home PC, kept running when needed. The inference host is separate from the onboard Raspberry Pi and operator laptop; select an authenticated network connection and evaluate image-analysis latency during integration. The intended model is Cloudflare Clef-Flash, Q8_0, with image-input and structured decision support verified in published documentation. Runtime compatibility and PC performance still need testing; see ai-model.md. No runtime, downloads, or network service have been configured.

Send selected imagery to the chosen AI service. Store its advisory choices, model probabilities, input context, and request outcome. Clef-Flash does not generate free-form explanations; visible evidence annotations require a separate, explicitly designed method. Treat probabilities as model scores until calibration is evaluated. Display possible hazard, no hazard detected, or unknown. On timeout, missing imagery, or model failure, show unknown/pending. Navigation and local stop behavior do not wait for AI. Evaluate missed hazards and false alarms on controlled labelled scenes. The intended model is now identified; local execution is still untested.

## Build milestones and validation

1. Bench-test each intended student subsystem independently and settle school requirements.
2. Manual drive with local stopping, stable power, and measured encoder behavior.
3. Repeatable straight movement and turns; measure distance/heading error.
4. Autonomous obstacle avoidance; test different obstacle positions and communication loss.
5. Initial occupancy map and phone display; compare obstacle positions with measured arena ground truth.
6. Event capture, playback, and advisory AI assessment; test ambiguous scenes and service failure.
7. Integrated repeatable demonstration, physical measurements, photos/video, and project book.

Define numeric targets after hardware selection: collision count, stop distance, pose/map error, trial duration, connection-loss stop delay, capture completeness, and hazard-detection errors. The live proposal now sets planned targets of five collision-free trials, stopping within one second of command loss, and mean position error at most 30 cm in a small arena. No experimental results have been demonstrated.

Controller compliance remains unknown pending the user’s supervisor check next week.

## Diagram and component consistency

Current live proposal: one motion ESP, onboard Raspberry Pi, separate ESP CAM S3, one core USB 2D LiDAR, two side ToF sensors (left/right), two encoder motors, one IMU, two front/rear bumpers and four corner edge sensors. Motor-current and battery-voltage monitoring remain optional. The user-selected tldraw diagram is historical if its export predates this allocation; do not silently treat its older optional labels as current. Edge sensing is a stopping measure, not elevation mapping. School compliance remains open.

The app shows initial 2D occupancy map/path, camera imagery, map-linked events, advisory model scores and pending/unknown status, start/stop and manual controls. The AI model does not steer the rover. Concept images use example data, not live telemetry.
