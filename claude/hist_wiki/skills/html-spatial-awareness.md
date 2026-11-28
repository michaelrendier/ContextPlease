# html-spatial-awareness

**Skill:** `~/.claude/skills/html-spatial-awareness/` · mirror `ContextPlease/claude/skills/html-spatial-awareness/` · **Created:** 2026-11-24 (author: Cody Michael Allison): "i want you to use it to give you an 'html spacial awareness' skill...for when doing my gallery pages ... make a sub gallery for visualizations i have you do in javascript ... ensure they are named according to the type of code inside."

How to give an HTML page a space: panels as viewports, y-up buffers, yaw/pitch/distance cameras, a path parameter that drives colour and growth; when to use raw WebGL, three.js, Canvas 2D, SVG, CSS 3-D, React; Cody's gallery conventions; the JavaScript sub-gallery naming rule; a headless-Firefox verification recipe.

**Findings at creation (measured):**
- The collection `xml12333/HTML_CSS_JS` is a learner's archive of 1,160 front-end projects; of those, 201 use requestAnimationFrame, 186 SVG, 89 GSAP, 88 Canvas 2D, 74 GLSL, 45 raw WebGL, 43 three.js, 13 React.
- Four failures recorded as rules: additive glow saturates (scale alpha with count); equal-phase sampling draws fake spokes; file:// cannot fetch local data (bake base64 into a script); headless Firefox cannot capture WebGL (use ?snap=1).
- React Native is a mobile framework; browser pages from Gemini are normally React/JSX (untested here).

## 2026-11-28: section 8, CherryPy

Cody: "update your HTML skill with CherryPy... that is what I am using for the web API for PTorrent." Section 8 of the skill records the loopback JSON API recipe (one app serves the page and `/api`, MethodDispatcher, `json_in`/`json_out`, `serve_file` for Range, server-sent events, JSON error pages, background tasks, CORS only when the origin differs). The recipe was run and checked the same day (index, JSON GET and POST, Range 206, SSE, JSON 404) in `ValaQuenta/.venv` (CherryPy 18.10). The tutorials already in the repository are `Ptolemy2/Mouseion/cherrypy/`.
