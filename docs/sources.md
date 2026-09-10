# Sources and attribution

Inspected the user-supplied OpenAEC Foundation `Three.js-Claude-Skill-Package-master`, package version 1.1.0. Its taxonomy informed coverage. Its README, renderer skill, and React Three Fiber skill were inspected; instructions and code were not copied into this collection. The original local package remains unchanged.

The new collection favors task-specific decisions over universal ALWAYS/NEVER rules and does not inherit the reference's broad r160+ compatibility claim.

The installation-first README and simpler repository presentation also take inspiration from [GSAP Skills](https://github.com/greensock/gsap-skills). No GSAP instructions or plugin manifests were copied.

## Packaging references

Checked September 10, 2026:

- [Agent Skills specification](https://agentskills.io/specification): frontmatter and folder structure.
- [Claude Code](https://code.claude.com/docs/en/skills): discovery and invocation.
- [Codex](https://learn.chatgpt.com/docs/build-skills): `.agents/skills`, progressive disclosure, invocation.
- [Cursor](https://cursor.com/docs/skills): `.cursor/skills` and compatible directories.

## Technical references

- [Three.js API](https://threejs.org/docs/) and [manual](https://threejs.org/manual/): resolve APIs against installed revisions.
- [WebGPURenderer](https://threejs.org/docs/pages/WebGPURenderer.html) and [TSL](https://threejs.org/docs/pages/TSL.html): backend and shader guidance.
- [GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html), [Material](https://threejs.org/docs/pages/Material.html), [InstancedMesh](https://threejs.org/docs/pages/InstancedMesh.html), [AnimationMixer](https://threejs.org/docs/pages/AnimationMixer.html), [Raycaster](https://threejs.org/docs/pages/Raycaster.html): feature APIs.
- [Fiber introduction](https://r3f.docs.pmnd.rs/getting-started/introduction) and [migration guide](https://r3f.docs.pmnd.rs/tutorials/v9-migration-guide): React/Fiber coupling. Direct retrieval was unreliable; indexed official excerpts were available. Skills require installed peer checks instead of freezing version recommendations.
- [Rapier integration parameters](https://rapier.rs/docs/user_guides/javascript/integration_parameters/): stepping behavior.
- [MDN WebXR](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API): capability/session constraints.

Individual skills link further official documentation for implementation-time lookup. Links do not imply that every page or device combination was tested. Some Three.js manual URLs could not be retrieved; use the index or installed source if a deep link moves.
