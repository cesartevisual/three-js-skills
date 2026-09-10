# Behavioral evaluation scenarios

Evaluation briefs, not completed cross-agent certification. Use temporary applications, supply the request/fixture and indicated skills, then inspect actual code and browser behavior. Matching phrases alone is insufficient.

| Request and fixture | Skills | Pass criteria |
| --- | --- | --- |
| Fix cropping when a sidebar opens; non-square panel, wide model | scene, debugging | Container sizing, projection update, fits width/height, zero-size recovery |
| Switch GLBs without leaks; shared textures, out-of-order loads | assets, performance | No stale replacement, shared ownership preserved, repeated-cycle memory evidence |
| Fix development Strict Mode; external primitives, cached loaders | r3f | Checks peers, repairs lifecycle without disabling Strict Mode or prematurely disposing cache |
| Port GLSL/composer to WebGPU on a pinned older revision | webgpu, shaders, postprocessing | Inspects APIs, ports incompatible stages, tests or explicitly limits fallback claims |
| Configurator must work without dragging | product-viewer, accessibility | Synchronized HTML options/reset, keyboard focus, reduced motion, fallback |
| Decoder URL returns HTML under /shop/ | deployment, debugging | Inspects response, fixes build-aware URL, verifies production base path |
| Physics explodes after tab resume | physics | Fixed step, bounded backlog, single owner, tests fast collision/resume |
| Measure a known span in georeferenced BIM | spatial-data | Reversible local origin, units and round-trip checked, measured tolerance |
| AR placement with emulator but no real device | xr | Correct session states and fallback, hardware verification explicitly not run |
| Change a form button color beside an untouched canvas | none | Requested CSS only, no unnecessary renderer workflow |

Expand skill names with `threejs-`. Record host/model version, fixture commit, prompt, loaded skills, artifacts, failures, and targeted corrections. Run relevant scenarios on each intended host before advertising behavioral certification.
