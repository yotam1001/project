# Current rover diagram

[Current proposal block diagram](current-proposal-block-diagram.png) was synchronized with the live written proposal on 7 October 2026. It includes motion ESP, Pi mapping/backend, USB 2D LiDAR, separate WiFi ESP CAM S3, left/right ToF, encoders/IMU, two bumpers, four edge sensors, browser operation and authenticated HTTPS home-PC Clef-Flash inference. It is inserted in the current Google Doc.

`build_current_diagram.py` regenerates this diagram, reusing the handwriting font embedded in the existing tldraw SVG. It preserves that handwritten visual style. Motor-current and battery-voltage monitoring remain optional and are not depicted as core.

The user's [tldraw board](https://www.tldraw.com/f/4aOaHZDyKxk2AseGkkgxy) and exported SVGs/PNGs below are historical assets, not current architecture authority. They are retained to preserve editable source history; the board itself was not changed in this synchronization.

## Historical export notes

# Current editable block diagram

[Open the tldraw board](https://www.tldraw.com/f/4aOaHZDyKxk2AseGkkgxy)

The earlier proposal used updated **Page 1** (`page:page`). The current architecture is ESP motion control and stopping, onboard Raspberry Pi capture/mapping/navigation/backend, browser access from phone/laptop, and home-PC Clef-Flash Q8_0 analysis. Cleaning has been removed. Right ToF, LiDAR and additional protection/monitoring sensors are marked optional.

All text-bearing shapes on Page 1 use tldraw's handwriting font (`draw`). The separate Hebrew page is an earlier reference and is not used in the proposal.

- `tldraw-current-pi-source.svg`: current live board export.
- `tldraw-current-pi-render.svg`: visible-label rendering repair, with embedded Shantell Sans informal handwriting for reliable export.
- `tldraw-current-pi.png`: current diagram inserted in Google Docs.
- `tldraw-original-page-1-*`: historical pre-update exports.
- `tldraw-proposal-*`: earlier Hebrew-page exports.

The exporter emitted hidden labels and empty font sources. Rendering repairs preserve the board's shapes, labels, geometry and arrow connections. The repair embeds the OFL-licensed Shantell Sans font from Google Fonts, using its informal axis. Regenerate exports after editing the live board.
