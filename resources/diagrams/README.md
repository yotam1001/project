# Editable proposal block diagram

[Open the tldraw board](https://www.tldraw.com/f/4aOaHZDyKxk2AseGkkgxy)

The Google Docs proposal now uses the original **Page 1** (`page:page`), exactly as requested by the user. Its Raspberry Pi and simulated-cleaning labels are preserved. The proposal caption distinguishes that original diagram from the current laptop/camera plan; inserting it does not reinstate cleaning as the project goal.

The separate **תרשים מלבנים: הצעת הפרויקט** (`page:hebrew-proposal-rover`) page remains on the board but is not the diagram used in the Google Doc.

The current page shows the phone, laptop, home-PC image analysis, ESP motion controller, capture subsystem, sensors, motor drivers, camera, and power supply. Capture hardware and the two-controller compliance question remain unresolved. Arrows show data and commands; the power block is separate from the data flow.

- `tldraw-proposal-source.svg`: original SVG export from the current board page.
- `tldraw-proposal-render.svg`: export repaired for rendering, with visible text, Arial fallback, and no text outline shadow.
- `tldraw-proposal.png`: previously inserted Hebrew diagram, now replaced in the Google Doc.
- `tldraw-original-page-1-source.svg`: original Page 1 SVG export.
- `tldraw-original-page-1-render.svg`: visible-text export repair with outline shadows removed.
- `tldraw-original-page-1.png`: original Page 1 diagram now inserted in the Google Doc.

The tldraw exporter emitted hidden rich-text labels and an empty embedded font. The render repair changes presentation only; node text, rectangles, positions and arrow relationships come from the board. Regenerate these assets from the live board after diagram edits.
