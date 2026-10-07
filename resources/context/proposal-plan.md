# Proposal work plan — updated 7 October 2026

1. Confirm revised exploration-rover scope with the supervisor; pair project, 5 units already confirmed.
2. Define a controlled planar arena and the first milestone: autonomous movement, avoidance, and initial mapping. Cleaning is excluded; AI image assessment is an additional goal.
3. Settle two independently functional computing subsystems. The user will ask about compliance next week; leave acceptance unknown for now. ESP and onboard Raspberry Pi are now the planned processors. Verify each independently functioning subsystem meets the complete school requirements; a camera alone is not a controller.
4. Select motors/encoders, distance sensors, camera hardware, Raspberry Pi model, power supply, communication, operator laptop, and phone interface according to budget and available equipment.
5. Research source-backed alternatives: teleoperated inspection, autonomous planar mapping, and existing exploration robots. No commercial survey has yet been verified.
6. The live proposal selects 2D LiDAR, left/right ToF, IMU, bumpers, edge sensors and a separate ESP CAM S3. Finalize hardware models and basic algorithms. Define test metrics and error limits; leave full SLAM and real cave operation outside the first commitment.
7. Specify hazard capture, event storage, and AI advisory output. Preferred hosting is on the user’s home PC. Cloudflare Clef-Flash Q8_0 is the intended model, and image-input support is documented. The user has already checked hardware suitability. Verify compatible runtime integration and project-specific latency during implementation.
8. Complete cover details, explained block diagram, component list, and proposal PDF. Review revised scope and acceptance criteria with the supervisor.

The deadline around the 15th is for the proposal only; its full date is unconfirmed. The current circular's examiner-submission deadline is 30 October of the school year. The live Google Doc is authoritative. The repository text and native exports are synchronized references; do not overwrite the live document with older drafts.

## Latest synchronization
The live document now has goal/problem and cover names, camera and sensor allocation, HTTPS home-PC AI exchange, and planned numeric targets. These supersede older open placeholders and optional sensor labels. Web app concept must depict exploration, mapping, camera events and advisory AI review.
