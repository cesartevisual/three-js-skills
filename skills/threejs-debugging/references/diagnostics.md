# Symptom tree

| Symptom | First evidence | Focused next step |
| --- | --- | --- |
| Empty canvas | Console, element rect, render counter | Verify context and nonzero size; render an unlit subject |
| Model invisible | Bounds, camera, visibility/layers | Frame inspected bounds; check finite transforms |
| Model black | Unlit comparison, environment, normals | Separate lighting/reflection from texture/topology |
| Washed-out colors | Texture tags and output stages | Trace duplicate conversion and tone mapping |
| Parse exception | Actual HTTP response | Check HTML route fallback, CORS, decoders |
| Surface flicker | Camera planes, duplicate surfaces | Separate precision, overlap and transparency |
| Shadow stripes/detachment | Shadow frustum and scale | Tighten coverage and tune bias incrementally |
| Picking offset | View rectangle and pointer | Reproduce after scrolling; fix coordinates |
| Drag snaps under parent | Parent matrix and drag space | Convert world result to local parent space |
| Stale model appears | Request ordering | Guard completion and release superseded loads |
| Scene duplicates on navigation | Mount, loop, listener counts | Repair teardown and development remount assumptions |
| Demand scene freezes | Invalidation and motion owners | Invalidate mutations and ongoing damping |
| Context/device loss | Browser error and memory trend | Provide recovery and inspect resource pressure |

Preserve the minimal reproduction and original failing action. Remove diagnostic helpers/materials after fixing the cause. If browser access is unavailable, give precise reproduction steps and mark pixel verification as not run.
